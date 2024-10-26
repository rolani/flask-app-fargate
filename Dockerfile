# Use the official Python image as the base image
FROM python:3.12-slim

RUN apt-get update -y 

# Set the working directory in the container
WORKDIR /app

RUN pip install flask

# Copy the application code
COPY app.py .

# Expose port 80 for Flask
EXPOSE 80

# Define the command to run the Flask app
CMD ["python", "app.py"]