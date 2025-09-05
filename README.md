# Customer Management API

A serverless CRUD API for customer management built with AWS SAM, Lambda, and DynamoDB.

## Architecture

- **API Gateway**: REST API endpoints
- **AWS Lambda**: Serverless compute for business logic
- **DynamoDB**: NoSQL database for customer data
- **Python 3.12**: Runtime environment

## Customer Data Model

Each customer record contains:
- `customer_id`: Unique identifier (UUID)
- `first_name`: Customer's first name
- `last_name`: Customer's last name
- `date_of_birth`: Date of birth (YYYY-MM-DD)
- `address`: Street address
- `city`: City
- `state`: State/Province
- `postal_code`: ZIP/Postal code
- `phone_number`: Phone number
- `email_address`: Email address
- `customer_acquisition_date`: When customer was acquired (ISO datetime)
- `preferred_communication_channels`: Array of ["email", "text", "phone"]
- `is_loyalty_member`: "y" or "n"
- `customer_status`: "active", "inactive", or "canceled"
- `lifetime_value`: Customer's lifetime value (float)

## API Endpoints

- `GET /customers` - List all customers
- `POST /customers` - Create a new customer
- `GET /customers/{customer_id}` - Get a specific customer
- `PUT /customers/{customer_id}` - Update a customer
- `DELETE /customers/{customer_id}` - Delete a customer
- `POST /seed` - Seed database with 10 sample customers

## Prerequisites

- AWS CLI configured with appropriate permissions
- AWS SAM CLI installed
- Python 3.12

## Deployment

1. **Build the application:**
   ```bash
   ./deploy.sh
   ```
   Or manually:
   ```bash
   sam build
   sam deploy --guided
   ```

2. **Seed the database:**
   After deployment, call the seed endpoint:
   ```bash
   curl -X POST https://your-api-gateway-url.execute-api.region.amazonaws.com/Prod/seed
   ```

## Testing with Swagger UI

1. Open `swagger-ui.html` in your browser
2. Update the API URL in the HTML file to match your deployed API Gateway URL
3. Use the interactive interface to test all endpoints

## Example API Calls

### Create a Customer
```bash
curl -X POST https://your-api-url/Prod/customers \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email_address": "john.doe@example.com",
    "phone_number": "555-0123",
    "preferred_communication_channels": ["email", "phone"],
    "is_loyalty_member": "y",
    "lifetime_value": 1500.00
  }'
```

### Get All Customers
```bash
curl https://your-api-url/Prod/customers
```

### Get Specific Customer
```bash
curl https://your-api-url/Prod/customers/{customer_id}
```

### Update Customer
```bash
curl -X PUT https://your-api-url/Prod/customers/{customer_id} \
  -H "Content-Type: application/json" \
  -d '{
    "lifetime_value": 2000.00,
    "customer_status": "active"
  }'
```

### Delete Customer
```bash
curl -X DELETE https://your-api-url/Prod/customers/{customer_id}
```

## Project Structure

```
customer-management-api/
├── template.yaml              # SAM template
├── src/                      # Lambda function code
│   ├── models.py            # Customer model and utilities
│   ├── db_utils.py          # DynamoDB operations
│   ├── create_customer.py   # Create customer handler
│   ├── get_customer.py      # Get customer handler
│   ├── list_customers.py    # List customers handler
│   ├── update_customer.py   # Update customer handler
│   ├── delete_customer.py   # Delete customer handler
│   ├── seed_data.py         # Seed database handler
│   └── requirements.txt     # Python dependencies
├── swagger.yaml             # OpenAPI specification
├── swagger-ui.html          # Swagger UI interface
├── deploy.sh               # Deployment script
├── teardown.sh             # Cleanup script
└── README.md               # This file
```

## Cleanup

To delete all AWS resources:
```bash
./teardown.sh
```

## Development

### Local Testing
```bash
sam local start-api
```

### View Logs
```bash
sam logs -n CreateCustomerFunction --stack-name customer-management-api --tail
```

## Security Considerations

- API Gateway has CORS enabled for web browser access
- DynamoDB uses IAM roles for access control
- No authentication implemented (add API Gateway authorizers for production)

## Cost Optimization

- DynamoDB uses on-demand billing
- Lambda functions use minimal memory allocation
- API Gateway charges per request

## Monitoring

The deployment includes basic CloudWatch logging. Consider adding:
- CloudWatch alarms for error rates
- X-Ray tracing for performance monitoring
- Custom metrics for business KPIs
