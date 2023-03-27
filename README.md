# Wake on WAN with Micropython/Telegram
Wake on WAN with Micropython (Made for Raspberry Pi Pico W)

## What is this?

This is a small project to wake your computer from anywhere in the world just by sending in a Telegram message. You can then use TeamViewer, Anydesk or anything you like to control it remotely.

## THIS ONLY WORKS ON ETHERNET AND ONLY IF YOUR MOTHERBOARD SUPPORTS WAKE ON LAN

## How to use

### Step 0
Create a [Telegram](https://telegram.org/) account.

### Step 1 - Creating Bot and finding out your chat id / bot token
Once you are all set-up with your Telegram account, go to Telegram search bar and type BotFather. Follow the instructions and create your bot. (Note your Bot Token, we will be needing that later). Click on the link to access your bot chat (you will be sending messages here to wake your computer). Go to the [web version of Telegram](web.telegram.org) and enter your chat with the bot. At the end of the URL you will find something like this ?chat_id=<Special Number Here>, save that too.

### Step 2 - Find out your MAC Address
Open CMD and type ```ipconfig /all```. There you will see all your internet adapters' info, MAC Address included, note that down too.

### Step 3 - Router Config
This is a bit more technical but easy enough. Go to your router's port forwarding page and add a new rule. It has to be UDP Protocol, with WAN range 0.0.0.0 - 0.0.0.0 , WAN/LAN port add the same number, but be sure you won't need that port for something else so avoid using a common number. I personally use 25566 (one up on Minecraft's most widespread port) and haven;t encountered any issues. Hit save and note down your port number for later.

### Step 3b - Router Config 2
Almost done, I promise. Find the DHCP Port Binding setting and map your Pi's MAC Address (or your device accordingly) to a specific IP Address of your liking

### Step 4 - Fill in secrets.py
This is where all those things we noted down are going to be useful. Add your router's broadcast address too (if you don't know what it is, then it is propably your router's IP but ending in .255 . You can always ask your ISP / Google for the answer) with your WiFi's name in SSID and Password accordingly.

### secrets.py example 
SSID = 'My WiFi'  
PASSWORD = 'SuperStrongPassword'  
MAC = [0x01, 0x02, 0x03] if your MAC address is 01:02:03  
BOT_TOKEN = '45d6f4sd58f4d5s645d5sf89:4d5f8e45df45'  
CHAT_ID = '56421154651'  
BROADCAST = '192.168.1.255'  
PORT = 25566  
