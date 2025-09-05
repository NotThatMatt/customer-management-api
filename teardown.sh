#!/bin/bash

STACK_NAME="customer-management-api"

echo "Deleting CloudFormation stack: $STACK_NAME"
aws cloudformation delete-stack --stack-name $STACK_NAME

echo "Waiting for stack deletion to complete..."
aws cloudformation wait stack-delete-complete --stack-name $STACK_NAME

if [ $? -eq 0 ]; then
    echo "Stack deleted successfully!"
else
    echo "Stack deletion failed or timed out. Check AWS Console for details."
fi

echo "Cleaning up local build artifacts..."
rm -rf .aws-sam/
