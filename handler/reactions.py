from flask import jsonify, request
from dao.reaction import ReactionDAO

class ReactionsHandler:
    def getAllReactions(self):
        dao = ReactionDAO()
        result = dao.getAllReactions()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Reactions=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['message_id'] = row[1]
        result['user_id'] = row[2]
        result['reaction'] = row[3]  # like/dislike
        return result

    def getReactionsByID(self, id):
        dao = ReactionDAO()
        result = dao.getReactionById(id)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped = self.mapToDict(result)
            return jsonify(Reaction=mapped)

    def getReactionsByUserID(self, uid):
        dao = ReactionDAO()
        result = dao.getReactionByUserId(uid)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
               mapped_result.append(self.mapToDict(r))
            return jsonify(Reaction=mapped_result)