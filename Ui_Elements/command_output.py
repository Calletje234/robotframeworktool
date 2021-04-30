from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import calendar
import sys

class command_box:
    def __init__(self):
        # Create Box
        self.command_output_box = QHBoxLayout()

        # Create Entry
        self.command_output_entry = QTextEdit()

        self.add_item_to_layout()

    def add_item_to_layout(self):
        self.command_output_box.addWidget(self.command_output_entry)

    def return_command_box(self):
        return self.command_output_box