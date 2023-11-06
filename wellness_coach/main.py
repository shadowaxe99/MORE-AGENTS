```python
import os
from flask import Flask, request, jsonify
from database import Database
from api import HealthAPI

app = Flask(__name__)

# Initialize database
db = Database(os.getenv("DATABASE_URL"))

# Initialize API
api = HealthAPI(db)

@app.route('/goal', methods=['POST'])
def set_goal():
    data = request.get_json()
    return api.set_goal(data)

@app.route('/habit', methods=['POST'])
def track_habit():
    data = request.get_json()
    return api.track_habit(data)

@app.route('/workout', methods=['POST'])
def plan_workout():
    data = request.get_json()
    return api.plan_workout(data)

@app.route('/nutrition', methods=['POST'])
def give_nutrition_advice():
    data = request.get_json()
    return api.give_nutrition_advice(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```