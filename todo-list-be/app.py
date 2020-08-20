from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'name': 'sushant'})

app.run(debug=True, port=5000)