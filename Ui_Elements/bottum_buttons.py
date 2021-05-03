import Advanced_window
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import calendar
import sys

class bottum_buttons(QWidget):
    def __init__(self, path_object, option_object, command_ui):
        QWidget.__init__(self)

        self.path_ui = path_object
        self.option_ui = option_object
        self.command_ui = command_ui

        # Create Objects
        self.advanced_window = Advanced_window.AdvancedWindows()

        # Create Layout
        self.bottom_box = QHBoxLayout()

        # Creating Buttons
        self.cancel_button = QPushButton("Cancel")
        self.run_button = QPushButton("Run")
        self.advanced_button = QPushButton("Advancend Options")

        self.add_items_to_layout()
        self.create_button_functions()

        self.setLayout(self.bottom_box)

    def add_items_to_layout(self):
        self.bottom_box.addWidget(self.cancel_button)
        self.bottom_box.addWidget(self.run_button)
        self.bottom_box.addWidget(self.advanced_button)

    def create_button_functions(self):
        self.cancel_button.clicked.connect(lambda: self.window().close())
        # self.advanced_button.clicked.connect(lambda: Advanced_window.AdvancedWindows())
        self.run_button.clicked.connect(lambda: self.get_items())

    def get_items(self):
        robot_path = self.path_ui.get_robot_path()
        python_path = self.path_ui.get_python_path()
        output_path = self.path_ui.get_output_dir_path()
        print()

    def return_bottom_buttons(self):
        return self.bottom_box
