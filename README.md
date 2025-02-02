# E-commerce DynamoDB Project

This project represents the last step of a **NoSQL data modeling** project for an e-commerce store. The primary focus of this phase is to insert predefined data into a local DynamoDB instance using Python scripts. This setup is part of a larger effort to design and implement a robust database structure capable of handling various e-commerce operations, including product reviews, customer information, and order details.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [DynamoDB Setup](#dynamodb-setup)
- [Contributing](#contributing)
- [License](#license)


## Overview of `dynamodb_setup.py` Script

The `dynamodb_setup.py` script is designed to insert data into a local DynamoDB instance, ensuring that no duplicates are created in the process. The script performs the following actions:

- **Reads data** from predefined JSON files.
- **Inserts data** into DynamoDB tables using **Condition Expressions** to enforce constraints (such as ensuring that an item with the same ID does not already exist).
- **Logs errors and success messages**, providing feedback on whether each insertion was successful or if it failed due to conditions like existing records.

This script is the final step in the project, where the model is populated with data to test the structure and simulate realistic operations.

## Project Structure

The project has the following folder structure:

```
ecommerce-dynamodb/
├── README.md
├── requirements.txt
├── src/
│   ├── mock_data/
│   │   ├── avaliacao.json
│   │   ├── carrinho.json
│   │   ├── cliente.json
│   │   ├── pedido.json
│   │   ├── produto.json
│   ├── condition_expression.json
│   ├── create_table.json
│   ├── dynamodb_setup.py
```

## Installation

To run this project, you need to set up the following:

### Prerequisites

This project uses a **Docker container** to run the Python script, eliminating the need for local environment setup.

## Usage

I encourage you to use a dev container to make the dependencies 
process easier. Just have Docker Desktop installed, the Dev Containers
extension installed in your VSCode. Then cd into the project folder and navegate to the "Reopen in Container" option in your VSCode.

Once the container is built, you can run the script with the following 
command:
```bash
python src/dynamodb_setup.py
```

## DynamoDB Setup

The script was created with a local instance of DynamoDB in mind.

You can easily run a local DynamoDB instance by downloading and 
installing [NoSQL Workbench](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html), then toggling the DDB local 
option in the bottom left corner.

## Script Functionalities

The `dynamodb_setup.py` script is responsible for interacting with a local DynamoDB instance to populate predefined tables with sample data. Below is an overview of the key functionalities of the script:

### 1. **Data Loading from JSON**

The script reads data from predefined JSON files, each containing the records that need to be inserted into the DynamoDB tables. Each JSON object represents a record for a specific table, ensuring that the right data is populated into the appropriate fields.

### 2. **Insertion with Conditional Expressions**

The script performs data insertion into the DynamoDB tables using the `PutItem` operation. To avoid inserting duplicate records, it employs **Condition Expressions**. Specifically, it checks whether a record with a specific ID already exists before attempting to insert a new one. If the condition fails (e.g., if the item already exists), an error is raised.

### 3. **Logging of Results**

For every data insertion attempt, the script logs the result:

- **Success:** When the item is inserted successfully, a confirmation message is logged.
- **Failure:** If there’s an error (such as a conditional check failure), the error message is captured and displayed. This helps in identifying issues like duplicate records or missing data.

### 4. **Error Handling**

The script includes error handling to catch common issues that may arise during the data insertion process, such as:

- **Validation errors** when the condition expressions are not met.
- **Connection errors** if the script fails to connect to the local DynamoDB instance.

By catching these errors, the script ensures that the process doesn't stop unexpectedly and provides useful feedback for debugging.

### 5. **Data Insertion Feedback**

The script provides detailed feedback, indicating whether the insertion of each item was successful or if there was a failure due to condition checks or validation issues. This helps to track which records were successfully inserted and which need further attention.

### Example Output

```bash
Inserting item into table_name: {'id_produto': '12345', '_id': 'item_1', 'nota': 5, 'comentario': 'Great product!'}
Item inserted successfully into table_name
```

If a record fails:
```bash
Error inserting item into table_name: An error occurred(ConditionalCheckFailedException) when calling the PutItem operation: The conditional request failed
```


