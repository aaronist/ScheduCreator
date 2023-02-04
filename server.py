from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def data():
    # Your data that you want to send to Angular
    data = {'123': 'value'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
    