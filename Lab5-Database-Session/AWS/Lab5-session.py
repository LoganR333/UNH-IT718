import boto3
import json
import uuid
from http import cookies

# Initialize DynamoDB client and table
DYNAMO_TABLE_NAME = 'Lab5-session'
dynamo = boto3.resource('dynamodb').Table(DYNAMO_TABLE_NAME)

def lambda_handler(event, context):
    status_code = 200
    headers = {"Content-Type": "application/json"}
    body = None

    try:
        raw_path = event.get('rawPath', '')
        query_params = event.get('queryStringParameters', {})
        email = query_params.get('email')

        if not email:
            raise ValueError("Missing 'email' query parameter")

        if raw_path == "/new":
            # Generate a new UUID and store in DynamoDB
            user_uuid = str(uuid.uuid4())
            dynamo.put_item(
                Item={
                    'email': email,
                    'uuid': user_uuid
                }
            )

            # Set UUID in a cookie
            cookie = cookies.SimpleCookie()
            cookie['uuid'] = user_uuid
            cookie['uuid']['path'] = '/'
            cookie['uuid']['httponly'] = True
            headers['Set-Cookie'] = cookie.output(header='', sep='').strip()

            body = json.dumps({"message": "User created", "uuid": user_uuid})

        elif raw_path == "/get":
            # Retrieve the record from DynamoDB
            record = dynamo.get_item(Key={'email': email})

            if 'Item' not in record:
                raise ValueError("Record not found for the provided email")

            stored_uuid = record['Item']['uuid']

            # Retrieve the UUID from the request's cookies
            request_cookies = event.get('headers', {}).get('cookie', '')
            cookie = cookies.SimpleCookie(request_cookies)
            received_uuid = cookie.get('uuid')

            if not received_uuid or received_uuid.value != stored_uuid:
                raise ValueError("UUID mismatch or missing cookie")

            body = json.dumps({"message": "UUID verified", "email": email})

        else:
            raise ValueError(f"Unsupported route: {raw_path}")

    except Exception as e:
        status_code = 400
        body = json.dumps({"error": str(e)})

    return {
        'statusCode': status_code,
        'body': body,
        'headers': headers
    }
