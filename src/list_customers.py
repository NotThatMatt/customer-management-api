from models import create_response
from db_utils import list_customers

def lambda_handler(event, context):
    try:
        customers = list_customers()
        return create_response(200, {'customers': customers})
    except Exception as e:
        return create_response(400, {'error': str(e)})
