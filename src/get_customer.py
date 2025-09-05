from models import create_response
from db_utils import get_customer

def lambda_handler(event, context):
    try:
        customer_id = event['pathParameters']['customer_id']
        customer = get_customer(customer_id)
        
        if not customer:
            return create_response(404, {'error': 'Customer not found'})
        
        return create_response(200, customer)
    except Exception as e:
        return create_response(400, {'error': str(e)})
