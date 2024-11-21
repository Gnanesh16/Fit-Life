# Use Python base image
FROM python:3.9-slim

# Set working directory
#WORKDIR /app

# Copy application files
COPY /fitlife-app.spec /usr/local/FitLifeapp

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
