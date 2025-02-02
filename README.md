# My Python DynamoDB Project

This project is designed to create and manage tables in a DynamoDB instance running in a Docker container. It utilizes Python and the AWS SDK (boto3) to interact with DynamoDB.

## Project Structure

```
my-python-dynamodb-project
├── .devcontainer
│   ├── devcontainer.json
│   └── Dockerfile
├── src
│   └── create_tables.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   Clone this repository to your local machine using:
   ```
   git clone <repository-url>
   ```

2. **Open in Development Container**
   Open the project in a development container using your preferred IDE that supports dev containers.

3. **Install Dependencies**
   The required Python packages are listed in `requirements.txt`. They will be installed automatically when the container is built.

4. **Run the Script**
   To create the DynamoDB tables, run the following command inside the container:
   ```
   python src/create_tables.py
   ```

## Usage

The `create_tables.py` script connects to the DynamoDB instance and creates the specified tables. Make sure to configure your AWS credentials and region as needed.

## Additional Information

For more details on how to use DynamoDB with Python, refer to the [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).