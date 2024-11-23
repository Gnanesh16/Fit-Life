# Use a Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
