# Various tests as componeents deploy
curl -X POST https://<api-endpoint>/trigger \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "action": "create"}'

curl -X POST https://<api-endpoint>/trigger \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "action": "read"}'

  {
  "httpMethod": "POST",
  "body": "{\"jwt\": \"your-jwt-token-here\"}"
}

# lambda endpoint
https://it718lab7.s3.us-east-2.amazonaws.com/login.html
