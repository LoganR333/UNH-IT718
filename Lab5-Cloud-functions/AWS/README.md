# AWS												
1.	Identify static web site you would like to publish on the web.
2.	Push the web content to cloud storage.
3.	Make the cloud storage publicly available.

### Creat Database
aws dynamodb create-table \
    --table-name manage_session \
    --attribute-definitions AttributeName=email,AttributeType=S \
    --key-schema AttributeName=email,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST

### Deploy cloud function using IAM and deployment process from previous lab
```
ROLE_ARN=` aws iam get-role --role-name LambdaBasicExecutionRole --query "Role.Arn" --output text`
zip function.zip manage_session.py
aws lambda create-function --function-name manage_session --runtime python3.13 \
    --role $ROLE_ARN --handler manage_session.lambda_handler --zip-file fileb://function.zip
aws lambda create-function-url-config --function-name manage_session --auth-type NONE
aws lambda add-permission --function-name manage_session --action lambda:InvokeFunctionUrl \
    --principal "*" --function-url-auth-type NONE --statement-id FunctionURLPublicAccess
```

### Sample screenshots
![CLI screen capture](lab5-aws-cli.png)
![Website home page](lab5-aws-website.png)
