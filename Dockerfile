# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt from cache if available
RUN  pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run a command to start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]