import json
from models import Customer, create_response
from db_utils import create_customer

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        customer = Customer(**body)
        result = create_customer(customer)
        return create_response(201, result)
    except Exception as e:
        return create_response(400, {'error': str(e)})
