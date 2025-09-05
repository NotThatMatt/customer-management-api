from models import Customer, create_response
from db_utils import create_customer

def lambda_handler(event, context):
    try:
        sample_customers = [
            {
                "first_name": "John", "last_name": "Doe", "date_of_birth": "1985-03-15",
                "address": "123 Main St", "city": "New York", "state": "NY", "postal_code": "10001",
                "phone_number": "555-0101", "email_address": "john.doe@email.com",
                "preferred_communication_channels": ["email", "phone"], "is_loyalty_member": "y",
                "customer_status": "active", "lifetime_value": 1250.50
            },
            {
                "first_name": "Jane", "last_name": "Smith", "date_of_birth": "1990-07-22",
                "address": "456 Oak Ave", "city": "Los Angeles", "state": "CA", "postal_code": "90210",
                "phone_number": "555-0102", "email_address": "jane.smith@email.com",
                "preferred_communication_channels": ["text", "email"], "is_loyalty_member": "n",
                "customer_status": "active", "lifetime_value": 875.25
            },
            {
                "first_name": "Bob", "last_name": "Johnson", "date_of_birth": "1978-11-08",
                "address": "789 Pine Rd", "city": "Chicago", "state": "IL", "postal_code": "60601",
                "phone_number": "555-0103", "email_address": "bob.johnson@email.com",
                "preferred_communication_channels": ["phone"], "is_loyalty_member": "y",
                "customer_status": "inactive", "lifetime_value": 2100.75
            },
            {
                "first_name": "Alice", "last_name": "Brown", "date_of_birth": "1992-05-12",
                "address": "321 Elm St", "city": "Houston", "state": "TX", "postal_code": "77001",
                "phone_number": "555-0104", "email_address": "alice.brown@email.com",
                "preferred_communication_channels": ["email"], "is_loyalty_member": "y",
                "customer_status": "active", "lifetime_value": 1650.00
            },
            {
                "first_name": "Charlie", "last_name": "Wilson", "date_of_birth": "1988-09-30",
                "address": "654 Maple Dr", "city": "Phoenix", "state": "AZ", "postal_code": "85001",
                "phone_number": "555-0105", "email_address": "charlie.wilson@email.com",
                "preferred_communication_channels": ["text"], "is_loyalty_member": "n",
                "customer_status": "active", "lifetime_value": 950.30
            },
            {
                "first_name": "Diana", "last_name": "Davis", "date_of_birth": "1995-01-18",
                "address": "987 Cedar Ln", "city": "Philadelphia", "state": "PA", "postal_code": "19101",
                "phone_number": "555-0106", "email_address": "diana.davis@email.com",
                "preferred_communication_channels": ["email", "text"], "is_loyalty_member": "y",
                "customer_status": "active", "lifetime_value": 1425.80
            },
            {
                "first_name": "Frank", "last_name": "Miller", "date_of_birth": "1982-12-03",
                "address": "147 Birch St", "city": "San Antonio", "state": "TX", "postal_code": "78201",
                "phone_number": "555-0107", "email_address": "frank.miller@email.com",
                "preferred_communication_channels": ["phone", "email"], "is_loyalty_member": "n",
                "customer_status": "canceled", "lifetime_value": 750.00
            },
            {
                "first_name": "Grace", "last_name": "Garcia", "date_of_birth": "1987-06-25",
                "address": "258 Spruce Ave", "city": "San Diego", "state": "CA", "postal_code": "92101",
                "phone_number": "555-0108", "email_address": "grace.garcia@email.com",
                "preferred_communication_channels": ["text", "phone"], "is_loyalty_member": "y",
                "customer_status": "active", "lifetime_value": 1875.45
            },
            {
                "first_name": "Henry", "last_name": "Martinez", "date_of_birth": "1993-04-14",
                "address": "369 Willow Rd", "city": "Dallas", "state": "TX", "postal_code": "75201",
                "phone_number": "555-0109", "email_address": "henry.martinez@email.com",
                "preferred_communication_channels": ["email"], "is_loyalty_member": "n",
                "customer_status": "active", "lifetime_value": 1125.60
            },
            {
                "first_name": "Ivy", "last_name": "Anderson", "date_of_birth": "1991-08-07",
                "address": "741 Poplar St", "city": "San Jose", "state": "CA", "postal_code": "95101",
                "phone_number": "555-0110", "email_address": "ivy.anderson@email.com",
                "preferred_communication_channels": ["phone", "text", "email"], "is_loyalty_member": "y",
                "customer_status": "active", "lifetime_value": 2250.90
            }
        ]
        
        created_customers = []
        for customer_data in sample_customers:
            customer = Customer(**customer_data)
            result = create_customer(customer)
            created_customers.append(result)
        
        return create_response(201, {
            'message': f'Successfully seeded {len(created_customers)} customers',
            'customers': created_customers
        })
    except Exception as e:
        return create_response(400, {'error': str(e)})
