# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port for Gunicorn
EXPOSE 8000

COPY ./start-server.sh .
RUN sed -i 's/\r$//g' start-server.sh
RUN chmod +x start-server.sh

EXPOSE 8080
STOPSIGNAL SIGTERM
