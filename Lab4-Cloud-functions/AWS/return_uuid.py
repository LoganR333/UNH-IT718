import json
import uuid
import logging

def lambda_handler(event, context):
    # Generate a UUID
    print("Event:", json.dumps(event))
    print("Context:", str(context))
    generated_uuid = str(uuid.uuid4())
    print(f"Generated UUID: {generated_uuid}")
    
    # Create HTML response
    html_1 = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>Your session UUID: """
    html_2 = f""".</p>
    </body>
    </html>
    """
    
    html_content = html_1 + generated_uuid + html_2
    
    # Return the response with the Set-Cookie header
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
            "Pragma": "no-cache",
            "Expires": "0",
            "Set-Cookie": "test-id=" + generated_uuid + "; Path=/; HttpOnly"
        },
        "body": html_content
    }

if __name__ == '__main__':
     print(lambda_handler(0,0))
