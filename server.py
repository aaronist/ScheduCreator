from flask import Flask,jsonify
from flask_cors import CORS
import course

app = Flask(__name__)
CORS(app)



@app.route('/department')
def data():
    # Your data that you want to send to Angular

    #temp = {'departments': []}

    return course.getTermInfo()
    #jsonify(course.getTermInfo())


if __name__ == '__main__':
    app.run(debug=True)