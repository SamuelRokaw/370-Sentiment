#Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import zipfile
import os #needed to handle file paths
import joblib  # Import joblib for saving/loading models

# Gets current folder directory
current_folder = os.path.dirname(__file__)

model_path = os.path.join(current_folder, 'sentiment_model.pkl')
vectorizer_path = os.path.join(current_folder, 'vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)


def analyze_sentiment(text):
    # Preprocess the input text
    text_vectorized = vectorizer.transform([text])

    # Predict the sentiment
    prediction = model.predict(text_vectorized)

    # Return the sentiment prediction
    return prediction[0]