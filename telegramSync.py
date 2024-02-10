import secrets
import urequests as requests

requestURL = 'https://api.telegram.org/bot' + secrets.BOT_TOKEN + '/getUpdates?offset=-1'
sendURL = 'https://api.telegram.org/bot' + secrets.BOT_TOKEN + '/sendMessage'

#Sends message to you
def sendMessage(msg):
    id = requests.post(sendURL + "?chat_id=" + secrets.CHAT_ID + "&text=" + str(msg))
    print("Message Sent:", msg)
    id.close()

#Reads last message sent to conversation
def getUpdates(lastId):
    message = requests.get(requestURL).json()
    if message == {'result': [], 'ok': True}:
        return {'message_id': -1, "text": ''}
    else:
        message_shorten = message["result"][0]["message"]
        if message_shorten["message_id"] > lastId:
            return {'message_id': message_shorten["message_id"], 'text': message_shorten["text"]}
        return {'message_id': lastId, "text": ''}
        

