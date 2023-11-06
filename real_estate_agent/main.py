```python
import os
from flask import Flask, request, jsonify
from database import Database
from api import RealEstateAPI

app = Flask(__name__)

# Initialize database connection
db = Database(os.getenv("DATABASE_URL"))

# Initialize API
api = RealEstateAPI(db)

@app.route('/search', methods=['POST'])
def search_property():
    data = request.get_json()
    result = api.search_property(data)
    return jsonify(result)

@app.route('/estimate', methods=['POST'])
def estimate_price():
    data = request.get_json()
    result = api.estimate_price(data)
    return jsonify(result)

@app.route('/process', methods=['POST'])
def process_paperwork():
    data = request.get_json()
    result = api.process_paperwork(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```