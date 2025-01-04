import json
import uuid

def lambda_handler(event, context):
    # Generate a UUID
    print("Event:", json.dumps(event))
    print("Context:", str(context))
    
    path = event.get('rawPath', '/')
    if path == '/favicon.ico':
        return {
            "statusCode": 404,
            "body": "Not Found"
        }
    
    res = get_response()
    print(json.dumps(res))
    return(res)

def get_response():
    generated_uuid = str(uuid.uuid4())
    print(f"Generated UUID: {generated_uuid}")
    
    # Create HTML response
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>Your session UUID: {generated_uuid}</p>
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
