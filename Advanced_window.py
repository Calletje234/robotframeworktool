from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import calendar
import sys


class AdvancedWindows(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Advanced Options")

        ### Creating all the variables of the class
        # Create Boxes
        self.main_frame = QVBoxLayout()
        self.plan_box = QGridLayout()
        self.environment = QHBoxLayout()
        self.button_bottum = QHBoxLayout()

        # Create Labels
        self.text_box_label = QLabel("Type time in format '00:00:00'")

        # Create CheckBox
        self.plan_run = QCheckBox("Plan a run")
        self.env_var = QCheckBox("Add Environment Variable Files")

        # Create Entries
        self.env_var_entry = QLineEdit()

        # Create Button
        self.start_date_widget = QPushButton("...")
        self.cancel_button = QPushButton("Cancel")
        self.save_button = QPushButton("Save")

        # Create Time Planner
        self.plan_time = QLineEdit()
        self.plan_date_entry = QDateEdit()

        # Create setters for time and date
        self.time = 0
        self.date = "Default"

        # Set States and Logic
        self.plan_time.setEnabled(False)
        self.plan_date_entry.setEnabled(False)
        self.start_date_widget.setEnabled(False)
        self.env_var_entry.setEnabled(False)

        self.env_var_entry.setPlaceholderText("Name of File")

        self.plan_date_entry.setDateTime(QtCore.QDateTime.currentDateTime())

        self.plan_run_check = 0
        self.env_var_check = 0

        self.plan_run.toggled.connect(self.update_plan_run)
        self.cancel_button.clicked.connect(self.close)
        self.save_button.clicked.connect(self.save_date_time)
        self.env_var.toggled.connect(self.update_env_var)

        self.setLayout(self.main_frame)
        self.show()

        ### Start of the methods in the class

    def save_date_time(self):
        self.time = self.plan_time.text()
        self.date = QLocale(QLocale.English, QLocale.UnitedStates).toString(self.plan_date_entry.date(), "dd-MM-yyyy")

    def update_env_var(self):
        if self.env_var_check == 0:
            self.env_var_entry.setEnabled(True)
            self.env_var_check = 1
        else:
            self.env_var_entry.setEnabled(False)
            self.env_var_check = 0

    def update_plan_run(self):
        if self.plan_run_check == 0:
            self.plan_date_entry.setEnabled(True)
            self.plan_time.setEnabled(True)
            self.plan_run_check = 1
        else:
            self.plan_date_entry.setEnabled(False)
            self.plan_time.setEnabled(False)
            self.plan_run_check = 0

    def init_items_to_frames(self):
        self.plan_box.addWidget(self.plan_run, 0, 0)
        self.plan_box.addWidget(self.plan_date_entry, 1, 0)
        self.plan_box.addWidget(self.start_date_widget, 1, 1)
        self.plan_box.addWidget(self.plan_time, 1, 2)
        self.plan_box.addWidget(self.text_box_label, 0, 2)
        self.environment.addWidget(self.env_var)
        self.environment.addWidget(self.env_var_entry)
        self.button_bottum.addWidget(self.save_button)
        self.button_bottum.addWidget(self.cancel_button)

        self.main_frame.addLayout(self.plan_box)
        self.main_frame.addLayout(self.environment)
        self.main_frame.addLayout(self.button_bottum)

        return self.main_frame

    def get_time_date(self):
        time = self.set_time
        date = self.set_date
        return time, date

