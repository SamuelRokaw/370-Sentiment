# Stage 1: Use an official Python runtime as a parent image
# Using a specific version is good practice for reproducibility
FROM python:3.11-slim-buster AS base

# Set environment variables
# PYTHONUNBUFFERED ensures that Python output is sent straight to terminal without being first buffered
ENV PYTHONUNBUFFERED=1
# PORT will be set by Render. Gunicorn will use this. Default for local testing.
ENV PORT=5000
# Default number of Gunicorn workers. Can be overridden by Render environment variable 'WORKERS'.
ENV WORKERS=3
# Define the NLTK_DATA path. The start.sh script will also set/use this.
# Having it here makes it explicit and available during build if needed for other tools.
ENV NLTK_DATA=/app/nltk_data

# Set the working directory in the container
WORKDIR /app

# Install system dependencies that might be needed by some Python packages
# (e.g., psycopg2 for PostgreSQL often needs libpq-dev). Uncomment and modify if needed.
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     libpq-dev \
#  && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt ./

# Install Python dependencies from requirements.txt
# Ensure 'nltk' and 'gunicorn' are included in your requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the start script into the container and make it executable
# This assumes 'start.sh' is in the same directory as the Dockerfile when building
COPY start.sh ./start.sh
RUN chmod +x ./start.sh

# Copy the rest of your application code into the container
# This should be done after copying requirements.txt and start.sh to optimize Docker layer caching
COPY . .

# Expose the port the app runs on (Gunicorn will bind to this via $PORT set in start.sh or by Render)
EXPOSE ${PORT}

# Set the command to run when the container starts.
# This will execute our start.sh script, which handles NLTK downloads and then starts Gunicorn.
CMD ["./start.sh"]

# --- Notes for usage with Render ---
# 1. Ensure you have a `requirements.txt` file in the root of your project, including `flask`, `gunicorn`, and `nltk`.
#    Example `requirements.txt`:
#    flask
#    gunicorn
#    nltk
#    # ... other dependencies
#
# 2. Your main Flask application file should be in the root (e.g., `app.py`) and
#    the Flask instance named `app`. If not, update the Gunicorn command in `start.sh`.
#    (e.g., `main:application` if your file is `main.py` and instance is `application`).
#
# 3. Place this `Dockerfile` and the `start.sh` script (from the other document)
#    in the root of your repository.
#
# 4. In your Render service settings:
#    - Render should automatically detect and use this Dockerfile.
#    - The "Start Command" on Render can usually be left blank, as the Dockerfile's `CMD` will be used.
#    - You can set the `WORKERS` environment variable in Render's dashboard to control Gunicorn worker count.
#      The `start.sh` script will use this environment variable if set, otherwise it defaults to 3.
#
# 5. The `start.sh` script (referenced in the CMD line) downloads NLTK data every time the service starts.

