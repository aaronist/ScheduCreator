from flask import Flask,jsonify
from flask_cors import CORS
import course

app = Flask(__name__)
CORS(app)



@app.route('/')
def data():
    # Your data that you want to send to Angular
<<<<<<< HEAD
    data = {'123': 'value'}
    return jsonify("Hello")
    #return jsonify(data)
=======
    temp = {'departments': course.getTermInfo()}    
    return jsonify(course.getTermInfo())
>>>>>>> 73db5aa269a114775a710b99961d87a2065a9a56

if __name__ == '__main__':
    app.run(debug=True)
    