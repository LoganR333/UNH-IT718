import os
import json
import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME'] # set by cloudformation
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Parse the request body
        body = json.loads(event['body'])
        email = body.get('email', None)

        if not email or not action:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing 'email' or 'action' in request body."})
            }

        if action == "create":
            # Add a new item to DynamoDB
            table.put_item(Item={"email": email, "message": "Welcome to DynamoDB!"})
            return {
                "statusCode": 200,
                "body": json.dumps({"message": f"User {email} added to the table."})
            }

        elif action == "read":
            # Retrieve an item from DynamoDB
            response = table.get_item(Key={"email": email})
            item = response.get('Item', None)
            if not item:
                return {
                    "statusCode": 404,
                    "body": json.dumps({"message": f"User {email} not found."})
                }
            return {
                "statusCode": 200,
                "body": json.dumps(item)
            }

        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Invalid action. Use 'create' or 'read'."})
            }

    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "DynamoDB error.", "error": str(e)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error.", "error": str(e)})
        }
