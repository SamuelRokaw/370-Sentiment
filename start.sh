#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# --- NLTK Setup ---
# Define the directory where NLTK data will be stored.
# This path is relative to the WORKDIR defined in your Dockerfile (usually /app).
NLTK_RESOURCES_DIR="/app/nltk_data"

# Export NLTK_DATA environment variable. NLTK will use this path to find its data.
# This ensures that NLTK looks for data in the directory we specify.
export NLTK_DATA=$NLTK_RESOURCES_DIR

# Create the NLTK data directory if it doesn't exist.
mkdir -p $NLTK_RESOURCES_DIR
echo "NLTK_DATA directory set to: $NLTK_DATA"

# Check if NLTK is installed (it should be, via requirements.txt in the Dockerfile build stage).
# This is a safety check.
if python -c "import nltk" &> /dev/null; then
    echo "NLTK module found. Proceeding to download resources..."
    # Download the 'punkt' tokenizer models.
    # The '-d' flag directs the download to our specified NLTK_RESOURCES_DIR.
    echo "Downloading NLTK 'punkt' resource..."
    python -m nltk.downloader -d $NLTK_RESOURCES_DIR punkt

    # Download the 'stopwords' corpus.
    echo "Downloading NLTK 'stopwords' resource..."
    python -m nltk.downloader -d $NLTK_RESOURCES_DIR stopwords

    # Add other NLTK resources you might need here, for example:
    # echo "Downloading NLTK 'wordnet' resource..."
    # python -m nltk.downloader -d $NLTK_RESOURCES_DIR wordnet
    # echo "Downloading NLTK 'averaged_perceptron_tagger' resource..."
    # python -m nltk.downloader -d $NLTK_RESOURCES_DIR averaged_perceptron_tagger

    echo "NLTK resources downloaded successfully to $NLTK_RESOURCES_DIR."

    # Optional: Verify NLTK data path in your Python application if you encounter issues.
    # You can add this to the beginning of your app.py:
    # import nltk
    # nltk.data.path.append("/app/nltk_data") # Or the value of NLTK_RESOURCES_DIR
    # print(f"NLTK data paths: {nltk.data.path}")

else
    echo "WARNING: NLTK Python module not found."
    echo "Please ensure 'nltk' is listed in your requirements.txt file."
    echo "Skipping NLTK resource download."
fi
# --- End NLTK Setup ---

# --- Start Application ---
# Start the Gunicorn server.
# Render injects the PORT environment variable, which Gunicorn will use.
# WORKERS is an environment variable you can set in Render's dashboard or defaults to 3 here.
# Replace 'app:app' with 'your_main_file:your_flask_instance_variable' if different.
echo "Starting Gunicorn web server on port ${PORT} with ${WORKERS:-3} workers..."
exec gunicorn --bind 0.0.0.0:${PORT} \
             --workers ${WORKERS:-3} \
             --log-level info \
             app:app
