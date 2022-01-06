# Complete project details at https://RandomNerdTutorials.com/micropython-bme680-esp32-esp8266/
'''Effectively exports:
  socket
  time (sleep)
  machine (Pin and I2C)
  network
  esp
  gc
  bme680 (all objects)
  rtc (uRTC)
'''
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

from wifiTime import uRTC

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21))
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4))

line = 30*'-'
print(f"\n\n\n{line}\n\n\n")
f = open('uAuto.cfg', 'r')
ssid = f.readline().rstrip('\n')
password = f.readline().rstrip('\n')

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

nTries = 0
rtc = uRTC()
while station.isconnected() == False and nTries < connectTries:
    nTries += 1
    print (f'{nTries} tries of {connectTries} failed to connect')
    sleep(1)
if station.isconnected():
    rtc.webTimeRefresh()
    currentTime = rtc.time()
    currentDate = rtc.date()
    address = station.ifconfig()[0]
    print(f'Connection successful on {currentDate} at {currentTime} as {address}')
else:
    print('Connection failed at {} on {}'.format(rtc.time(), rtc.date(())))