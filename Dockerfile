# Use an official lightweight Python image.
FROM python:3.9-slim

# Install system dependencies: nginx and supervisor.
RUN apt-get update && apt-get install -y nginx supervisor && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app.
WORKDIR /app

# Copy the project files to the container.
COPY . /app

# Upgrade pip and install Python dependencies.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy your custom Nginx configuration file.
# This will override the default Nginx site configuration.
COPY nginx.conf /etc/nginx/sites-available/default

# Copy the Supervisor configuration file.
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose port 80 for Nginx.
EXPOSE 80

# Start Supervisor to run both Uvicorn and Nginx.
CMD ["/usr/bin/supervisord", "-n"]
