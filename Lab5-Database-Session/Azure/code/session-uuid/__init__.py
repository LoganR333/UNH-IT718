import logging
import azure.functions as func
from azure.data.tables import TableServiceClient
import uuid
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("test",status_code=200)
