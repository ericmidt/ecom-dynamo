import boto3
from botocore.exceptions import ClientError

def create_dynamodb_tables():
    # Initialize a session using Amazon DynamoDB
    session = boto3.Session(
        aws_access_key_id='your_access_key',
        aws_secret_access_key='your_secret_key',
        region_name='us-west-2'  # Change to your desired region
    )

    # Initialize DynamoDB resource
    dynamodb = session.resource('dynamodb')

    # Define the tables to create
    tables = [
        {
            'TableName': 'Table1',
            'KeySchema': [
                {'AttributeName': 'id', 'KeyType': 'HASH'}  # Partition key
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        },
        {
            'TableName': 'Table2',
            'KeySchema': [
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
    ]

    # Create the tables
    for table in tables:
        try:
            print(f"Creating table {table['TableName']}...")
            dynamodb.create_table(
                TableName=table['TableName'],
                KeySchema=table['KeySchema'],
                AttributeDefinitions=table['AttributeDefinitions'],
                ProvisionedThroughput=table['ProvisionedThroughput']
            )
            print(f"Table {table['TableName']} created successfully.")
        except ClientError as e:
            print(f"Error creating table {table['TableName']}: {e.response['Error']['Message']}")

if __name__ == "__main__":
    create_dynamodb_tables()