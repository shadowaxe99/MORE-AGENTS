```python
import os
from flask import Flask, request, jsonify
from database import Database
from api import CustomerServiceAPI

app = Flask(__name__)

# Initialize database connection
database = Database(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Initialize API
api = CustomerServiceAPI(database)

@app.route('/question', methods=['POST'])
def handle_question():
    data = request.get_json()
    response = api.handle_question(data)
    return jsonify(response)

@app.route('/sentiment_analysis', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    response = api.sentiment_analysis(data)
    return jsonify(response)

@app.route('/account_lookup', methods=['POST'])
def account_lookup():
    data = request.get_json()
    response = api.account_lookup(data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```