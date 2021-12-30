'''wifiTime:
    Object to get the wifi time

    Many thanks to Alan Wang's ESP8266 MicroPython Web Clock,
    https://www.hackster.io/alankrantas/very-simple-micropython-esp8266-esp-12-web-clock-3c5c6f

'''
import network, urequests, utime, machine
from machine import RTC, I2C, Pin

class uRTC():
    '''
    '''
    def __init__(self, rtc=0, web_query_delay=60000, retry_delay=5000,
                url="http://worldtimeapi.org/api/timezone/America/Detroit"
):
        self.web_query_delay = web_query_delay # interval time of web JSON query
        self.retry_delay = retry_delay # interval time of retry after a failed Web query
        if rtc:
            self.rtc = rtc
        else:
            self.rtc = RTC()
        self.url = url

        self.update_time = utime.ticks_ms() - self.web_query_delay
        self.webTimeRefresh()


    def webTimeRefresh(self):
        '''Refresh the webtime in the RTC'''
        if utime.ticks_ms() - self.update_time >= self.web_query_delay:
            print(f'Update Time: {self.update_time} -- Web Query Delay: {self.web_query_delay}')

            # HTTP GET data
            print('Updating clock\nURL:', self.url)
            response = urequests.get(self.url)

            if response.status_code == 200: # query success
                # parse JSON
                parsed = response.json()
                datetime_str = str(parsed["datetime"])
                year = int(datetime_str[0:4])
                month = int(datetime_str[5:7])
                day = int(datetime_str[8:10])
                hour = int(datetime_str[11:13])
                minute = int(datetime_str[14:16])
                second = int(datetime_str[17:19])
                subsecond = int(round(int(datetime_str[20:26]) / 10000))
                print(datetime_str)

                # update internal RTC
                self.rtc.datetime((year, month, day, 0, hour, minute, second, subsecond))
                self.update_time = utime.ticks_ms()
                print("RTC updated\n")

            else: # query failed, retry retry_delay ms later
                self.update_time = utime.ticks_ms() - self.web_query_delay + self.retry_delay

    def date(self):
        self.webTimeRefresh()
        return "{1:02d}/{2:02d}/{0:4d}".format(*self.rtc.datetime())

    def time(self):
        self.webTimeRefresh()
        return "{4:02d}:{5:02d}:{6:02d}".format(*self.rtc.datetime())
