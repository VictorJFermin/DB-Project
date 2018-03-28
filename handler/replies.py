from flask import jsonify, request
from dao.reply import ReplyDAO
from dao.message import MessageDAO
from dao.user import UserDAO

class ReplyHandler:
    def getAllReplies(self):
        dao = ReplyDAO()
        result = dao.getAllReplies()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Replies=mapped_result)

    def getAllReplies2(self):
        dao = ReplyDAO()
        dao1 = UserDAO()
        dao2 = MessageDAO()
        result = dao.getAllReplies()
        mapped_result = []
        for r in result:
            result1 = dao1.getUserById(r[1])
            result2 = dao2.getMessageById(r[2])
            r[1] = result1[1] + " " + result1[2]
            r[2] = result2[1]
            mapped_result.append(self.mapToDict2(r))
        return jsonify(Replies=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['reply_id'] = row[0]
        result['owner_id'] = row[1]
        result['message_id'] = row[2]
        result['text_field'] = row[3]
        result['reply_date'] = row[4]
        return result

    def mapToDict2(self, row):
        result = {}
        result['reply_id'] = row[0]
        result['replying user'] = row[1]
        result['original message'] = row[2]
        result['reply'] = row[3]
        result['reply_date'] = row[4]
        return result

    def getReplyByID(self, id):
        dao = ReplyDAO()
        result = dao.getReplyById(id)
        if result == None:
            return jsonify(Error="REPLY NOT FOUND")
        else:
            mapped = self.mapToDict2(result)
            return jsonify(Reply=mapped)

    def getReplyByID2(self, id):
        dao = ReplyDAO()
        dao1 = UserDAO()
        dao2 = MessageDAO()
        result = dao.getReplyById(id)
        if result == None:
            return jsonify(Error="REPLY NOT FOUND")
        else:
            result1 = dao1.getUserById(result[1])
            result2 = dao2.getMessageById(result[2])
            result[1] = result1[1] + " " + result1[2]
            result[2] = result2[1]
            mapped = self.mapToDict2(result)
            return jsonify(Reply=mapped)

    def findMessagesReplies(self, message_id):
        dao = ReplyDAO()
        result = dao.findReplyByMessageId(message_id)
        if result == None:
            return jsonify(Error="MESSAGE NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Replies=mapped_result)

    def findMessagesReplies2(self, message_id):
        dao = ReplyDAO()
        dao1 = UserDAO()
        dao2 = MessageDAO()
        result = dao.findReplyByMessageId(message_id)
        if result == None:
            return jsonify(Error="MESSAGE NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                result1 = dao1.getUserById(r[1])
                result2 = dao2.getMessageById(r[2])
                r[1] = result1[1] + " " + result1[2]
                r[2] = result2[1]
                mapped_result.append(self.mapToDict2(r))
            return jsonify(Replies=mapped_result)

    def findByOwnerID(self, user_id):
        dao = ReplyDAO()
        result = dao.searchByOwnerId(user_id)
        if result == None:
            return jsonify(Error="OWNER NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Replies=mapped_result)

    def findByOwnerID2(self, user_id):
        dao = ReplyDAO()
        dao1 = UserDAO()
        dao2 = MessageDAO()
        result = dao.searchByOwnerId(user_id)
        if result == None:
            return jsonify(Error="OWNER NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                result1 = dao1.getUserById(r[1])
                result2 = dao2.getMessageById(r[2])
                r[1] = result1[1] + " " + result1[2]
                r[2] = result2[1]
                mapped_result.append(self.mapToDict2(r))
            return jsonify(Replies=mapped_result)