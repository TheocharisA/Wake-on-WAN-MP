import wakeOnLan
import wifiConnect
import telegramSync
import secrets
import machine

global latestUpdate
counter = 0

def startServer():

    #Pre-Loop Setup
    lastId = -1
    telegramSync.sendMessage('Bot alive. What to do?')
    contents = telegramSync.getUpdates(lastId)
    lastId = contents['message_id']
    x = True

    #Server Loop
    while x:
        try:
            #Sleep for 20s then send request
            machine.lightsleep(20000)
            contents = telegramSync.getUpdates(lastId)
            if contents['message_id'] != -1:
                lastId = contents['message_id']
                if contents['text'] == 'Wake':
                    wakeOnLan.wakePC()
                    telegramSync.sendMessage('PC Booting')
        except OSError as e:
            #Print Error and soft resertting device
            print('Connection closed')
            print('Error: ', e)
