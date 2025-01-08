import json
import uuid
from google.cloud import bigtable

# Initialize Bigtable client
client = bigtable.Client(project="your-project-id", admin=True)  # Replace with your project ID
instance = client.instance("your-instance-id")  # Replace with your Bigtable instance ID
table = instance.table("email_table")  # Replace with your Bigtable table name

def handler(request):
    """
    Cloud Function to handle two paths:
    - /new: Stores email and UUID in Bigtable and returns UUID as a cookie.
    - /get: Retrieves the email record from Bigtable and compares the UUID cookie.

    Args:
        request: HTTP request object.

    Returns:
        HTTP response.
    """
    path = request.path
    email = request.args.get("email")

    if not email:
        return "Missing 'email' parameter.", 400

    if path == "/new":
        return handle_new(email)
    elif path == "/get":
        cookie = request.cookies.get("uuid")
        return handle_get(email, cookie)
    else:
        return "Invalid path. Use /new or /get.", 404


def handle_new(email):
    """Handles the /new path by storing email and UUID in Bigtable."""
    new_uuid = str(uuid.uuid4())
    row_key = email.encode("utf-8")

    try:
        # Store email and UUID in Bigtable
        row = table.row(row_key)
        row.set_cell("user_data", "uuid", new_uuid)
        row.commit()
    except Exception as e:
        return f"Error storing data: {str(e)}", 500

    # Return the UUID as a cookie
    response = {
        "statusCode": 200,
        "headers": {
            "Set-Cookie": f"uuid={new_uuid}; Path=/; HttpOnly"
        },
        "body": json.dumps({"message": "Record created", "uuid": new_uuid})
    }
    return response


def handle_get(email, cookie):
    """Handles the /get path by comparing the cookie value with the stored UUID."""
    if not cookie:
        return "Missing 'uuid' cookie.", 400

    row_key = email.encode("utf-8")

    try:
        # Retrieve the record from Bigtable
        row = table.read_row(row_key)
        if not row:
            return "Record not found.", 404

        stored_uuid = row.cell_value("user_data", "uuid").decode("utf-8")
        if stored_uuid == cookie:
            return {"statusCode": 200, "body": json.dumps({"message": "UUID matches"})}
        else:
            return {"statusCode": 403, "body": json.dumps({"message": "UUID does not match"})}
    except Exception as e:
        return f"Error retrieving data: {str(e)}", 500
