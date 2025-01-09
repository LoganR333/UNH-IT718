import json
import uuid
from google.cloud import firestore
import functions_framework

db = firestore.Client()

@functions_framework.http

def handler(request):
    # Parse the request path
    path = request.path
    email = request.args.get('email')

    if path == '/':
        return handle_uuid()
    
    if not email:
        return "Missing 'email' parameter.", 400

    if path == '/new':
        return handle_new(email)
    elif path == '/get':
        # fix to cookie? uuid = request.cookies.get('uuid')
        uuid = request.args.get('uuid')
        return handle_get(email, uuid)
    else:
        return "Invalid path. Use /new or /get.", 404


def handle_uuid():
    new_uuid = str(uuid.uuid4())

    response_content = f"""
    <html>
    <body>
        <p>UUID: {new_uuid}</p>
    </body>
    </html>
    """
    response = html_response(response_content)
    return response 

def handle_new(email):
    """Handles the /new path by storing email and UUID in Firestore."""
    new_uuid = str(uuid.uuid4())

    try:
        # Store the email and UUID in Firestore
        db.collection('return-uuid').document(email).set({'uuid': new_uuid})
    except Exception as e:
        return f"Error storing data: {str(e)}", 500

    response_content = f"""
    <html>
    <body>
        <h1>Record Created</h1>
        <p>Email: {email}</p>
        <p>UUID: {new_uuid}</p>
    </body>
    </html>
    """
    response = html_response(response_content)
    response.headers['Set-Cookie'] = f"uuid={new_uuid}; Path=/; HttpOnly"
    return response 

def handle_get(email, uuid):
    """Handles the /get path by comparing the cookie value with the stored UUID."""
    if not uuid:
        return "Missing 'uuid' query parameter.", 400

    try:
        # Retrieve the record from Firestore
        doc_ref = db.collection('return-uuid').document(email)
        doc = doc_ref.get()

        if not doc.exists:
            return "Record not found.", 404

        # Compare the UUID in the cookie with the stored UUID
        stored_uuid = doc.to_dict().get('uuid')
        response_content = f"""
        <html>
        <body>
            <h1>UUID check</h1>
            <p>stored uuid: {stored_uuid}</p>
            <p>request uuid: {uuid}</p>
        </body>
        </html>
        """
        response = html_response(response_content)
        response.headers['Set-Cookie'] = f"uuid={uuid}; Path=/; HttpOnly"
        return response
        
    except Exception as e:
        return f"Error retrieving data: {str(e)}", 500

def html_response(content, status=200):
    from flask import Response
    return Response(response=content, status=status, mimetype="text/html")
    
if __name__ == "__main__":
    # Explicitly bind to the port specified by the environment variable PORT (default: 8080)
    port = int(os.environ.get('PORT', 8080))
    print(f"Listening on port {port}")
    # The functions_framework will automatically start the HTTP server and listen on the given port
    from functions_framework import run
    run(host='0.0.0.0', port=port)
