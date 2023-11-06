```python
from flask import Flask, request, jsonify
from database import get_property, estimate_price, automate_paperwork

app = Flask(__name__)

@app.route('/property_search', methods=['POST'])
def property_search():
    data = request.get_json()
    properties = get_property(data['location'], data['property_type'], data['budget'])
    return jsonify(properties)

@app.route('/price_estimation', methods=['POST'])
def price_estimation():
    data = request.get_json()
    estimated_price = estimate_price(data['property_id'])
    return jsonify({'estimated_price': estimated_price})

@app.route('/paperwork_automation', methods=['POST'])
def paperwork_automation():
    data = request.get_json()
    paperwork_status = automate_paperwork(data['property_id'], data['buyer_id'])
    return jsonify({'paperwork_status': paperwork_status})

if __name__ == '__main__':
    app.run(debug=True)
```