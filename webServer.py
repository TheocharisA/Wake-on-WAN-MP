import wakeOnLan
import telegramSync
import secrets
import urequests as requests
import usocket as socket

global latestUpdate
counter = 0

def startServer():

    #Pre-Loop Setup
    lastId = -1
    socketStart()
    telegramSync.sendMessage('Bot alive. What to do?')
    contents = telegramSync.getUpdates(lastId)
    lastId = contents['message_id']
    x = True

    #Server Loop
    while x:
        try:
            contents = telegramSync.getUpdates(lastId)
            if contents['message_id'] != -1:
                lastId = contents['message_id']
                if contents['text'] == 'Wake':
                    wakeOnLan.wakePC()
                    telegramSync.sendMessage('PC Booting')
        except OSError as e:
            #Print Error and restart socket connection
            print('Connection closed')
            print('Error: ', e)
            socketStart()

#Binds pico to desired port
def socketStart():
    addr = socket.getaddrinfo('0.0.0.0', secrets.PORT)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)