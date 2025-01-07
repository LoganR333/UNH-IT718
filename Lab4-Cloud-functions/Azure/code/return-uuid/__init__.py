import json
import uuid
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    new_uuid = uuid.uuid4()
    return func.HttpResponse(
        f"Generated UUID: {new_uuid}",
        status_code=200
    )
