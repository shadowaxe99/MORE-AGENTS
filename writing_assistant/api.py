from flask import Flask, request, jsonify
from main import WritingAssistant

app = Flask(__name__)
assistant = WritingAssistant()

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data.get('text', '')
    result = assistant.analyze(text)
    return jsonify(result)

@app.route('/correct', methods=['POST'])
def correct_text():
    data = request.get_json()
    text = data.get('text', '')
    result = assistant.correct(text)
    return jsonify(result)

@app.route('/advise', methods=['POST'])
def advise_structure():
    data = request.get_json()
    text = data.get('text', '')
    result = assistant.advise(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
```
