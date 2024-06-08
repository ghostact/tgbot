# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Command to run the application
CMD ["python", "airdopmuseumbot.py"]
