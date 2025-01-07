import logging
import azure.functions as func
from azure.data.tables import TableServiceClient
import uuid
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("test",status_code=200)
    create_table_if_not_exists()  # Ensure the table exists

    
    try:
        # Parse request
        path = req.route_params.get("path", "")
        email = req.params.get("email")
        if not email:
            return func.HttpResponse("Missing 'email' query parameter.", status_code=400)

        if path == "new":
            # Generate and store a new UUID
            new_uuid = str(uuid.uuid4())
            entity = {"PartitionKey": email, "RowKey": email, "uuid": new_uuid}
            table_client.upsert_entity(entity)
            return func.HttpResponse(f"UUID stored: {new_uuid}", status_code=200)

        elif path == "get":
            # Validate UUID
            provided_uuid = req.params.get("uuid")
            if not provided_uuid:
                return func.HttpResponse("Missing 'uuid' query parameter.", status_code=400)

            # Retrieve the stored UUID
            entity = table_client.get_entity(partition_key=email, row_key=email)
            stored_uuid = entity["uuid"]

            if stored_uuid == provided_uuid:
                return func.HttpResponse("UUID validated successfully.", status_code=200)
            else:
                return func.HttpResponse("UUID mismatch.", status_code=400)

        else:
            return func.HttpResponse(f"Unsupported path: {path}", status_code=404)

    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)
