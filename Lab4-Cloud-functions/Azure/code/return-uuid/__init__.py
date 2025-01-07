import json
import uuid
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Check if the request is for favicon.ico
    if req.url.endswith('/favicon.ico'):
        return func.HttpResponse("", status_code=204) 

    generated_uuid = uuid.uuid4()
    
    # Create HTML response
    html_content = f"<h1>Hello, World!</h1><p>Your session UUID: {generated_uuid}</p>"
    
    response = func.HttpResponse(
        body=html_content,
        status_code=200,
        mimetype="text/html"
        )
    response.headers["Set-Cookie"] = f"test-id={generated_uuid}; Domain=azurewebsites.net; Path=/"

    return response
    
