from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import nbformat
from nbconvert import PythonExporter
import importlib.util

# Load and execute the notebook
sys.path.append(r"C:\Users\YASH\myenv\SentimentAnalysis")

# Import the notebook as a module
import importnb
with importnb.Notebook():
    import TwitterSentimentAnalysis
    from TwitterSentimentAnalysis import complete_sentiment_analysis

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    result = complete_sentiment_analysis(data['text'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)