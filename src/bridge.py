from PyQt5.QtCore import QTread, pyqtSigna

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
            self.latest_msg.emit(msg)
