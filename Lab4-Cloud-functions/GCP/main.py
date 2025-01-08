import json
import uuid
from google.cloud import firestore
import functions_framework

# Initialize Firestore client
db = firestore.Client()

@functions_framework.http

def handler(request):
    # Parse the request path
    path = request.path
    email = request.args.get('email')

    if not email:
        return "Missing 'email' parameter.", 400

    if path == '/new':
        return handle_new(email)
    elif path == '/get':
        cookie = request.cookies.get('uuid')
        return handle_get(email, cookie)
    else:
        return "Invalid path. Use /new or /get.", 404


def handle_new(email):
    """Handles the /new path by storing email and UUID in Firestore."""
    new_uuid = str(uuid.uuid4())

    try:
        # Store the email and UUID in Firestore
        db.collection('return-uuid').document(email).set({'uuid': new_uuid})
    except Exception as e:
        return f"Error storing data: {str(e)}", 500

    # Set the UUID as a cookie
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

    try:
        # Retrieve the record from Firestore
        doc_ref = db.collection('return-uuid').document(email)
        doc = doc_ref.get()

        if not doc.exists:
            return "Record not found.", 404

        # Compare the UUID in the cookie with the stored UUID
        stored_uuid = doc.to_dict().get('uuid')
        if stored_uuid == cookie:
            return {"statusCode": 200, "body": json.dumps({"message": "UUID matches"})}
        else:
            return {"statusCode": 403, "body": json.dumps({"message": "UUID does not match"})}

    except Exception as e:
        return f"Error retrieving data: {str(e)}", 500

if __name__ == "__main__":
    # Explicitly bind to the port specified by the environment variable PORT (default: 8080)
    port = int(os.environ.get('PORT', 8080))
    print(f"Listening on port {port}")
    # The functions_framework will automatically start the HTTP server and listen on the given port
    from functions_framework import run
    run(host='0.0.0.0', port=port)
