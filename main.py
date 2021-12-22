# Complete project details at https://RandomNerdTutorials.com/micropython-bme680-esp32-esp8266/

from machine import Pin, I2C
from time import sleep
from bme680 import *

'''fmtFloat:
    Format a floating point number and return a string
    Parameters:
        floatV - Floating point number to be formatted
        places - Number of decimal places (default: 2)

    returns a string from the floating point value rounded to the number
    of deficmal places
'''
def fmtFloat(floatV, places=2):
    return str(round(floatV, places))

'''fmtTemp:
    Return the temperature in degrees Celcius or Farenheit as a formatted string
    Paramteters:
        temp - Temperature as a floating point value
        units - C for Celcius or F for Farenheit (not case sensitive; default:'c')
'''
def fmtTemp(temp, units='c'):
    if units.lower() != 'c':
        temp = temp * (9/5) + 32

    return fmtFloat(temp, 2) + ' C'

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21))
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4))

bme = BME680_I2C(i2c=i2c)

while True:
  try:
    temp = bme.temperature
    temp = fmtTemp(temp, 'F')
    #   Convert celsius to farenheit
    # temp = (bme.temperature) * (9/5) + 32
    # temp = str(round(temp, 2)) + 'F'

    hum = fmtFloat(bme.humidity, 2) + ' %'

    pres = fmtFloat(bme.pressure, 2) + ' hPa'

    gas = fmtFloat(bme.gas/1000, 2) + ' KOhms'

    print('Temperature:', temp)
    print('Humidity:', hum)
    print('Pressure:', pres)
    print('Gas:', gas)
    print('-------')
  except OSError as e:
    print('Failed to read sensor.')

  sleep(5)
