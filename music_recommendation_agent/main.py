```python
import os
from flask import Flask, request, jsonify
from database import Database
from api import MusicAPI

app = Flask(__name__)
db = Database()
api = MusicAPI()

@app.route('/recommend', methods=['POST'])
def recommend_music():
    user_id = request.json.get('user_id')
    user_history = db.get_user_history(user_id)
    recommendations = api.get_recommendations(user_history)
    return jsonify(recommendations), 200

@app.route('/history', methods=['POST'])
def update_history():
    user_id = request.json.get('user_id')
    song_id = request.json.get('song_id')
    db.update_user_history(user_id, song_id)
    return jsonify({'message': 'History updated successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
```