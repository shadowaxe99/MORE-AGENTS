```python
from flask import Flask, request, jsonify
from .database import get_destination_recommendations, create_itinerary, book_trip

app = Flask(__name__)

@app.route('/recommendations', methods=['POST'])
def recommendations():
    user_preferences = request.json
    recommendations = get_destination_recommendations(user_preferences)
    return jsonify(recommendations)

@app.route('/itinerary', methods=['POST'])
def itinerary():
    trip_details = request.json
    itinerary = create_itinerary(trip_details)
    return jsonify(itinerary)

@app.route('/book', methods=['POST'])
def book():
    booking_details = request.json
    booking_confirmation = book_trip(booking_details)
    return jsonify(booking_confirmation)

if __name__ == '__main__':
    app.run(debug=True)
```