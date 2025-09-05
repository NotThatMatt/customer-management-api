#!/bin/bash

echo "Building SAM application..."
sam build

if [ $? -ne 0 ]; then
    echo "Build failed!"
    exit 1
fi

echo "Deploying SAM application..."
sam deploy --guided

if [ $? -eq 0 ]; then
    echo "Deployment successful!"
    echo "To seed the database with sample data, call the /seed endpoint:"
    echo "curl -X POST https://your-api-gateway-url.execute-api.region.amazonaws.com/Prod/seed"
else
    echo "Deployment failed!"
    exit 1
fi
