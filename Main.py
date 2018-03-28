from flask import Flask, request

from handler.members import MembershipHandler
from handler.reactions import ReactionsHandler
from handler.replies import ReplyHandler
from handler.users import UsersHandler
from handler.chats import ChatsHandler
from handler.messages import MessageHandler

app = Flask(__name__)


@app.route('/')
def home():
    return "DB Project"


@app.route('/Home')
def welcome():
    return "Welcome to DB Chat!"


@app.route('/Users')
def users():
    handler = UsersHandler()
    return handler.getAllUsers()


@app.route('/Users/<int:user_id>')
def getUserById(user_id):
    return UsersHandler().getUserByID(user_id)

@app.route('/Users/Memberships')
def memberships():
    handler = MembershipHandler()
    return handler.getAllMemberships()

@app.route('/Users/Memberships/<int:user_id>')
def membershipsByUID(user_id):
    handler = MembershipHandler()
    return handler.getMembershipByUID(user_id)

@app.route('/Users/Reactions/<int:user_id>')
def getReactionsByUID(user_id):
    handler = ReactionsHandler()
    return handler.getReactionsByUserID(user_id)

@app.route('/Users/Messages')
def getMessages():
    return MessageHandler().getAllMessages()

@app.route('/Users/Messages/<int:user_id>')
def getMessagesByUID(user_id):
    return MessageHandler().findUserMessages(user_id)

@app.route('/Users/Messages/Replies')
def getReplies():
    handler = ReplyHandler()
    return handler.getAllReplies()

@app.route('/Users/Messages/Replies/<int:owner_id>')
def getRepliesByOwnerID(owner_id):
    handler = ReplyHandler()
    return handler.findByOwnerID(owner_id)



@app.route('/Replies/<int:rep_id>')
def getRepliesByID(rep_id):
    handler = ReplyHandler()
    return handler.getReplyByID(rep_id)


@app.route('/Memberships/<int:mem_id>')
def membershipsByMembershipID(mem_id):
    handler = MembershipHandler()
    return handler.getMembershipsByID(mem_id)

@app.route('/GroupChats')
def chats():
    handler = ChatsHandler()
    return handler.getAllChats()

@app.route('/GroupChats/Memberships/<int:chat_id>')
def membershipsByChatID(chat_id):
    handler = MembershipHandler()
    return handler.getMembershipByChatID(chat_id)


@app.route('/GroupChats/<int:chat_id>')
def getChatById(chat_id):
    return ChatsHandler().getChatByID(chat_id)


@app.route('/GroupChats/<string:chat_name>')
def getChatByName(chat_name):
    return ChatsHandler().findChat(chat_name)


@app.route('/GroupChats/Messages')
def messages():
    handler = MessageHandler()
    return handler.getAllMessages()


@app.route('/GroupChats/Messages/<int:message_id>')
def getMessageById(message_id):
    return MessageHandler().getMessageByID(message_id)


@app.route('/GroupChats/Messages/Chat/<int:chat_id>')
def getChatMessages(chat_id):
    return MessageHandler().findChatMessages(chat_id)

@app.route('/GroupChats/Messages/Replies/<int:message_id>')
def getRepliesByMessageID(message_id):
    handler = ReplyHandler()
    return handler.findMessagesReplies(message_id)

@app.route('/Reactions')
def getReactions():
    handler = ReactionsHandler()
    return handler.getAllReactions()


@app.route('/Reactions/<int:r_id>')
def getReactionsByID(r_id):
    return ReactionsHandler().getReactionsByID(r_id)





if __name__ == '__main__':
    app.run()
