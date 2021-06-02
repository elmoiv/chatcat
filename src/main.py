from time import sleep
from socket import gethostbyname, getfqdn

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem, QWidget, QLabel, QHBoxLayout, QLayout
from PyQt5.QtCore import Qt, QRegExp, QSize, QEvent
from PyQt5.QtGui import QRegExpValidator, QColor, QPixmap, QIcon

from gui import Ui_MainWindow
from server import Server
from bridge import MsgThread, OnlineBroadcastThread
from utils import send_msg, send_info, ip2id, id2ip
from assets import app_icon

class ChatCat(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.version = '1.0.0'

        # Add window icon
        self.icon = self.processIcon(app_icon)
        self.setWindowIcon(self.icon)
        self.setupUi(self)
        
        self.client = None
        self.HOST = gethostbyname(getfqdn())
        self.SERVER = None
        self.PORT = 4000
        
        # Threading
        self.msg_thread = MsgThread()

        self.online_broadcast_thread = OnlineBroadcastThread()

        # Connect buttons
        self.buttons = [
            (self.btnConnect,    self.connect,    'Connect to this IP'),
            (self.btnDisconnect, self.disconnect, 'Disconnect the session'),
            (self.btnSend,       self.send,       'Send a message'),
        ] 
        
        for btn, btn_func, btn_tip in self.buttons:
            btn.setToolTip(btn_tip)
            btn.clicked.connect(btn_func)

        # Accept correct IPs in textIP
        rgx = QRegExp(r'[0-9a-fA-F]{8}')
        validator = QRegExpValidator(rgx, self)
        self.txtIP.setValidator(validator)
        self.txtIP.textChanged.connect(self.txtIPChanged)

        self.lblIP.setText(ip2id(self.HOST).upper())

        self.txtSend.textChanged.connect(self.txtSendChanged)
        self.txtSend.setPlainText('')
        self.txtSend.installEventFilter(self)  # Install self.eventFilter()

        self.disable_widget(self.grpChat, self.btnDisconnect, self.btnConnect)

    @staticmethod
    def processIcon(icon_data):
        """
        Create icon pixmap object from raw data
        """
        pix = QPixmap()
        icon = QIcon()
        pix.loadFromData(icon_data)
        icon.addPixmap(pix)
        return icon

    def eventFilter(self, obj, event):
        '''
        Implement Facebook Messenger sending mechanism
        - Enter -> Send
        - Shift + Enter -> Add \n
        '''
        if obj is self.txtSend and event.type() == QEvent.KeyPress:
            # If Pressed key is Enter
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                
                # If Second key is Shift (Shift + Enter)
                if event.modifiers() == Qt.ShiftModifier:
                    
                    # Add \n and move cursor to end of text
                    text = self.txtSend.toPlainText() + '\n'
                    self.txtSend.setPlainText(text)
                    cursor = self.txtSend.textCursor()
                    cursor.setPosition(len(text))
                    self.txtSend.setTextCursor(cursor)
                
                # If only Enter is pressed
                else:
                    self.send()
                return True
        return super(ChatCat, self).eventFilter(obj, event)

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
    
    def txtIPChanged(self):
        '''
        Only Enable Connect button when IP (ID) is correct
        '''
        if len(self.txtIP.text()) != 8:
            self.disable_widget(self.btnConnect)
        else:
            self.enable_widget(self.btnConnect)

    def txtSendChanged(self):
        '''
        Set Maximum Char limit for QPlainTextEdit
        https://stackoverflow.com/a/46550977/5305953
        '''
        WrittenLen = len(self.txtSend.toPlainText())
        self.lblCharLeft.setText(str(500 - WrittenLen))
        if WrittenLen > 500:
            text = self.txtSend.toPlainText()
            text = text[:500]
            self.txtSend.setPlainText(text)
            cursor = self.txtSend.textCursor()
            cursor.setPosition(500)
            self.txtSend.setTextCursor(cursor)

        # Send "is typing" status to your friend
        if self.client:
            send_info(
                self.client,
                self.SERVER,
                'typing',
                self.txtName.text()
            )

    def disable_widget(self, *widgets):
        for widget in widgets:
            widget.setEnabled(False)
    
    def enable_widget(self, *widgets):
        for widget in widgets:
            widget.setEnabled(True)

    def connect(self):
        self.SERVER = (id2ip(self.txtIP.text()), self.PORT)

        self.client = Server(self.HOST, self.PORT)
        self.client.start()
        
        self.MsgThread_Starter()
        self.OnlineBroadcastThread_Starter()

        self.disable_widget(self.btnConnect, self.txtIP)
        self.enable_widget(self.grpChat, self.btnDisconnect)

    def disconnect(self):
        self.SERVER = None

        self.online_broadcast_thread.disconnected = True
        self.msg_thread.disconnected = True
        self.client.stop()

        self.disable_widget(self.grpChat, self.btnDisconnect)
        self.enable_widget(self.btnConnect, self.txtIP)
    
    def send(self):
        text = self.txtSend.toPlainText()
        text = '\n'.join(i for i in text.split('\n') if i.strip())
        if not text:
            return
        
        dct = send_msg(
            self.client,
            self.SERVER,
            text,
            self.txtName.text()
        )
        self.add_msg_to_chat(dct)

        # Clear Msg Text Box after send and scroll to bottom
        self.txtSend.setPlainText('')
        self.lstChat.scrollToBottom()
    
    def MsgThread_Starter(self):
        self.msg_thread.__init__()
        self.msg_thread.latest_msg.connect(self.MsgThread_Reciever)
        self.msg_thread.typing_status.connect(self.Status_Reciever)
        self.msg_thread.online_status.connect(self.Online_Reciever)
        self.msg_thread.client = self.client
        self.msg_thread.start()

    def MsgThread_Reciever(self, last_msg):
        self.add_msg_to_chat(last_msg, False)
        self.lstChat.scrollToBottom()

    def OnlineBroadcastThread_Starter(self):
        self.online_broadcast_thread.__init__()
        self.online_broadcast_thread.client = self.client
        self.online_broadcast_thread.server = self.SERVER
        self.online_broadcast_thread.name = self.txtName.text()
        self.online_broadcast_thread.start()

    def Status_Reciever(self, args):
        text, color = args
        self.lblStatus.setText(f"<font color='{color}'>{text}</font>")
    
    def Online_Reciever(self, args):
        text, color = args
        self.lblOnline.setText(f"<font color='{color}'>{text}</font>")
