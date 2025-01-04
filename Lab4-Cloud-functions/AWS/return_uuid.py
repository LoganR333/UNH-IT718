import json
import uuid
import logging

def lambda_handler(event, context):
    # Generate a UUID
    generated_uuid = "monkeys:" + str(uuid.uuid4())
    logging.info(f"Generated UUID: {generated_uuid}")
    
    # Create HTML response
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>Your session UUID: {generated_uuid}.</p>
    </body>
    </html>
    """
    
    # Return the response with the Set-Cookie header
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
            "Pragma": "no-cache",
            "Expires": "0",
            "Set-Cookie": f"test-id={generated_uuid}; Path=/; HttpOnly"
        },
        "body": html_content
    }

if __name__ == '__main__':
     logging.info(lambda_handler(0,0))
