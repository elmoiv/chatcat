from PyQt5.QtWidgets import QApplication
from sys import argv, exit
from main import ChatCat

if __name__ == "__main__":
    app = QApplication(argv)
    GUI = ChatCat()
    GUI.show()
    exit(app.exec_())