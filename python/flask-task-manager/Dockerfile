# Start with Python 3.10 Alpine for compatibility with dependencies
FROM python:3.10-alpine

# Set working directory
WORKDIR /app

# Copy requirements first (for better Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt


# Copy application files
COPY app.py .
COPY templates/ ./templates/

# Copy tasks.json (creates empty file if doesn't exist)
COPY tasks.json* ./

# # Expose port 5000
# EXPOSE 5000

# # Set environment variables for Docker
# ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
CMD ["python", "app.py"]