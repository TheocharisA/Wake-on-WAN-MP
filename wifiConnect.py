import network
import machine
import usocket as socket
import secrets
import urequests as requests

#Connects to WiFi
def wifiStart():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print('Connecting to WiFi')
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    while not wlan.isconnected():
        machine.idle()

#Binds pico to desired port
def socketStart():
    addr = socket.getaddrinfo('0.0.0.0', secrets.PORT)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)
    return s

#Tests internet connectivity
def connectionStatus(s):
    try:
        s = requests.get('https://clients3.google.com/generate_204')
        s.close()
        print("Connected To Internet")
        return True
    except OSError as e:
        print("No internet access")
        return False
