# Complete project details at https://RandomNerdTutorials.com/micropython-bme680-esp32-esp8266/

connectTries = 10    # Number of times to try to connect to the network

try:
  import usocket as socket
except:
  import socket

from time import sleep

from machine import Pin, I2C
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

from bme680 import *

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21))
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4))

ssid = 'starr-5GHz'
password = 'Aa7br60uAW#v'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

nTries = 0
while station.isconnected() == False and nTries < connectTries:
    nTries += 1
    print (nTries, ' tries failed to connect')
    sleep(1)

print('Connection successful')
print(station.ifconfig())
