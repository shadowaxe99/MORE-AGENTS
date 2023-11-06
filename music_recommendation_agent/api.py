```python
from flask import Flask, request, jsonify
from database import get_db_connection
from main import recommend_music

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_id = data.get('user_id')
    db = get_db_connection()
    recommendations = recommend_music(user_id, db)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
```