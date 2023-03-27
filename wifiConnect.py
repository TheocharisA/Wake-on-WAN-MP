import network
import machine
import usocket as socket
import secrets

#Connects to WiFi
def wifiStart():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print('Connecting to WiFi')
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    while not wlan.isconnected():
        machine.idle()