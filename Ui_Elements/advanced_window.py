from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets


class AdvancedWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Advanced Options")
        self.window = QVBoxLayout()
        self.button = QHBoxLayout()
        self.planner = QVBoxLayout()

        # Create Buttons
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(lambda: self.save_button_clicked())

        # Create CheckBox
        self.plan_checkbox_state = 0
        self.planning_checkbox = QCheckBox("Plan a Run")
        self.planning_checkbox.toggled.connect(lambda: self.planner_checkbox_checked())

        # Create Date Planner
        self.date_edit = QtWidgets.QDateEdit(calendarPopup=True)
        self.date_edit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.date_edit.setEnabled(False)
        self.text = ""

        self.create_layout()
        self.add_items_to_screen()
        self.setLayout(self.window)

    def create_layout(self):
        self.button.addWidget(self.save_button)
        self.planner.addWidget(self.planning_checkbox)
        self.planner.addWidget(self.date_edit)

    def add_items_to_screen(self):
        self.window.addLayout(self.planner)
        self.window.addLayout(self.button)

    def planner_checkbox_checked(self):
        if self.plan_checkbox_state == 0:
            self.date_edit.setEnabled(True)
            self.plan_checkbox_state = 1
        else:
            self.date_edit.setEnabled(False)
            self.plan_checkbox_state = 0

    def save_button_clicked(self):
        self.text = self.date_edit.text()

    def get_date(self):
        if self.date_edit.text() == QtCore.QDateTime.currentDateTime():
            return self.date_edit.text()
        else:
            return self.text
