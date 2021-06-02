from PyQt5.QtCore import QThread, pyqtSignal
from server import threaded
from utils import send_info
from time import sleep

class MsgThread(QThread):
    latest_msg = pyqtSignal(dict)
    typing_status = pyqtSignal(list)
    online_status = pyqtSignal(list)

    def __init__(self):
        QThread.__init__(self)
        self.client = None
        self.disconnected = False
        self.still_typing = True
        self.still_online = False

    def run(self):
        self.client.live_recieve()
        self.online_watcher()

        while not self.disconnected:
            sleep(0.001)
            
            if self.client.hard_disk:
                
                msg = eval(self.client.hard_disk.pop(0))
                if msg['type'] == 'msg':
                    self.latest_msg.emit(msg)
                
                if msg['type'] == 'info':
                    
                    if msg['text'] == 'typing' and self.still_typing:
                        #print('info type: is typing...')
                        self.is_typing()
                    
                    if msg['text'] == 'online':
                        #print('info type: is online...')
                        self.still_online = True
        
        #print('Killed Message Reciever.')
    
    @threaded
    def is_typing(self):
        '''
        Implement "typing..." messenger feature
        '''
        self.still_typing = False
        self.typing_status.emit(['Your friend is typing...', 'lime'])
        sleep(0.5)
        self.typing_status.emit(['IDLE.', 'black'])
        self.still_typing = True

    @threaded
    def online_watcher(self):
        '''
        Implement online status feature
        '''
        while not self.disconnected:
            #print(self.still_online)
            if self.still_online:
                self.online_status.emit(['Online', 'green'])
            else:
                self.online_status.emit(['Offline', 'red'])
            
            self.still_online = False
            sleep(1)
        #print('Killed Online Watcher.')
        

class OnlineBroadcastThread(QThread):
    '''
    Online status Broadcaster
    '''
    def __init__(self):
        QThread.__init__(self)
        self.disconnected = False
        self.client = None
        self.server = None
        self.name = None

    def run(self):
        while not self.disconnected:
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

        #print('Killed Online Broadcast.')