```python
import os
from flask import Flask, request, jsonify
from database import Database
from api import CalendarAPI

app = Flask(__name__)
db = Database()
api = CalendarAPI()

@app.route('/schedule', methods=['POST'])
def schedule_meeting():
    data = request.get_json()
    user_id = data.get('user_id')
    meeting_details = data.get('meeting_details')

    # Check user availability
    user = db.get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    availability = api.check_availability(user, meeting_details)
    if not availability:
        return jsonify({'error': 'User is not available at the requested time'}), 400

    # Schedule meeting
    meeting_id = db.create_meeting(user_id, meeting_details)
    api.schedule_meeting(user, meeting_id, meeting_details)

    return jsonify({'message': 'Meeting scheduled successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
```