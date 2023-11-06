```python
from flask import Flask, request, jsonify
from database import get_tutoring_data, update_tutoring_data
from main import process_tutoring_request

app = Flask(__name__)

@app.route('/api/tutoring', methods=['GET'])
def get_tutoring():
    user_id = request.args.get('user_id')
    data = get_tutoring_data(user_id)
    return jsonify(data)

@app.route('/api/tutoring', methods=['POST'])
def post_tutoring():
    data = request.get_json()
    user_id = data['user_id']
    topic = data['topic']
    question = data['question']
    response = process_tutoring_request(user_id, topic, question)
    update_tutoring_data(user_id, topic, question, response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```