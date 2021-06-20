import socket
from time import sleep
from events import Events
from threading import Thread


class OpenProtocol:
    client = None
    __events__ = (('on_update'))
    t = Events()

    def __init__(self, ip, port=4545):
        self.ip = ip
        self.port = port

    def connect(self):
        Thread(target=self.update_cycle, daemon=True).start() 
        
    def update_cycle(self):
        while True:
            print('updating cycle')
            self.t.on_update()
            sleep(1)

    def disconnect(self):
        ...

    def keep_alive(self):
        ...

    def job_subscribe(self):
        self.t.on_update += self.tool_update

    def tool_update(self):
        print('Tool updated')


if __name__ == '__main__':
    tool = OpenProtocol('192.168.0.100', 4545)
    tool.connect()
    tool.job_subscribe()
    while True:
        ... 
