import os
import json
import boto3
import uuid
from google.oauth2 import id_token
from google.auth.transport import requests

CLIENT_ID = "958115105182-0rvbal5tufba8jsubammhgq3ee149vdu.apps.googleusercontent.com"

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME'] # set by cloudformation
table = dynamodb.Table(table_name)

def handler(event, context):
    try:

        # Parse JSON body
        body = json.loads(event["body"])
        token = body.get("idToken")
        
        if not token:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "JWT is required"})
            }
        
        # Call Google service to validate JWT
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        sub = idinfo['sub']
        email = idinfo['email']
        user_uuid = str(uuid.uuid4())

        # Update the database
        table.put_item(Item={"email": email, "uuid": user_uuid})

        # TODO/FIX the cookie options
        return {
            "statusCode": 200,
            "headers": { {"Content-Type": "application/json"},
                       {"Set-Cookie", "sub="+sub+"; HttpOnly; Secure=false; SameSite=Lax; Path=/" } },
            "body": json.dumps({"message": "Session created", "uuid": user_uuid})
        }
    
    except ValueError:
        # Invalid token
        self.send_response(401)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "Invalid JWT"}).encode('utf-8'))
