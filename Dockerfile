# Use an official Python runtime as a base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files (Python script, configs, etc.)
# COPY ./data /app/data
COPY ./lib /app/lib
COPY ./.env /app/.env

# Copy the Python script
COPY ./main.py /app/main.py

# Command to run your Python script
CMD ["python", "-u", "main.py"]