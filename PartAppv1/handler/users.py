from flask import jsonify, request
from dao.user import UserDAO

class UsersHandler:
    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(User=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        result['uphone'] = row[2]
        result['uemail'] = row[3]
        result['upass'] = row[4]
        return result