# Complete project details at https://RandomNerdTutorials.com/micropython-bme680-esp32-esp8266/

from formatting import *
from socketPage import MySocket


def web_page(fTemp, cTemp, sPressure, sHumidity, sGas, timeNow, dateNow):
    """Create the HTML for the response to a http request
    """

    html = """<html><head><title>ESP with BME680</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"><style>body { text-align: center; font-family: "Trebuchet MS", Arial;}
    table { border-collapse: collapse; margin-left:auto; margin-right:auto; }
    th { padding: 12px; background-color: #0043af; color: white; }
    tr { border: 1px solid #ddd; padding: 12px; }
    tr:hover { background-color: #bcbcbc; }
    td { border: none; padding: 12px; }
    .sensor { color:white; font-weight: bold; background-color: #bcbcbc; padding: 1px;
    </style></head><body><h1>ESP with BME680</h1>
    <h2>""" + dateNow + ' ' + timeNow + """</h2>
    <table><tr><th>MEASUREMENT</th><th>VALUE</th></tr>
    <tr><td>Temp. Celsius</td><td><span class="sensor">""" + cTemp + """</span></td></tr>
    <tr><td>Temp. Fahrenheit</td><td><span class="sensor">""" + fTemp  + """</span></td></tr>
    <tr><td>Pressure</td><td><span class="sensor">""" + sPressure + """ hPa</span></td></tr>
    <tr><td>Humidity</td><td><span class="sensor">""" + sHumidity + """ %</span></td></tr>
    <tr><td>Gas</td><td><span class="sensor">""" + sGas + """ KOhms</span></td></tr>
    </table>
    <form>
        <input type='submit' value='Refresh'>
    </form>
    </body></html>
    """
    return html


theSocket = MySocket(socket, gc, 80)
bme = BME680_I2C(i2c=i2c)

while True:
    try:
        conn, addr = theSocket.listen()
        if (conn):
            temp = bme.temperature
            fTemp = fmtTemp(temp, 'F')
            cTemp = fmtTemp(temp, 'C')
            sPressure = fmtFloat(bme.pressure, 2)
            sHumidity = fmtFloat(bme.humidity, 2)
            sGas = fmtFloat(bme.gas/1000, 2)
            timeNow = rtc.time()
            dateNow = rtc.date()

            print(20*'-', f'{dateNow}  {timeNow}', 20*'-')
            print('Temp: ', fTemp)
            print('Temp: ', cTemp)
            print('Pressure: ', sPressure)
            print('Humidity: ', sHumidity)
            print('Gas: ', sGas)
            print(20*'-')


            response = web_page(fTemp, cTemp, sPressure, sHumidity, sGas, timeNow, dateNow)
            theSocket.respond(conn, addr, response)
    except OSError as e:
        print(e.message())