from models import create_response
from db_utils import delete_customer

def lambda_handler(event, context):
    try:
        customer_id = event['pathParameters']['customer_id']
        delete_customer(customer_id)
        return create_response(204, {})
    except Exception as e:
        return create_response(400, {'error': str(e)})
