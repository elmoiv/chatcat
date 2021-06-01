from sys import argv, exit
from socket import gethostbyname, getfqdn

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator

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
            (self.btnConnect,    self.connect,    'Connect to this IP'),
            (self.btnDisconnect, self.disconnect, 'Disconnect the session'),
            (self.btnSend,       self.send,       'Send a message'),
        ] 
        
        for btn, btn_func, btn_tip in self.buttons:
            btn.setToolTip(btn_tip)
            btn.clicked.connect(btn_func)

        # Accept
        rgx = QRegExp(r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b')
        validator = QRegExpValidator(rgx, self)
        self.txtIP.setValidator(validator)

        self.disable_widget(self.grpChat, self.btnDisconnect)
        self.lblIP.setText(self.HOST)

    def disable_widget(self, *widgets):
        for widget in widgets:
            widget.setEnabled(False)
    
    def enable_widget(self, *widgets):
        for widget in widgets:
            widget.setEnabled(True)

    def to_chat_history(self, dct):
        self.lstChat.addItem(f'{dct["name"]}: {dct["text"]}')

    def connect(self):
        if len(self.txtIP.text().split('.')) != 4:
            QMessageBox.critical(self, 'IP Validation Error!', 'Please Enter a Valid IP Address!')
            return
        
        self.client = Server(self.HOST, self.PORT)
        self.client.start()
        self.MsgThread_Starter()

        self.disable_widget(self.btnConnect)
        self.enable_widget(self.grpChat, self.btnDisconnect)

    def disconnect(self):
        self.client.stop()
        self.msg_thread.disconnected = True

        self.disable_widget(self.grpChat, self.btnDisconnect)
        self.enable_widget(self.btnConnect)
    
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
