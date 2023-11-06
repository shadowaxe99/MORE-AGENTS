```python
import os
from flask import Flask, request, jsonify
from transformers import pipeline
from utils import preprocess_text

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    preprocessed_text = preprocess_text(text)

    sentiment_analysis = pipeline('sentiment-analysis')
    result = sentiment_analysis(preprocessed_text)[0]

    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```