import json
from datetime import datetime
from typing import Dict, Any, Optional
from decimal import Decimal
import uuid

class Customer:
    def __init__(self, **kwargs):
        self.customer_id = kwargs.get('customer_id', str(uuid.uuid4()))
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.date_of_birth = kwargs.get('date_of_birth', '')
        self.address = kwargs.get('address', '')
        self.city = kwargs.get('city', '')
        self.state = kwargs.get('state', '')
        self.postal_code = kwargs.get('postal_code', '')
        self.phone_number = kwargs.get('phone_number', '')
        self.email_address = kwargs.get('email_address', '')
        self.customer_acquisition_date = kwargs.get('customer_acquisition_date', datetime.now().isoformat())
        self.preferred_communication_channels = kwargs.get('preferred_communication_channels', [])
        self.is_loyalty_member = kwargs.get('is_loyalty_member', 'n')
        self.customer_status = kwargs.get('customer_status', 'active')
        self.lifetime_value = Decimal(str(kwargs.get('lifetime_value', 0.0)))

    def to_dict(self) -> Dict[str, Any]:
        return {
            'customer_id': self.customer_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'postal_code': self.postal_code,
            'phone_number': self.phone_number,
            'email_address': self.email_address,
            'customer_acquisition_date': self.customer_acquisition_date,
            'preferred_communication_channels': self.preferred_communication_channels,
            'is_loyalty_member': self.is_loyalty_member,
            'customer_status': self.customer_status,
            'lifetime_value': self.lifetime_value
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Customer':
        return cls(**data)

def create_response(status_code: int, body: Any) -> Dict[str, Any]:
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        },
        'body': json.dumps(body, default=str)
    }
