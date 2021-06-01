from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep

class MsgThread(QThread):
    latest_msg = pyqtSignal(dict)
    latest_info = pyqtSignal(dict)

    def __init__(self):
        QThread.__init__(self)
        self.client = None
        self.disconnected = False

    def run(self):
        self.client.live_recieve()
        while not self.disconnected:
            
            sleep(0.001)
            
            if self.client.hard_disk:
                
                msg = eval(self.client.hard_disk.pop(0))
                if msg['type'] == 'msg':
                    self.latest_msg.emit(msg)
                if msg['type'] == 'info':
                    self.latest_info.emit(msg)
        
        # Reset disconnected signal to fix not working after disconnected
        self.disconnected = False
        print('Killed Message Reciever')