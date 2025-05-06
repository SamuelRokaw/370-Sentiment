from flask import Flask, request, render_template
from Sentimentanal import analyze_sentiment  # Import the function from Sentimentanal.py
import os  # Import os to access environment variables

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    output = None
    user_input = ""
    if request.method == "POST":
        user_input = request.form["userInput"]
        # Call the sentiment analysis function
        output = analyze_sentiment(user_input)

    return render_template("form.html", output=output, user_input=user_input)  # returns the analysis result and user input so they can be displayed

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or default to 5000
    app.run(host="0.0.0.0", port=port)  # Listen on all interfaces
    