from Ui_Elements import option_box
from Ui_Elements import path_box
from Ui_Elements import bottum_buttons
from Ui_Elements import command_output
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import calendar
import sys


class main_screen(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Robo Tool")
        self.main_frame = QVBoxLayout()

        # Get UI Elements
        path_ui = path_box.path_box()
        option_ui = option_box.option_box()
        command_ui = command_output.command_box()
        self.bottom_buttons = bottum_buttons.bottum_buttons()

        self.path = path_ui.return_path_box()
        self.option_box = option_ui.return_options_box()
        self.command_output = command_ui.return_command_box()

        self.setLayout(self.add_item_to_frame(self.main_frame))
        self.setGeometry(300,400,650,750)

    def add_item_to_frame(self, main_frame):
        main_frame.addLayout(self.path)
        main_frame.addLayout(self.option_box)
        main_frame.addLayout(self.command_output)
        main_frame.addWidget(self.bottom_buttons)
        return main_frame


app = QApplication(sys.argv)
dialog = main_screen()
dialog.show()
app.exec_()
