def main(req: func.HttpRequest) -> func.HttpResponse:
    # Check if the request is for favicon.ico
    if req.url.endswith('/favicon.ico'):
        return func.HttpResponse("", status_code=204) 
    return get_response()

def get_response():
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
