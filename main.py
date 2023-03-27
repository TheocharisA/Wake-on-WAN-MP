import wifiConnect
import webServer

if __name__ == '__main__':
    #Connect to WiFi
    wifiConnect.wifiStart()
    #Initialize Server
    webServer.startServer()