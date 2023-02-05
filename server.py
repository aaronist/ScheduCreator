from flask import Flask,jsonify
from flask_cors import CORS
import course

app = Flask(__name__)
CORS(app)



@app.route('/department')
def data():
    return course.getTermInfo()


if __name__ == '__main__':
    print('a')
    app.run(debug=True)
    