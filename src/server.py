from socket import socket, AF_INET, SOCK_DGRAM, timeout
from utils import threaded
from time import sleep

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
                self.soc.settimeout(None)
            except timeout:
                continue
            except OSError:
                break
            self.hard_disk.append(data.decode('utf-8'))
            sleep(0.001)
        #print('Killed Server')
