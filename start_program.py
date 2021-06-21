import sys
from PyQt5.QtWidgets import QApplication
from main_screen import MainScreen


def start():
    UI = MainScreen()
    UI.show()
    return  UI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = start()
    app.exec_()
