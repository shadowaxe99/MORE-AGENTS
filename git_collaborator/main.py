```python
import os
from flask import Flask, request, jsonify
from database import Database
from api import GitAPI

app = Flask(__name__)
db = Database()
api = GitAPI()

@app.route('/analyze_repo', methods=['POST'])
def analyze_repo():
    data = request.get_json()
    repo_url = data.get('repo_url')
    if not repo_url:
        return jsonify({'error': 'Repo URL is required'}), 400
    analysis = api.analyze_repo(repo_url)
    db.save_analysis(analysis)
    return jsonify(analysis), 200

@app.route('/review_pr', methods=['POST'])
def review_pr():
    data = request.get_json()
    pr_url = data.get('pr_url')
    if not pr_url:
        return jsonify({'error': 'PR URL is required'}), 400
    review = api.review_pr(pr_url)
    db.save_review(review)
    return jsonify(review), 200

@app.route('/coding_buddy', methods=['POST'])
def coding_buddy():
    data = request.get_json()
    code = data.get('code')
    if not code:
        return jsonify({'error': 'Code is required'}), 400
    conversation = api.coding_buddy(code)
    db.save_conversation(conversation)
    return jsonify(conversation), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```