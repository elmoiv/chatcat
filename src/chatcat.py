from sys import argv, exit
from socket import gethostbyname, getfqdn

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt

from gui import Ui_MainWindow
from server import Server
from bridge import MsgThread

class ChatCat(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.version = '1.0.3'
        self.setupUi(self)
        
        self.HOST = gethostbyname(getfqdn())
        self.PORT = 4000
        
        # Threading
        self.msg_thread = MsgThread()
        self.msg_thread.latest_msg.connect(self.MsgThread_Reciever)

        # Connect buttons
        self.buttons = [
            (self.btnConnect,       self.connect,       'Connect to this IP'),
            (self.btnDisconnect,    self.disconnect,    'Disconnect the session'),
            (self.btnSend,          self.send,          'Send a message'),
        ] 
        
        for btn, btn_func, btn_tip in self.buttons:
            btn.setToolTip(btn_tip)
            btn.clicked.connect(btn_func)

        self.grpChat.setEnabled(False)
        self.lblIP.setText(self.HOST)

    def to_chat_history(self, dct):
        self.lstChat.addItem(f'{dct["name"]}: {dct["text"]}')

    def connect(self):
        self.client = Server(self.HOST, self.PORT)
        self.client.start()
        self.grpChat.setEnabled(True)
        self.MsgThread_Starter()

    def disconnect(self):
        self.grpChat.setEnabled(False)
        self.client.stop()
        self.msg_thread.disconnected = True
    
    def send(self):
        dct = {
            'name': self.txtName.text() or 'Anonymous',
            'text': self.txtSend.text()
            }
        self.client.send(str(dct), (self.txtIP.text(), self.PORT))
        self.to_chat_history(dct)

        # Clear Msg Text Box after send and scroll to bottom
        self.txtSend.setText('')
        self.lstChat.scrollToBottom()
    
    def MsgThread_Starter(self):
        self.msg_thread.client = self.client
        self.msg_thread.start()

    def MsgThread_Reciever(self, last_msg):
        self.to_chat_history(last_msg)
        self.lstChat.scrollToBottom()

if __name__ == "__main__":
    app = QApplication(argv)
    GUI = ChatCat()
    GUI.show()
    exit(app.exec_())
