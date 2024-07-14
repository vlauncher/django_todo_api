# Use the official Python image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /code/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the Django project
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]