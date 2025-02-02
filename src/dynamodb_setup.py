import json
import boto3
import os

# Connect to DynamoDB (local instance)
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://host.docker.internal:8000',  # Use 'localhost' if running outside WSL
    aws_access_key_id='fakeMyKeyId',  # Dummy credentials for local DynamoDB
    aws_secret_access_key='fakeSecretAccessKey',
    region_name='us-east-1'
)

def load_json(filename):
    """Load JSON data from a file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def create_tables():
    """Create DynamoDB tables from JSON file."""
    tables = load_json("create_table.json")

    for table in tables:
        try:
            response = dynamodb.create_table(**table)
            print(f"Creating table: {table['TableName']} - {response.table_status}")
        except boto3.client("dynamodb").exceptions.ResourceInUseException:
            print(f"Table {table['TableName']} already exists.")

# Function to load the condition expressions from the JSON file
def load_condition_expressions():
    with open('condition_expression.json', 'r') as file:
        return json.load(file)

# Function to load the mock data for a given table
def load_mock_data(table_name):
    mock_data_folder = 'mock_data'
    file_path = os.path.join(mock_data_folder, f'{table_name}.json')
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Function to insert items into DynamoDB based on the condition expressions
def insert_items():
    # Load condition expressions
    condition_expressions = load_condition_expressions()
    
    for table_info in condition_expressions:
        table_name = table_info['TableName']
        table = dynamodb.Table(table_name)
        
        # Load the mock data for the current table
        mock_data = load_mock_data(table_name)
        
        # Insert each item with the condition expression
        for item in mock_data:
            print(f"Inserting item into {table_name}: {item}")
            try:
                response = table.put_item(
                    Item=item
                )
                print(f"Item inserted into {table_name} with response: {response}")
            except Exception as e:
                print(f"Error inserting item into {table_name}: {e}\n")


if __name__ == "__main__":
    create_tables()
    insert_items()
