```python
import os
from flask import Flask, request, jsonify
from database import Database
from api import TutoringAPI

app = Flask(__name__)

# Initialize database connection
db = Database(os.getenv("DB_HOST"), os.getenv("DB_USER"), os.getenv("DB_PASS"), os.getenv("DB_NAME"))

# Initialize API
api = TutoringAPI(db)

@app.route('/tutoring/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    response = api.ask_question(data['user_id'], data['question'])
    return jsonify(response), 200

@app.route('/tutoring/track', methods=['POST'])
def track_progress():
    data = request.get_json()
    response = api.track_progress(data['user_id'], data['progress'])
    return jsonify(response), 200

@app.route('/tutoring/scaffold', methods=['POST'])
def scaffold_topic():
    data = request.get_json()
    response = api.scaffold_topic(data['user_id'], data['topic'])
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```