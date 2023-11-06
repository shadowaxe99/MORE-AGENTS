```python
import flask
from flask import request, jsonify
import database
import api

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Writing Assistant</h1><p>This site is a prototype API for a writing assistant.</p>"

@app.route('/api/v1/resources/analyze', methods=['POST'])
def analyze_text():
    if 'text' in request.args:
        text = str(request.args['text'])
    else:
        return "Error: No text field provided. Please specify a text."

    # Connect to the database
    db = database.connect_db()

    # Analyze the text
    result = api.analyze_text(db, text)

    # Return the result
    return jsonify(result)

@app.route('/api/v1/resources/correct', methods=['POST'])
def correct_text():
    if 'text' in request.args:
        text = str(request.args['text'])
    else:
        return "Error: No text field provided. Please specify a text."

    # Connect to the database
    db = database.connect_db()

    # Correct the text
    result = api.correct_text(db, text)

    # Return the result
    return jsonify(result)

@app.route('/api/v1/resources/advice', methods=['POST'])
def give_advice():
    if 'text' in request.args:
        text = str(request.args['text'])
    else:
        return "Error: No text field provided. Please specify a text."

    # Connect to the database
    db = database.connect_db()

    # Give advice on the text
    result = api.give_advice(db, text)

    # Return the result
    return jsonify(result)

app.run()
```