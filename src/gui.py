# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kelmo\Desktop\OLD DESKTOP\-Python\CODE\ChatCat\exe\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 694)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.grpConfig = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpConfig.sizePolicy().hasHeightForWidth())
        self.grpConfig.setSizePolicy(sizePolicy)
        self.grpConfig.setMinimumSize(QtCore.QSize(0, 243))
        self.grpConfig.setMaximumSize(QtCore.QSize(16777215, 234))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.grpConfig.setFont(font)
        self.grpConfig.setObjectName("grpConfig")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.grpConfig)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnConnect = QtWidgets.QPushButton(self.grpConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConnect.sizePolicy().hasHeightForWidth())
        self.btnConnect.setSizePolicy(sizePolicy)
        self.btnConnect.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnConnect.setFont(font)
        self.btnConnect.setObjectName("btnConnect")
        self.gridLayout_2.addWidget(self.btnConnect, 2, 2, 1, 1)
        self.btnDisconnect = QtWidgets.QPushButton(self.grpConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDisconnect.sizePolicy().hasHeightForWidth())
        self.btnDisconnect.setSizePolicy(sizePolicy)
        self.btnDisconnect.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnDisconnect.setFont(font)
        self.btnDisconnect.setObjectName("btnDisconnect")
        self.gridLayout_2.addWidget(self.btnDisconnect, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.grpConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.grpConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(131, 206))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)
        self.txtName = QtWidgets.QLineEdit(self.grpConfig)
        self.txtName.setMinimumSize(QtCore.QSize(0, 36))
        self.txtName.setMaximumSize(QtCore.QSize(16777215, 215))
        self.txtName.setObjectName("txtName")
        self.gridLayout_2.addWidget(self.txtName, 0, 2, 1, 1)
        self.txtIP = QtWidgets.QLineEdit(self.grpConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtIP.sizePolicy().hasHeightForWidth())
        self.txtIP.setSizePolicy(sizePolicy)
        self.txtIP.setMinimumSize(QtCore.QSize(0, 36))
        self.txtIP.setMaximumSize(QtCore.QSize(16777215, 211))
        self.txtIP.setInputMask("")
        self.txtIP.setText("")
        self.txtIP.setObjectName("txtIP")
        self.gridLayout_2.addWidget(self.txtIP, 1, 2, 1, 1)
        self.lblIP = QtWidgets.QLabel(self.grpConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIP.sizePolicy().hasHeightForWidth())
        self.lblIP.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblIP.setFont(font)
        self.lblIP.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIP.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblIP.setObjectName("lblIP")
        self.gridLayout_2.addWidget(self.lblIP, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.grpConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 206))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout.addWidget(self.grpConfig, 0, 0, 1, 1)
        self.grpChat = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.grpChat.setFont(font)
        self.grpChat.setObjectName("grpChat")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.grpChat)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnSend = QtWidgets.QPushButton(self.grpChat)
        self.btnSend.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSend.setFont(font)
        self.btnSend.setObjectName("btnSend")
        self.gridLayout_3.addWidget(self.btnSend, 2, 1, 1, 1)
        self.lblCharLeft = QtWidgets.QLabel(self.grpChat)
        self.lblCharLeft.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCharLeft.setObjectName("lblCharLeft")
        self.gridLayout_3.addWidget(self.lblCharLeft, 3, 1, 1, 1)
        self.lstChat = QtWidgets.QListWidget(self.grpChat)
        self.lstChat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lstChat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lstChat.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.lstChat.setTextElideMode(QtCore.Qt.ElideNone)
        self.lstChat.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.lstChat.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.lstChat.setMovement(QtWidgets.QListView.Static)
        self.lstChat.setFlow(QtWidgets.QListView.TopToBottom)
        self.lstChat.setProperty("isWrapping", False)
        self.lstChat.setResizeMode(QtWidgets.QListView.Fixed)
        self.lstChat.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.lstChat.setViewMode(QtWidgets.QListView.ListMode)
        self.lstChat.setWordWrap(True)
        self.lstChat.setSelectionRectVisible(False)
        self.lstChat.setObjectName("lstChat")
        self.gridLayout_3.addWidget(self.lstChat, 0, 0, 1, 2)
        self.txtSend = QtWidgets.QPlainTextEdit(self.grpChat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtSend.sizePolicy().hasHeightForWidth())
        self.txtSend.setSizePolicy(sizePolicy)
        self.txtSend.setMinimumSize(QtCore.QSize(566, 80))
        self.txtSend.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txtSend.setFont(font)
        self.txtSend.setPlainText("")
        self.txtSend.setObjectName("txtSend")
        self.gridLayout_3.addWidget(self.txtSend, 2, 0, 2, 1)
        self.lblStatus = QtWidgets.QLabel(self.grpChat)
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout_3.addWidget(self.lblStatus, 4, 0, 1, 1)
        self.lblOnline = QtWidgets.QLabel(self.grpChat)
        self.lblOnline.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOnline.setObjectName("lblOnline")
        self.gridLayout_3.addWidget(self.lblOnline, 4, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.gridLayout.addWidget(self.grpChat, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatCat"))
        self.grpConfig.setTitle(_translate("MainWindow", "Configuration"))
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.btnDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.label_2.setText(_translate("MainWindow", "Your ID:"))
        self.label.setText(_translate("MainWindow", "SERVER ID:"))
        self.txtName.setPlaceholderText(_translate("MainWindow", "Default is: Anonymous"))
        self.txtIP.setPlaceholderText(_translate("MainWindow", "ID Example: AF EC 1D 05"))
        self.lblIP.setText(_translate("MainWindow", "00000000"))
        self.label_3.setText(_translate("MainWindow", "Your Name:"))
        self.grpChat.setTitle(_translate("MainWindow", "Chat"))
        self.btnSend.setText(_translate("MainWindow", "Send"))
        self.lblCharLeft.setText(_translate("MainWindow", "500"))
        self.txtSend.setPlaceholderText(_translate("MainWindow", "Type Here..."))
        self.lblStatus.setText(_translate("MainWindow", "STATUS"))
        self.lblOnline.setText(_translate("MainWindow", "Offline"))
