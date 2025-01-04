# AWS												
1.	Identify static web site you would like to publish on the web.
2.	Push the web content to cloud storage.
3.	Make the cloud storage publicly available.

### Review sample code
```
import json
import uuid

def lambda_handler(event, context):
    # Generate a UUID
    generated_uuid = str(uuid.uuid4())
    
    # Create HTML response
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>Your session UUID has been set.</p>
    </body>
    </html>
    """
    
    # Return the response with the Set-Cookie header
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Set-Cookie": f"session-id={generated_uuid}; Path=/; HttpOnly"
        },
        "body": html_content
    }
```
### Sample screenshots
![CLI screen capture](lab5-aws-cli.png)
![Website home page](lab5-aws-website.png)
