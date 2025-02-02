import boto3
from botocore.exceptions import ClientError

def create_dynamodb_tables():
    # Initialize DynamoDB resource pointing to local instance
    dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url='http://host.docker.internal:8000',  # Use 'localhost' if running outside WSL
        aws_access_key_id='fakeMyKeyId',  # Dummy credentials for local DynamoDB
        aws_secret_access_key='fakeSecretAccessKey',
        region_name='us-east-1'
    )

    tables = [
        {
            'TableName': 'Table1',
            'KeySchema': [{'AttributeName': 'id', 'KeyType': 'HASH'}],
            'AttributeDefinitions': [{'AttributeName': 'id', 'AttributeType': 'S'}],
            'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        },
        {
            'TableName': 'Table2',
            'KeySchema': [{'AttributeName': 'id', 'KeyType': 'HASH'}],
            'AttributeDefinitions': [{'AttributeName': 'id', 'AttributeType': 'S'}],
            'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        }
    ]

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
