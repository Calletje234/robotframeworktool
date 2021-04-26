from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import calendar
import sys


class AdvancedWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Advanced Options")

        ### Creating all the variables of the class
        # Create Boxes
        self.main_frame = QVBoxLayout()
        self.plan_box = QGridLayout()
        self.button_bottum = QHBoxLayout()

        self.text_box_label = QLabel("Type time in format '00:00:00'")

        # Create CheckBox
        self.plan_run = QCheckBox("Plan a run")

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

        self.plan_date_entry.setDateTime(QtCore.QDateTime.currentDateTime())

        self.plan_run_check = 0

        self.plan_run.toggled.connect(self.update_plan_run)
        self.cancel_button.clicked.connect(self.close)
        self.save_button.clicked.connect(self.save_date_time)

        main_frame = self.init_items_to_frames()
        self.setLayout(main_frame)

    ### Start of the methods in the class
    def save_date_time(self):
        self.time = self.plan_time.text()
        self.date = QLocale(QLocale.English, QLocale.UnitedStates).toString(self.plan_date_entry.date(), "dd-MM-yyyy")

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
        self.button_bottum.addWidget(self.save_button)
        self.button_bottum.addWidget(self.cancel_button)

        self.main_frame.addLayout(self.plan_box)
        self.main_frame.addLayout(self.button_bottum)

        return self.main_frame

    def get_time_date(self):
        time = self.set_time
        date = self.set_date
        return time, date


class RobotTool(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Robotool")

        ### Creating All Variables for class
        # Create Boxes
        self.main_frame = QVBoxLayout()
        self.path_box = QGridLayout()
        self.option_box = QGridLayout()
        self.command_output_box = QHBoxLayout()
        self.bottum_box = QHBoxLayout()

        # Create Buttons
        self.path_python_button = QPushButton("...")
        self.path_robot_button = QPushButton("...")

        self.cancel_button = QPushButton("Cancel")
        self.run_button = QPushButton("Run")
        self.advanced_button = QPushButton("Advanced Options")

        # Create Entries
        self.python_path_entrie = QLineEdit()
        self.robot_path_entrie = QLineEdit()
        self.tst_inc_entrie = QLineEdit()
        self.tst_exc_entrie = QLineEdit()
        self.tag_inc_entrie = QLineEdit()
        self.tag_exc_entrie = QLineEdit()
        self.suite_inc_entrie = QLineEdit()
        self.suite_exc_entrie = QLineEdit()
        self.command_output_entrie = QLineEdit()

        # Create Checkboxes
        self.tst_check = QCheckBox("Test")
        self.tst_inc_check = QCheckBox("Include")
        self.tst_exc_check = QCheckBox("Exclude")
        self.tag_check = QCheckBox("Tag")
        self.tag_inc_check = QCheckBox("Include")
        self.tag_exc_check = QCheckBox("Exclude")
        self.suite_check = QCheckBox("Suite")
        self.suite_inc_check = QCheckBox("Include")
        self.suite_exc_check = QCheckBox("Exclude")

        # Set Place holders for path
        self.python_path_entrie.setPlaceholderText("C:\\Python37\\python.exe")
        self.robot_path_entrie.setPlaceholderText("C:\\ws\\cmge.automation\\RobotFrameworkCMGE")

        # Set States and Logic Behind buttons
        self.check_tst_toggle = 0
        self.check_tst_inc_toggle = 0
        self.check_tst_exc_toggle = 0
        self.check_tag_toggle = 0
        self.check_tag_inc_toggle = 0
        self.check_tag_exc_toggle = 0
        self.check_suite_toggle = 0
        self.check_suite_inc_toggle = 0
        self.check_suite_exc_toggle = 0

        self.tst_inc_check.setEnabled(False)
        self.tst_inc_entrie.setEnabled(False)
        self.tst_exc_check.setEnabled(False)
        self.tst_exc_entrie.setEnabled(False)
        self.tag_inc_check.setEnabled(False)
        self.tag_inc_entrie.setEnabled(False)
        self.tag_exc_check.setEnabled(False)
        self.tag_exc_entrie.setEnabled(False)
        self.suite_inc_check.setEnabled(False)
        self.suite_inc_entrie.setEnabled(False)
        self.suite_exc_check.setEnabled(False)
        self.suite_exc_entrie.setEnabled(False)

        self.tst_check.toggled.connect(self.update_tst_button)
        self.tst_inc_check.toggled.connect(self.update_tst_inc_entrie)
        self.tst_exc_check.toggled.connect(self.update_tst_exc_entrie)
        self.tag_check.toggled.connect(self.update_tag_button)
        self.tag_inc_check.toggled.connect(self.update_tag_inc_entrie)
        self.tag_exc_check.toggled.connect(self.update_tag_exc_entrie)
        # self.suite_check.toggled.connect(self.update_button("suite"))
        # self.suite_inc_check.toggled.connect(self.update_button("suite_inc"))
        # self.suite_exc_check.toggled.connect(self.update_button("suite_exc"))

        self.path_python_button.clicked.connect(self.open_file_selector)
        self.path_robot_button.clicked.connect(self.open_dir_selector)
        self.advanced_button.clicked.connect(self.open_new_window)
        self.cancel_button.clicked.connect(self.close)

        self.setGeometry(300, 300, 650, 750)
        main_frame = self.init_items_to_frame(self.main_frame)
        self.setLayout(main_frame)

    ### Start of the Methods inside the class
    def open_new_window(self):
        self.advanced = AdvancedWindow()
        self.advanced.show()

    def open_dir_selector(self):
        dir_selector = QFileDialog.getExistingDirectory(caption="Select RobotFrameWork Dir")
        self.robot_path_entrie.setText(dir_selector)

    def open_file_selector(self):
        file_selector = QFileDialog.getOpenFileUrl(caption="Path to python.exe", filter="Executable (*.exe)")
        file_selector = str(file_selector).strip("(PyQt5.QtCore.QUrl('file:///")
        file_selector = str(file_selector).strip("'), 'Executable (*.exe)')")
        file_selector = str(file_selector) + ".exe"
        self.python_path_entrie.setText(str(file_selector))

    def update_tag_button(self):
        if self.check_tag_toggle == 0:
            self.tag_inc_check.setEnabled(True)
            self.tag_exc_check.setEnabled(True)
            self.check_tag_toggle = 1
        elif self.check_tag_toggle == 1:
            if self.check_tag_inc_toggle == 1 and self.check_tag_exc_toggle == 1:
                self.tag_inc_check.toggle()
                self.tag_exc_check.toggle()
            elif self.check_tag_inc_toggle == 1:
                self.tag_inc_check.toggle()
            elif self.check_tag_exc_toggle == 1:
                self.tag_exc_check.toggle()
            else:
                pass

            self.tag_inc_check.setEnabled(False)
            self.tag_exc_check.setEnabled(False)
            self.check_tag_toggle = 0

    def update_tag_inc_entrie(self):
        if self.check_tag_inc_toggle == 0:
            self.tag_inc_entrie.setEnabled(True)
            self.check_tag_inc_toggle = 1
        elif self.check_tag_inc_toggle == 1:
            self.tag_inc_entrie.setEnabled(False)
            self.check_tag_inc_toggle = 0

    def update_tag_exc_entrie(self):
        if self.check_tag_exc_toggle == 0:
            self.tag_exc_entrie.setEnabled(True)
            self.check_tag_exc_toggle = 1
        elif self.check_tag_exc_toggle == 1:
            self.tag_exc_entrie.setEnabled(False)
            self.check_tag_exc_toggle = 0

    def update_tst_inc_entrie(self):
        if self.check_tst_inc_toggle == 0:
            self.tst_inc_entrie.setEnabled(True)
            self.check_tst_inc_toggle = 1
        elif self.check_tst_inc_toggle == 1:
            self.tst_inc_entrie.setEnabled(False)
            self.check_tst_inc_toggle = 0

    def update_tst_exc_entrie(self):
        if self.check_tst_exc_toggle == 0:
            self.tst_exc_entrie.setEnabled(True)
            self.check_tst_exc_toggle = 1
        elif self.check_tst_exc_toggle == 1:
            self.tst_exc_entrie.setEnabled(False)
            self.check_tst_exc_toggle = 0

    def update_tst_button(self):
        if self.check_tst_toggle == 0:
            self.tst_inc_check.setEnabled(True)
            self.tst_exc_check.setEnabled(True)
            self.check_tst_toggle = 1
        elif self.check_tst_toggle == 1:
            if self.check_tst_inc_toggle == 1 and self.check_tst_exc_toggle == 1:
                self.tst_inc_check.toggle()
                self.tst_exc_check.toggle()
            elif self.check_tst_inc_toggle == 1:
                self.tst_inc_check.toggle()
            elif self.check_tst_exc_toggle == 1:
                self.tst_exc_check.toggle()
            else:
                pass
            self.tst_inc_check.setEnabled(False)
            self.tst_exc_check.setEnabled(False)
            self.check_tst_toggle = 0

    def init_items_to_frame(self, main_frame):
        self.path_box.addWidget(self.python_path_entrie, 0, 0)
        self.path_box.addWidget(self.path_python_button, 0, 1)
        self.path_box.addWidget(self.robot_path_entrie, 1, 0)
        self.path_box.addWidget(self.path_robot_button, 1, 1)
        option_box = self.set_option_box()
        self.command_output_box.addWidget(self.command_output_entrie)
        self.bottum_box.addWidget(self.cancel_button)
        self.bottum_box.addWidget(self.run_button)
        self.bottum_box.addWidget(self.advanced_button)

        self.main_frame.addLayout(self.path_box)
        self.main_frame.addLayout(self.path_box)
        self.main_frame.addLayout(option_box)
        self.main_frame.addLayout(self.command_output_box)
        self.main_frame.addLayout(self.bottum_box)

        return self.main_frame

    def set_option_box(self):
        self.option_box.addWidget(self.tst_check, 0, 0)
        self.option_box.addWidget(self.tst_inc_check, 1, 1)
        self.option_box.addWidget(self.tst_inc_entrie, 1, 2)
        self.option_box.addWidget(self.tst_exc_check, 2, 1)
        self.option_box.addWidget(self.tst_exc_entrie, 2, 2)

        self.option_box.addWidget(self.tag_check, 3, 0)
        self.option_box.addWidget(self.tag_inc_check, 4, 1)
        self.option_box.addWidget(self.tag_inc_entrie, 4, 2)
        self.option_box.addWidget(self.tag_exc_check, 5, 1)
        self.option_box.addWidget(self.tag_exc_entrie, 5, 2)

        self.option_box.addWidget(self.suite_check, 6, 0)
        self.option_box.addWidget(self.suite_inc_check, 7, 1)
        self.option_box.addWidget(self.suite_inc_entrie, 7, 2)
        self.option_box.addWidget(self.suite_exc_check, 8, 1)
        self.option_box.addWidget(self.suite_exc_entrie, 8, 2)

        return self.option_box

    def get_all_options(self):
        tst_inc, tst_exc = self.get_tst_options
        tag_inc, tag_exc = self.get_tag_options
        suite_inc, suite_exc = self.get_suite_options
        return tst_inc, tst_exc, tag_inc, tag_exc, suite_inc, suite_exc

    def get_suite_options(self):
        if self.check_suite_toggle == 1 and self.check_suite_inc_toggle == 1 and self.check_suite_exc_toggle == 1:
            suite_inc = self.suite_inc_entrie.text()
            suite_exc = self.suite_exc_entrie.text()
            return suite_inc, suite_exc
        elif self.check_suite_toggle == 1 and self.check_suite_inc_toggle == 1:
            suite_inc = self.suite_inc_entrie.text()
            return suite_inc
        elif self.check_suite_toggle == 1 and self.check_suite_exc_toggle == 1:
            suite_exc = self.suite_exc_entrie.text()
            return suite_exc

    def get_tag_options(self):
        if self.check_tag_toggle == 1 and self.check_tag_inc_toggle == 1 and self.check_tag_exc_toggle == 1:
            tag_inc = self.tag_inc_entrie.text()
            tag_exc = self.tag_exc_entrie.text()
            return tag_inc, tag_exc
        elif self.check_tag_toggle == 1 and self.check_tag_inc_toggle == 1:
            tag_inc = self.tag_inc_entrie.text()
            return tag_inc
        elif self.check_tag_toggle == 1 and self.check_tag_exc_toggle == 1:
            tag_exc = self.tag_exc_entrie.text()
            return tag_exc

    def get_tst_options(self):
        if self.check_tst_toggle == 1 and self.check_tst_inc_toggle == 1 and self.check_tst_exc_toggle == 1:
            tst_inc = self.tst_inc_entrie.text()
            tst_exc = self.tst_exc_entrie.text()
            return tst_inc, tst_exc
        elif self.check_tst_toggle == 1 and self.check_tst_inc_toggle == 1:
            tst_inc = self.tst_inc_entrie.text()
            return tst_inc
        elif self.check_tst_toggle == 1 and self.check_tst_exc_toggle == 1:
            tst_exc = self.tst_exc_entrie.text()
            return tst_exc


class create_command:
    def __init__(self, ui):
        self.screen = ui


    def create_command(self):
        self.get_options()

    def get_python_path(self):
        pass

    def get_robot_path(self):
        pass

    def get_advanced_options(self):
        pass

    def get_options(self):
        tst_inc, tst_exc, tag_inc, tag_exc, suite_inc, suite_exc = self.screen.get_all_options()

app = QApplication(sys.argv)
dialog = RobotTool()
dialog.show()
app.exec_()



