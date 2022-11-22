from flask import jsonify
from dao.users import UserDAO


class UserController:

    def registerUser(self, json):
            if json and len(json) == 3:
                uname = json['name']
                uemail = json['username'] + '@tol.com'
                upassword = json['password']
                if uname and uemail and upassword:
                    dao = UserDAO()
                    uid = dao.insertUser(uname, uemail, upassword)
                    if(uid == 0):
                        return jsonify(Error="Username already in use. Try adding a number to your username or changing it."), 406
                    result = {}
                    result["UserID"] = uid
                    result["UserName"] = uname
                    result["UserEmail"] = uemail
                    result["UserPassword"] = upassword
                    return jsonify(User=result), 201
                else:
                    return jsonify(Error="Malformed post request"), 400
            else:
                return jsonify(Error="Malformed post request"), 400

    def deleteUser(self, json):
            if json and len(json) == 2:
                user = json['UserEmail']
                auth = json['UserPassword']

                if user and auth:
                    dao = UserDAO()
                    result = dao.deleteUser(user, auth)
                    if(result["Email"] == 0 and result["Password"] == 0):
                        return jsonify(Error="Email or Password is invalid."), 401
                    result["TerminationStatus"] = "User Terminated"
                    return jsonify(Users=result), 202
                else:
                    return jsonify(Error="Malformed post request"), 400
            else:
                return jsonify(Error="Malformed post request"), 400
