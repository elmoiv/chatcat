from sys import argv, exit
from socket import gethostbyname, getfqdn

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QWidget, QLabel, QHBoxLayout, QLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor

from gui import Ui_MainWindow
from server import Server
from bridge import MsgThread

class ChatCat(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.version = '1.0.0'
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

        self.lblIP.setText(self.HOST)
        self.txtSend.setPlainText('')

        self.disable_widget(self.grpChat, self.btnDisconnect)

    def add_msg_to_chat(self, dct, is_sender=True):
        '''
        Add the ability to edit list items as html
        Align sender to right and other to left
        '''
        list_item = QListWidgetItem() 
        widget = QWidget()
        align = ['right', 'left'][is_sender]
        text = dct['text'].replace('\n', '<br>')
        label =  QLabel(f'<p dir="rtl" style="text-align:{align};"><b>{dct["name"]}'
                        #                                  "‎" is not empty text
                        #                              Used to correct arabic-english mix
                        f'</b><br><span style="color:#ff0000;">{text+"‎"}</span></p>'
                )
        
        horizontal_box = QHBoxLayout()
        horizontal_box.addWidget(label)
        horizontal_box.setSizeConstraint(QLayout.SetMaximumSize)
        
        widget.setLayout(horizontal_box)      
        
        if not is_sender:
            list_item.setBackground(QColor('#e5e4e0'))
        
        self.lstChat.addItem(list_item)
        list_item.setSizeHint(QSize(100, 70 + 25 * text.count('<br>'))) 
        self.lstChat.setItemWidget(list_item, widget)
 
    
    def disable_widget(self, *widgets):
        for widget in widgets:
            widget.setEnabled(False)
    
    def enable_widget(self, *widgets):
        for widget in widgets:
            widget.setEnabled(True)

    def connect(self):
        if len(self.txtIP.text().split('.')) != 4:
            QMessageBox.critical(
                self,
                'IP Validation Error!',
                'Please Enter a Valid IP Address!'
            )
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
        text = self.txtSend.toPlainText()

        dct = {
            'type': 'msg',
            'name': self.txtName.text() or 'Anonymous',
            'text': text
            }
        self.client.send(str(dct), (self.txtIP.text(), self.PORT))
        self.add_msg_to_chat(dct)

        # Clear Msg Text Box after send and scroll to bottom
        self.txtSend.setPlainText('')
        self.lstChat.scrollToBottom()
    
    def MsgThread_Starter(self):
        self.msg_thread.client = self.client
        self.msg_thread.start()

    def MsgThread_Reciever(self, last_msg):
        self.add_msg_to_chat(last_msg, False)
        self.lstChat.scrollToBottom()

if __name__ == "__main__":
    app = QApplication(argv)
    GUI = ChatCat()
    GUI.show()
    exit(app.exec_())
