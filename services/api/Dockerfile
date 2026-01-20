FROM python:3.13-slim

# Do not write .pyc files and always flush stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (better Docker layer caching).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code.
COPY app ./app

EXPOSE 8080

# Run the API.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
