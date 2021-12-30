# uAtmosphere
#Purpose:
Report local atmospheric conditions by reading a [BME680](https://www.adafruit.com/product/3660) connected to an ESP32 and reporting it to the world via MQTT.

## NOTE:
This version will work with a local webpage (not sent to MQTT) to display the
1. Temperature in Celsius
2. Temperature in Fahrenheit
3. Air Pressure
4. Humidity
5. Gas resistance - The gas sensor on the BME680 adjusts resistance based on the amount of gases in the air.  The more the gases, the higher the resistance.

## Note 2:
When you run the program on the ESP32, it will print to the serial port the