from flask import Flask, request, jsonify, json
from hangman import Hangman
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

Words = [
    {
        'id': 1,
        'word':'test',
    },
    {
        'id': 2,
        'word':'cats',
    },
    {
        'id': 3,
        'word':'exponential',
    }
]

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route('/api/game', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        secret_word = random.choice(Words)
        dashes= "_" * len(secret_word['word'])
        return jsonify(secret_word, dashes)
    if request.method == 'POST':
        req_data = request.get_json(force=True)
        results= Hangman(req_data['guess'], req_data['word'], req_data['dashes'], req_data['guessleft'])
        return jsonify(results)
    secret_word = random.choice(Words)
    return jsonify(secret_word)

    

if __name__ == '__main__':
    app.run()