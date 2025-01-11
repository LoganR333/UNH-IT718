#!/bin/bash

STACK_NAME=$1

if [ -z "$1" ]
  then
    echo "No STACK_NAME argument supplied"
    exit 1
fi

S3BUCKET=$STACK_NAME-$(tr -dc a-f0-9 </dev/urandom | head -c 10)
sed -ri "s/bucket-random/${S3BUCKET}/" parameters.json
sed -ri "s/it718lab7-[0-9a-f]*/${S3BUCKET}/" parameters.json

echo "Creating stack... $STACK_NAME"

# Ideally the CloudFormation stacks would be combined into one.
# This appoach is allow students to alter steps as needed

STACK_NAME="$STACK_NAME-storage"
aws cloudformation create-stack --stack-name ${STACK_NAME} --template-body file://${STACK_NAME}.json --parameters file://parameters.json --tags file://tags.json --output text
echo "Waiting on ${STACK_NAME} create completion..."
aws cloudformation wait stack-create-complete --stack-name ${STACK_NAME}
aws cloudformation describe-stacks --stack-name ${STACK_NAME} | jq .Stacks[0].Outputs
exit

# Package and upload the lambda function
cd lambda
zip function.zip verifyToken.py
aws s3 cp function.zip s3://${S3BUCKET}/function.zip
cd ..


# upload website
cd website
aws s3 sync . s3://IT718Lab7
cd ../deploy
aws cloudformation create-stack --stack-name IT718Lab7-lambda --template-body file://lambdaStack.json --capabilities CAPABILITY_NAMED_IAM --parameters file://parameters.json --tags file://tags.json --output text

aws cloudformation describe-stacks --stack-name "IT718Lab7" --query "Stacks[*].{StackId: StackId, StackName: StackName}

# Update website config to reflect new resources
VAR=$(aws cloudformation list-exports --query "Exports[?contains(Name,'IT718Lab7-ApiEndpoint')].[Value]" --output text)
sed -ri "s^(invokeUrl: )('.*')^\1'${VAR}'^i" website/scripts/config.js

echo "Waiting on ${STACK_NAME} create completion..."
aws cloudformation wait stack-create-complete --stack-name ${STACK_NAME}
aws cloudformation describe-stacks --stack-name ${STACK_NAME} | jq .Stacks[0].Outputs
