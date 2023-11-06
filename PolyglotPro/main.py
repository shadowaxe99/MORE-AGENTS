
from flask import Flask, request, jsonify
from google.cloud import translate_v2 as translate
from utils import validate_language, validate_text

app = Flask(__name__)
translate_client = translate.Client()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()

    source_language = data.get('source_language')
    target_language = data.get('target_language')
    text = data.get('text')

    if not validate_language(source_language) or not validate_language(target_language):
        return jsonify({'error': 'Invalid language code'}), 400

    if not validate_text(text):
        return jsonify({'error': 'Invalid text'}), 400

    result = translate_client.translate(text, target_language=target_language, source_language=source_language)

    return jsonify({'translated_text': result['translatedText']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

