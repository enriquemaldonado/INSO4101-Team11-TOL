from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from controller.users import UserController

app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the TOL DB App!'

@app.route('/register', methods=['POST'])
def registerUser():
    if request.method == 'POST':
        return UserController().registerUser(request.json)
    else:
        return jsonify("Not Supported"), 405

@app.route('/deleteuser', methods=['DELETE'])
def deleteUser():
    if request.method == 'DELETE':
        return UserController().deleteUser(request.json)
    else:
        return jsonify("Not Supported"), 405


if __name__ == '__main__':
    app.run()