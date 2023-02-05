from flask import Flask, request, jsonify
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

@app.route('/course', methods= ['POST'])
def data1():

    data2 = request.get_json()

    print(data2)

    return data2


if __name__ == '__main__':
    app.run(debug=True)