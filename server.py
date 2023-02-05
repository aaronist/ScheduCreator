from flask import Flask, request, jsonify
from flask_cors import CORS
import course

app = Flask(__name__)
CORS(app)


globalD = {}

@app.route('/department')
def data():
    return course.getTermInfo()

@app.route('/course', methods= ['POST'])
def data1():

    global globalD 
    globalD= request.get_json()
    print("data1")
    print(globalD)

@app.route('/courseList')
def data2():

        #{'term': 'Spring 2022', 'department': 'ANATOMY'}
    print("data2")
    print(globalD)
    return course.getCourseNum(globalD)


if __name__ == '__main__':
    print('a')
    app.run(debug=True)
    