STACK_NAME="WebApp1-VPC"
echo "Creating stack... $STACK_NAME"
aws cloudformation deploy --stack-name ${STACK_NAME} \
  --template-file vpc-alb-app-db.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --output text
echo "Waiting on ${STACK_NAME} create completion..."
aws cloudformation describe-stacks --stack-name ${STACK_NAME} | jq .Stacks[0].Outputs

STACK_NAME="HealthCheckLab"
echo "Creating stack... $STACK_NAME"
aws cloudformation deploy --stack-name ${STACK_NAME} \
  --template-file staticwebapp.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --output text
echo "Waiting on ${STACK_NAME} create completion..."
aws cloudformation describe-stacks --stack-name ${STACK_NAME} | jq .Stacks[0].Outputs
