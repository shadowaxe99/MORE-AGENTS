```python
from flask import Flask, request, jsonify
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/budget', methods=['POST'])
def create_budget():
    data = request.get_json()
    result = db.create_budget(data)
    return jsonify(result), 201

@app.route('/budget/<int:id>', methods=['GET'])
def get_budget(id):
    result = db.get_budget(id)
    return jsonify(result), 200

@app.route('/expense', methods=['POST'])
def track_expense():
    data = request.get_json()
    result = db.track_expense(data)
    return jsonify(result), 201

@app.route('/expense/<int:id>', methods=['GET'])
def get_expense(id):
    result = db.get_expense(id)
    return jsonify(result), 200

@app.route('/portfolio', methods=['POST'])
def optimize_portfolio():
    data = request.get_json()
    result = db.optimize_portfolio(data)
    return jsonify(result), 201

@app.route('/portfolio/<int:id>', methods=['GET'])
def get_portfolio(id):
    result = db.get_portfolio(id)
    return jsonify(result), 200

@app.route('/retirement', methods=['POST'])
def plan_retirement():
    data = request.get_json()
    result = db.plan_retirement(data)
    return jsonify(result), 201

@app.route('/retirement/<int:id>', methods=['GET'])
def get_retirement_plan(id):
    result = db.get_retirement_plan(id)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
```