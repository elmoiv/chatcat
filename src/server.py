from socket import socket, AF_INET, SOCK_DGRAM, timeout
from time import sleep
from threading import Thread

def threaded(fn):
    """
    Thread wrapper function (decorator)
    """
    def run(*k, **kw):
        t = Thread(target=fn, args=k, kwargs=kw)
        t.start()
        return t
    return run

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.soc = None
        self.is_alive = False
        self.hard_disk = []
    
    def start(self):
        self.is_alive = True
        self.soc = socket(AF_INET, SOCK_DGRAM)
        self.soc.bind((self.host, self.port))
    
    def stop(self):
        self.is_alive = False
        self.soc.close()
    
    def send(self, data, ip_addr):
        self.soc.sendto(data.encode('utf-8'), ip_addr)

    @threaded
    def live_recieve(self):
        while self.is_alive:
            try:
                self.soc.settimeout(1)
                data, ip = self.soc.recvfrom(1024)
                print(data)
                self.soc.settimeout(None)
            except timeout:
                continue
            except OSError:
                break
            self.hard_disk.append(data.decode('utf-8'))
            sleep(0.001)
        print('Killed Server')
