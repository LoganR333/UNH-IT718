import json
import uuid
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return get_response()

def get_response():
    # Generate a UUID
    
    generated_uuid = uuid.uuid4()
    
    # Create HTML response
    html_content = f"""
        <h1>Hello, World!</h1>
        <p>Your session UUID: {generated_uuid}</p>
    """
    logging.info('got past content')
    
    response = func.HttpResponse(
        body=html_content,
        status_code=200,
        mimetype="html/text"
        }
    response.headers["Set-Cookie"] = f"test-id={generated_uuid}; Path=/"

    return response
    
