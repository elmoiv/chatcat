from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep

class MsgThread(QThread):
    latest_msg = pyqtSignal(dict)

    def __init__(self):
        QThread.__init__(self)
        self.client = None
        self.disconnected = False

    def run(self):
        self.client.live_recieve()
        while not self.disconnected:
            sleep(0.001)
            if self.client.hard_disk:
                print(self.client.hard_disk)
                msg = eval(self.client.hard_disk.pop(0))
                self.latest_msg.emit(msg)
