FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY src .

# Install the necessary dependencies
RUN pip install boto3

# Command to run the Python script
CMD ["python", "dyanamodb_setup.py"]