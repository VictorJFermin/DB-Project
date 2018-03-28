from flask import jsonify, request
from dao.member import MemberDAO
from dao.user import UserDAO
from dao.chat import ChatDAO

class MembershipHandler:
#Metodo original
    def getAllMemberships(self):
        dao = MemberDAO()
        result = dao.getAllMemberships()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Members=mapped_result)
#Este metodo es para poner los nombres
    def getAllMemberships2(self):
        dao = MemberDAO()
        dao1 = UserDAO()
        dao2 = ChatDAO()
        result = dao.getAllMemberships()

        mapped_result = []
        for r in result:
            result2 = dao1.getUserById(r[0])
            result3 = dao2.getChatById(r[1])
            r[0] = result2[1] + " " + result2[2]
            r[1] = result3[1]
            mapped_result.append(self.mapToDict2(r))
        return jsonify(Members=mapped_result)
#Metodo original
    def mapToDict(self, row):
        result = {}
        #result['membership_id'] = row[0]
        result['user_id'] = row[0]
        result['chat_id'] = row[1]
        return result

    def mapToDict2(self, row):
        result = {}
        result['user'] = row[0]
        result['chat'] = row[1]
        return result

    #def getMembershipsByID(self, id):
     #   dao = MemberDAO()
      #  result = dao.getMembershipByID(id)
       # if result == None:
        #    return jsonify(Error="MEMBERSHIP NOT FOUND")
        #else:
         #   mapped = self.mapToDict(result)
          #  return jsonify(Members=mapped)

    def getMembershipByUID(self, user_id):
        dao = MemberDAO()
        result = dao.getMembershipByUserID(user_id)
        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Members=mapped_result)

    def getMembershipByUID2(self, user_id):
        dao = MemberDAO()
        dao1 = UserDAO()
        dao2 = ChatDAO()
        result = dao.getMembershipByUserID(user_id)
        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                result2 = dao1.getUserById(r[0])
                result3 = dao2.getChatById(r[1])
                r[0] = result2[1] + " " + result2[2]
                r[1] = result3[1]
                mapped_result.append(self.mapToDict2(r))
            return jsonify(Members=mapped_result)



    def getMembershipByChatID(self, chat_id):
        dao = MemberDAO()
        result = dao.getMembershipByChatID(chat_id)
        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Members=mapped_result)

    def getMembershipByChatID2(self, chat_id):
        dao = MemberDAO()
        dao1 = UserDAO()
        dao2 = ChatDAO()
        result = dao.getMembershipByChatID(chat_id)
        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                result2 = dao1.getUserById(r[0])
                result3 = dao2.getChatById(r[1])
                r[0] = result2[1] + " " + result2[2]
                r[1] = result3[1]
                mapped_result.append(self.mapToDict2(r))
            return jsonify(Members=mapped_result)


