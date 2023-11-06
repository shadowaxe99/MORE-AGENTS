```python
from flask import Flask, request, jsonify
from .database import get_repo_analysis, get_pr_reviews, get_coding_buddy_conversations

app = Flask(__name__)

@app.route('/repo_analysis', methods=['POST'])
def repo_analysis():
    data = request.get_json()
    repo_url = data.get('repo_url')
    analysis = get_repo_analysis(repo_url)
    return jsonify(analysis), 200

@app.route('/pr_reviews', methods=['POST'])
def pr_reviews():
    data = request.get_json()
    pr_url = data.get('pr_url')
    reviews = get_pr_reviews(pr_url)
    return jsonify(reviews), 200

@app.route('/coding_buddy_conversations', methods=['POST'])
def coding_buddy_conversations():
    data = request.get_json()
    conversation_id = data.get('conversation_id')
    conversations = get_coding_buddy_conversations(conversation_id)
    return jsonify(conversations), 200

if __name__ == '__main__':
    app.run(debug=True)
```