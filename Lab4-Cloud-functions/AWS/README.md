# AWS												
1.	Review package elements (sample code provided).
2.	Deploy the function.
3.	Validate execution.
*Note:* The function needs to remain available until the lab is graded.
### Review code
For AWS code additionally includes IAM code.
### Create the IAM Role
```
aws iam create-role \
    --role-name LambdaBasicExecutionRole \
    --assume-role-policy-document file://policy.json
ROLE_ARN=` aws iam get-role --role-name LambdaBasicExecutionRole --query "Role.Arn" --output text`
```
### Attach the Basic Execution Policy
```
aws iam attach-role-policy \
    --role-name LambdaBasicExecutionRole \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```
### Package code
```
zip function.zip return_uuid.py
```
### Deploy code
```
aws lambda create-function \
    --function-name return_uuid \
    --runtime python3.13 \
    --role $ROLE_ARN \
    --handler return_uuid.lambda_handler \
    --zip-file fileb://function.zip
```
### Configure URL for public access
```
aws lambda create-function-url-config \
    --function-name return_uuid \
    --auth-type NONE \
    --cors '{ "AllowOrigins": ["*"], "AllowMethods": ["GET", "POST"] }'

aws lambda add-permission \
    --function-name return_uuid \
    --action lambda:InvokeFunctionUrl \
    --principal "*" \
    --function-url-auth-type NONE \
    --statement-id FunctionURLPublicAccess
```
### Retrieve URL for lab report
```
aws lambda get-function-url-config --function-name return_uuid --query "FunctionUrl" --output text
```
### Sample screenshots for lab report
![CLI screen capture](lab4-AWS-cli.png)
![Website home page](lab4-AWS-website.png)
