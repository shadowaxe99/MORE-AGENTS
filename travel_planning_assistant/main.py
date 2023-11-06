```python
import os
from flask import Flask, request, jsonify
from database import Database
from api import TravelAPI

app = Flask(__name__)

# Initialize database and API
db = Database(os.getenv("DATABASE_URL"))
api = TravelAPI(os.getenv("TRAVEL_API_KEY"))

@app.route('/plan', methods=['POST'])
def plan_trip():
    data = request.get_json()
    destination = data.get('destination')
    dates = data.get('dates')

    # Validate input
    if not destination or not dates:
        return jsonify({'error': 'Invalid input'}), 400

    # Get recommendations and build schedule
    recommendations = api.get_recommendations(destination)
    schedule = api.build_schedule(dates, recommendations)

    # Save to database
    db.save_plan(destination, dates, schedule)

    return jsonify(schedule), 200

if __name__ == '__main__':
    app.run(debug=True)
```