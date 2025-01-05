# AWS												
1.	Identify static web site you would like to publish on the web.
2.	Push the web content to cloud storage.
3.	Make the cloud storage publicly available.

### Deploy cloud function
Using IAM and deployment process from previous lab (names and policy edits)
```
aws iam create-role --role-name LambdaDynamoDBRole --assume-role-policy-document file://trust-policy.json
ROLE_ARN=` aws iam get-role --role-name LambdaDynamoDBRole --query "Role.Arn" --output text`
aws iam put-role-policy --role-name LambdaDynamoDBRole --policy-name DynamoDBAccessPolicy \
    --policy-document policy.json
zip function.zip Lab5_session.py
aws lambda create-function --function-name Lab5_session --runtime python3.13 \
    --role $ROLE_ARN --handler Lab5_session.lambda_handler --zip-file fileb://function.zip
aws lambda create-function-url-config --function-name Lab5_session --auth-type NONE
aws lambda add-permission --function-name Lab5_session --action lambda:InvokeFunctionUrl \
    --principal "*" --function-url-auth-type NONE --statement-id FunctionURLPublicAccess
```
### Creat Database
aws dynamodb create-table \
    --table-name Lab5_session \
    --attribute-definitions AttributeName=email,AttributeType=S \
    --key-schema AttributeName=email,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST

### Retrieve URL for lab report
```
aws lambda get-function-url-config --function-name Lab5_session --query "FunctionUrl" --output text
```

### Sample screenshots
![CLI screen capture](lab5-aws-cli.png)
![Website home page](lab5-aws-website.png)
