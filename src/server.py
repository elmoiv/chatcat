from socket import socket, AF_INET, SOCK_DGRAM
from utils import threaded
from time import sleep

class Server:
    def __init__(self, host, port, allowed_addr):
        self.host = host
        self.port = port
        self.allowed_addr = allowed_addr
        self.soc = None
        self.is_alive = False
        self.hard_disk = []
        self.error = None
    
    def start(self):
        self.is_alive = True
        self.soc = socket(AF_INET, SOCK_DGRAM)
        self.soc.bind((self.host, self.port))
    
    def stop(self):
        self.is_alive = False
        self.soc.close()
    
    def send(self, data, ip_addr):
        self.soc.sendto(data.encode('utf-8'), ip_addr)

    def get_recieved(self):
        if self.hard_disk:
            return self.hard_disk.pop(0)

    @threaded
    def live_reciever(self):
        while self.is_alive:
            try:
                data, ip = self.soc.recvfrom(1024)
            except Exception as e:
                self.error = str(e)
                break
            
            # Only accept certain ips
            if ip[0] == self.allowed_addr:
                self.hard_disk.append(data.decode('utf-8'))

            sleep(0.001)
