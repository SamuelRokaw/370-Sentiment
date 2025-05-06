from flask import Flask, request, render_template
from Sentimentanal import analyze_sentiment  # Import the function from Sentimentanal.py

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    output = None
    user_input = ""
    if request.method == "POST":

        user_input = request.form["userInput"]
        
        # Call the sentiment analysis function
        output = analyze_sentiment(user_input)
    
    return render_template("form.html", output=output, user_input=user_input) # returns the anylsis result and user input so they can be displayed

if __name__ == "__main__":
    app.run()
