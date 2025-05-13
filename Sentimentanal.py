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


def preprocess_text(text): # this adds not to the vectorizer so "not good" is detected as a negative review instead of a positive review, Version A
    # Tokenize the text
    tokens = word_tokenize(text)
    negation_words = {'not', "n't", 'no', 'never'}
    processed_tokens = []
    negate = False

    for token in tokens:
        if token in negation_words:
            negate = True
            processed_tokens.append(token)
        elif negate:
            processed_tokens.append(f'NOT_{token}')
            negate = False
        else:
            processed_tokens.append(token)

    return ' '.join(processed_tokens)
# def preprocess_text(text): #double negative version, Version B
#     # Tokenize the text
#     tokens = word_tokenize(text)
#     negation_words = {'not', "n't", 'no', 'never'}
#     processed_tokens = []
#     negate = False

#     for token in tokens:
#         if token in negation_words:
#             negate = not negate
#             processed_tokens.append(token)
#         elif negate:
#             processed_tokens.append(f'NOT_{token}')
#         else:
#             processed_tokens.append(token)

#     return ' '.join(processed_tokens)

# Gets current folder directory
current_folder = os.path.dirname(__file__)

model_path = os.path.join(current_folder, 'sentiment_model.pkl')
vectorizer_path = os.path.join(current_folder, 'vectorizer.pkl')

if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
else:
    #gets the path to the zip file in the current folder
    zip_file_path = os.path.join(current_folder, 'trainingandtest.zip')

    #unzip the Zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(current_folder)

    # Now you can read the CSV file
    #2 different files it could be trained off of from the zip file, the first one has 1.6 million samples but they are only negative and positive
    #the second one has 498 samples but it has negative, neutral, and positive 
    #option 1
    CSV_file_path = os.path.join(current_folder, 'training.1600000.processed.noemoticon.csv') #gets the path to the CSV file after unzipping
    #option 2
    # CSV_file_path = os.path.join(current_folder, 'testdata.manual.2009.06.14.csv') #gets the path to the CSV file after unzipping
    df = pd.read_csv(CSV_file_path, encoding='latin-1', header=None)

    #Preprocess the data
    df.columns = ['sentiment', 'id', 'date', 'query', 'user', 'text']
    df =df.drop(['id', 'date', 'query', 'user'], axis=1)
    df['sentiment'] = df['sentiment'].map({
        0: 'negative',
        2: 'neutral',
        4: 'positive'
    })
    # Train the model if not already saved
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['sentiment'], test_size=0.2, random_state=42)

    # Vectorize the text data
    vectorizer = CountVectorizer( tokenizer=word_tokenize, stop_words=stopwords.words('english'), preprocessor=preprocess_text)
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)

    # Train the model
    model = LogisticRegression(max_iter=1600000)
    model.fit(X_train, y_train)

    # Save the trained model and vectorizer
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

    # Test the model
    accuracy = model.score(X_test, y_test)
    print(f'Model accuracy: {accuracy}')

def analyze_sentiment(text):
    # Preprocess the input text
    text_vectorized = vectorizer.transform([text])

    # Predict the sentiment
    prediction = model.predict(text_vectorized)

    # Return the sentiment prediction
    return prediction[0]