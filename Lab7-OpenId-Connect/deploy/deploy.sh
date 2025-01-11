#!/bin/bash

if [ -z "$1" ]
  then
    echo "No DEPLOY_NAME argument supplied"
    exit 1
fi

DeployName=$1
DomainName=$DeployName.kengraf.com
S3BUCKET=$DeployName  # Needs to be globally unique

# Ideally the CloudFormation stacks would be combined into one.
# This appoach is allow students to alter steps as needed

STACK_NAME="$STACK_NAME-storage"
echo "Creating stack... $STACK_NAME"
aws cloudformation deploy --stack-name ${STACK_NAME} \
  --template-file file://${STACK_NAME}.json \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
      S3bucketName=${S3BUCKET} \
      DeployName=${DeployName} \
  --tags file://tags.json --output text
echo "Waiting on ${STACK_NAME} create completion..."
aws cloudformation wait stack-create-complete --stack-name ${STACK_NAME}
aws cloudformation describe-stacks --stack-name ${STACK_NAME} | jq .Stacks[0].Outputs

echo "Deploying backend components (apigatewayv2, lambda, dynamodb)"
STACK_NAME="$DeployName-backend"
aws cloudformation deploy --stack-name ${STACK_NAME} \
  --template-file file://${STACK_NAME}.json \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
      DeployName=${DeployName} \
  --tags file://tags.json --output text
echo "Waiting on ${STACK_NAME} create completion..."
aws cloudformation wait stack-create-complete --stack-name ${STACK_NAME}
aws cloudformation describe-stacks --stack-name ${STACK_NAME} | jq .Stacks[0].Outputs

echo "Deploy a CloudFront distribution"
CertificateArn="arn:aws:acm:us-east-2:788715698479:certificate/f5a199d0-7175-4992-bc7c-8ed2ad71541b"
DomainName="it718lab7.kengraf.com"
HostedZoneId="Z04154431JUEDZVN0IZ8F"
# Uncomment the next line if you do NOT have a Route53 hosted zone, previous settings will be ignored
#HostedZoneId=""  
STACK_NAME="$DeployName-distribution"
aws cloudformation deploy --stack-name ${STACK_NAME} \
  --template-file file://${STACK_NAME}.json \
  --parameter-overrides \
      HostedZoneId=${HostedZoneId} \
      DomainName=${DomainName} \
      CertificateArn=${CertificateArn} \
  --capabilities CAPABILITY_NAMED_IAM
aws cloudformation wait stack-create-complete --stack-name ${STACK_NAME}
aws cloudformation describe-stacks --stack-name ${STACK_NAME} | jq .Stacks[0].Outputs

echo "Packaging and uploading the lambda function"
cd lambda
zip function.zip verifyToken.py
aws s3 cp function.zip s3://${S3BUCKET}
cd ..

echo "Uploading website content"
cd website
aws s3 sync . s3://${S3BUCKET}
cd ..


aws cloudformation describe-stacks --stack-name ${STACK_NAME} --query "Stacks[*].{StackId: StackId, StackName: StackName}

# Update website config to reflect new resources
# VAR=$(aws cloudformation list-exports --query "Exports[?contains(Name,'IT718Lab7-ApiEndpoint')].[Value]" --output text)
# sed -ri "s^(invokeUrl: )('.*')^\1'${VAR}'^i" website/scripts/config.js

# echo "Waiting on ${STACK_NAME} create completion..."
# aws cloudformation wait stack-create-complete --stack-name ${STACK_NAME}
# aws cloudformation describe-stacks --stack-name ${STACK_NAME} | jq .Stacks[0].Outputs
