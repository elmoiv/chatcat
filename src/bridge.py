from PyQt5.QtCore import QThread, pyqtSignal
from utils import send_info, threaded
from time import sleep

class MsgThread(QThread):
    latest_msg = pyqtSignal(dict)
    typing_status = pyqtSignal(list)
    online_status = pyqtSignal(tuple)
    server_broken = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.client = None
        self.connected = True
        self.is_typing = False
        self.is_online = False

    def run(self):
        self.client.live_reciever()
        self.online_watcher()

        while self.connected:
            sleep(0.001)

            # If Server disconnected unexpectedly (Emit error signal)
            if not self.client.is_alive:
                self.server_broken.emit(self.client.error)

            msg = self.client.get_recieved()
            if msg == None:
                continue
            
            msg = eval(msg)

            _type, text = msg['type'], msg['text'] 
            
            if _type == 'msg':
                self.latest_msg.emit(msg)

            if [_type, text] == ['info', 'typing']:
                self.show_is_typing()
                
            if [_type, text] == ['info', 'online']:
                self.is_online = True
    
    @threaded
    def show_is_typing(self):
        '''
        Implement "typing..." messenger feature
        '''
        if self.is_typing:
            return

        self.is_typing = True
        self.typing_status.emit(['Your friend is typing...', 'lime'])
        sleep(0.5)
        self.typing_status.emit(['Idle', 'black'])
        self.is_typing = False

    @threaded
    def online_watcher(self):
        '''
        Implement online status feature
        '''
        while self.connected:
            self.online_status.emit(
                    [
                        ('Offline', 'red'),
                        ('Online', 'green')
                    ][self.is_online], 
                )
            
            self.is_online = False
            sleep(1)

class OnlineBroadcastThread(QThread):
    '''
    Online status Broadcaster
    '''
    def __init__(self):
        QThread.__init__(self)
        self.connected = True
        self.client = None
        self.server = None
        self.name = None

    def run(self):
        while self.connected:
            try:
                send_info(
                    self.client,
                    self.server,
                    'online',
                    self.name
                )
            except OSError:
                continue
            
            sleep(0.5)