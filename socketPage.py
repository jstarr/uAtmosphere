# Complete project details at https://RandomNerdTutorials.com/micropython-bme680-esp32-esp8266/

from bme680 import *
# from wifiTime import uRTC

class MySocket:
    """MySocket handles getting a message from the user via web connection and the response
    Usage:
        theSocket = MySocket(socket, gc, port)
    Where:
        socket  - A socket represents an endpoint on a network device, and when two sockets are connected together communication can proceed.
        gc      - The garbage collector
        port    - Which port to bind the socket to
    """


    def __init__(self, socket=0, gc=0, port=80):
        self._gc = gc
        self._port = port
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.bind(('', self._port))

    def _collectGarbage(self):
        if self._gc.mem_free() < 102000:
            self._gc.collect()


    def listen(self):
        """Listen on the web for an http request
        """
        self._s.listen(5)

        try:
            self._collectGarbage()
            print('Listening...')
            conn, addr = self._s.accept()
            return (conn, addr)
        except OSError as e:
            conn.close()
            print('Connection closed')

    def respond(self, conn, addr, response):
        """Respond to an http request
        """
        try:
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)

            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
        except OSError as e:
            conn.close()
            print('Connection closed')