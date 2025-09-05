import json
from decimal import Decimal
from models import create_response
from db_utils import update_customer

def lambda_handler(event, context):
    try:
        customer_id = event['pathParameters']['customer_id']
        updates = json.loads(event['body'])
        
        # Convert float values to Decimal for DynamoDB
        for key, value in updates.items():
            if isinstance(value, float):
                updates[key] = Decimal(str(value))
        
        result = update_customer(customer_id, updates)
        if not result:
            return create_response(404, {'error': 'Customer not found'})
        
        return create_response(200, result)
    except Exception as e:
        return create_response(400, {'error': str(e)})
