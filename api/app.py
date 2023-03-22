from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    # Get the text from the request body
    text = request.json.get('text', '')
    
    # Use TextBlob to analyze the sentiment of the text
    sentiment_score = TextBlob(text).sentiment.polarity
    
    # Determine the sentiment based on the sentiment score
    if sentiment_score > 0:
        sentiment = "positive"
    elif sentiment_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    # Return the sentiment as a JSON object
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)

