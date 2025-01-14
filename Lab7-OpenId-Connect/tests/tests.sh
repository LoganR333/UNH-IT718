# Various tests as componeents deploy
curl -X POST https://it718lab7.kengraf.com/v1/verifyToken \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "action": "create"}'

curl -X POST https://d3obdogsmpp9uy.cloudfront.net/v1/verifyToken \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "action": "create"}'

curl -X POST https://6863p36t83.execute-api.us-east-2.amazonaws.com/v1/verifyToken \
  -H "Content-Type: application/json" \
  -d '{"id_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"}'

  {
  "httpMethod": "POST",
  "body": "{\"jwt\": \"your-jwt-token-here\"}"
}

# S3 URL
# Lambda URL
# API Gateway URL
# CloudFront URL
# Customized domain

# /index.html redirects to /login.html if "session" cookie; else display query parameters and session cookie
# /v1/verifyToken
# POST with jwt in body, jwt is sent to Google for verification


# lambda endpoint
https://it718lab7.s3.us-east-2.amazonaws.com/login.html

https://kvyedg0ezb.execute-api.us-east-2.amazonaws.com/v1/verifyToken
