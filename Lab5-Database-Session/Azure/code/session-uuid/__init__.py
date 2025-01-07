import logging
import azure.functions as func

import uuid
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("test",status_code=200)
