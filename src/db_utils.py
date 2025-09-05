import boto3
import os
from typing import Dict, Any, List, Optional
from models import Customer

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['CUSTOMERS_TABLE'])

# DynamoDB reserved keywords that need ExpressionAttributeNames
RESERVED_KEYWORDS = {'state', 'status', 'date', 'location', 'name', 'size', 'type'}

def create_customer(customer: Customer) -> Dict[str, Any]:
    table.put_item(Item=customer.to_dict())
    return customer.to_dict()

def get_customer(customer_id: str) -> Optional[Dict[str, Any]]:
    response = table.get_item(Key={'customer_id': customer_id})
    return response.get('Item')

def list_customers() -> List[Dict[str, Any]]:
    response = table.scan()
    return response.get('Items', [])

def update_customer(customer_id: str, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    update_expression = "SET "
    expression_values = {}
    expression_names = {}
    
    for key, value in updates.items():
        if key != 'customer_id':
            if key.lower() in RESERVED_KEYWORDS:
                attr_name = f"#{key}"
                expression_names[attr_name] = key
                update_expression += f"{attr_name} = :{key}, "
            else:
                update_expression += f"{key} = :{key}, "
            expression_values[f":{key}"] = value
    
    update_expression = update_expression.rstrip(', ')
    
    kwargs = {
        'Key': {'customer_id': customer_id},
        'UpdateExpression': update_expression,
        'ExpressionAttributeValues': expression_values,
        'ReturnValues': 'ALL_NEW'
    }
    
    if expression_names:
        kwargs['ExpressionAttributeNames'] = expression_names
    
    response = table.update_item(**kwargs)
    return response.get('Attributes')

def delete_customer(customer_id: str) -> bool:
    table.delete_item(Key={'customer_id': customer_id})
    return True
