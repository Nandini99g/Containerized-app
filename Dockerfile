# Lightweight base image
FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy dependencies
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Switch to non-root user
USER appuser

# Document container port (actual value comes from ENV)
EXPOSE 5000

# Run application
CMD ["python", "main.py"]
