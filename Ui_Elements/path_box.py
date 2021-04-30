from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import calendar
import sys

class path_box:
    def __init__(self):

        # Create Frame
        self.path_box = QGridLayout()

        # Create Buttons
        self.python_path_button = QPushButton("...")
        self.robot_path_button = QPushButton("...")
        self.output_path_button = QPushButton("...")

        # Create Entry's
        self.python_path_entry = QLineEdit()
        self.robot_path_entry = QLineEdit()
        self.output_path_entry = QLineEdit()

        # Create Labels
        self.python_path_label = QLabel("Python")
        self.robot_path_label = QLabel("RobotFramework")
        self.output_dir_label = QLabel("Output Dir")

        self.create_placeholders()
        self.create_button_fuctions()
        self.add_item_to_layout()

    def create_placeholders(self):
        self.python_path_entry.setPlaceholderText("C:\\Python37\\python.exe")
        self.robot_path_entry.setPlaceholderText("C:\\ws\\cmge.testautomation\\RobotFrameworkCMGE")
        self.output_path_entry.setPlaceholderText("C:\\temp")

    def create_button_fuctions(self):
        self.python_path_button.clicked.connect(lambda: self.select_python_file())
        self.robot_path_button.clicked.connect(lambda: self.select_robot_dir())
        self.output_path_button.clicked.connect(lambda: self.select_output_dir())

    def select_python_file(self):
        file_selector = QFileDialog.getOpenFileUrl(caption="Path to python.exe", filter="Executable (*.exe)")
        file_selector = str(file_selector).strip("(PyQt5.QtCore.QUrl('file:///")
        file_selector = str(file_selector).strip("'), 'Executable (*.exe)')")
        file_selector = str(file_selector) + ".exe"
        self.python_path_entry.setText(str(file_selector))

    def select_robot_dir(self):
        dir_selector = QFileDialog.getExistingDirectory(caption="Select RobotFrameWork Dir")
        self.robot_path_entry.setText(dir_selector)

    def select_output_dir(self):
        dir_select = QFileDialog.getExistingDirectory(caption="Select Output Dir")
        self.output_path_entry.setText(dir_select)

    def add_item_to_layout(self):
        self.path_box.addWidget(self.python_path_label,0,0)
        self.path_box.addWidget(self.robot_path_label,1,0)
        self.path_box.addWidget(self.output_dir_label,2,0)

        self.path_box.addWidget(self.python_path_button,0,2)
        self.path_box.addWidget(self.robot_path_button,1,2)
        self.path_box.addWidget(self.output_path_button,2,2)

        self.path_box.addWidget(self.python_path_entry,0,1)
        self.path_box.addWidget(self.robot_path_entry,1,1)
        self.path_box.addWidget(self.output_path_entry,2,1)

    def return_path_box(self):
        return self.path_box