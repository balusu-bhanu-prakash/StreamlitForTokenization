from flask import Flask, request, jsonify
from tokenizer import tokenize_text

app = Flask(__name__)

@app.route('/tokenize', methods=['POST'])
def tokenize():
    data = request.get_json()
    text = data.get('text', '')
    tokens = tokenize_text(text)
    return jsonify({'tokens': tokens})

if __name__ == '__main__':
    app.run(debug=True, port=5000)