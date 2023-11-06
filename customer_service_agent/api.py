```python
from flask import Flask, request, jsonify
from database import get_customer_info, update_customer_info, get_customer_query, update_customer_query

app = Flask(__name__)

@app.route('/customer_info', methods=['GET'])
def customer_info():
    customer_id = request.args.get('customer_id')
    info = get_customer_info(customer_id)
    return jsonify(info)

@app.route('/customer_info', methods=['POST'])
def update_info():
    customer_id = request.args.get('customer_id')
    new_info = request.get_json()
    update_customer_info(customer_id, new_info)
    return jsonify({'status': 'success'})

@app.route('/customer_query', methods=['GET'])
def customer_query():
    query_id = request.args.get('query_id')
    query = get_customer_query(query_id)
    return jsonify(query)

@app.route('/customer_query', methods=['POST'])
def update_query():
    query_id = request.args.get('query_id')
    new_query = request.get_json()
    update_customer_query(query_id, new_query)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
```