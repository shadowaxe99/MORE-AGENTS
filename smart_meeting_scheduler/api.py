```python
from flask import Flask, request, jsonify
from database import get_availability, schedule_meeting

app = Flask(__name__)

@app.route('/check_availability', methods=['POST'])
def check_availability():
    data = request.get_json()
    user_id = data.get('user_id')
    date = data.get('date')
    availability = get_availability(user_id, date)
    return jsonify(availability), 200

@app.route('/schedule_meeting', methods=['POST'])
def schedule():
    data = request.get_json()
    user_id = data.get('user_id')
    date = data.get('date')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    meeting_id = schedule_meeting(user_id, date, start_time, end_time)
    return jsonify({'meeting_id': meeting_id}), 200

if __name__ == '__main__':
    app.run(debug=True)
```