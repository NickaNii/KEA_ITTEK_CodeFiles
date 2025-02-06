# Complete project details at https://RandomNerdTutorials.com
# https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/
# Put the following code in boot.py to create a webserver running on your ESP

try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

import random
lowercase = 'abcdefghijklmnopqrstuvwxyz'

ssid = ''
for i in range(10):
    ssid += random.choice(lowercase)
print('SSID:',ssid)
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Hello, World!</h1></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = web_page()
  conn.send(response)
  conn.close()