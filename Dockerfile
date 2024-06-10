# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Copy the service account key file
#COPY serviceAccountKey.json /app/serviceAccountKey.json

# Expose the port that the app runs on
EXPOSE 8080

# Set the environment variable for Google Application Credentials
ENV GOOGLE_APPLICATION_CREDENTIALS=/home/prajeshkollath/path/to/serviceAccountKey.json

# Run the application
CMD ["python", "app.py"]

