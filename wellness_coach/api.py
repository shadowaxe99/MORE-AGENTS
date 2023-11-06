```python
from flask import Flask, request, jsonify
from database import Database
from main import WellnessCoach

app = Flask(__name__)
db = Database()
coach = WellnessCoach()

@app.route('/api/goals', methods=['POST'])
def set_goals():
    data = request.get_json()
    user_id = data['user_id']
    goals = data['goals']
    coach.set_goals(user_id, goals)
    return jsonify({"message": "Goals set successfully"}), 200

@app.route('/api/habits', methods=['POST'])
def track_habits():
    data = request.get_json()
    user_id = data['user_id']
    habits = data['habits']
    coach.track_habits(user_id, habits)
    return jsonify({"message": "Habits tracked successfully"}), 200

@app.route('/api/workout', methods=['POST'])
def plan_workout():
    data = request.get_json()
    user_id = data['user_id']
    workout = data['workout']
    coach.plan_workout(user_id, workout)
    return jsonify({"message": "Workout planned successfully"}), 200

@app.route('/api/nutrition', methods=['POST'])
def give_nutrition_advice():
    data = request.get_json()
    user_id = data['user_id']
    nutrition = data['nutrition']
    coach.give_nutrition_advice(user_id, nutrition)
    return jsonify({"message": "Nutrition advice given successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```