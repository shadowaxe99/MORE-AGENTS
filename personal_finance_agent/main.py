```python
import os
from flask import Flask, request, jsonify
from database import Database
from api import FinanceAPI

app = Flask(__name__)

# Initialize database and API
db = Database(os.getenv("DATABASE_URL"))
api = FinanceAPI(os.getenv("FINANCE_API_KEY"))

@app.route('/budget', methods=['POST'])
def create_budget():
    data = request.get_json()
    result = db.create_budget(data)
    return jsonify(result), 201

@app.route('/expense', methods=['POST'])
def track_expense():
    data = request.get_json()
    result = db.track_expense(data)
    return jsonify(result), 201

@app.route('/portfolio', methods=['GET'])
def optimize_portfolio():
    data = request.get_json()
    result = api.optimize_portfolio(data)
    return jsonify(result), 200

@app.route('/retirement', methods=['GET'])
def plan_retirement():
    data = request.get_json()
    result = api.plan_retirement(data)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
```