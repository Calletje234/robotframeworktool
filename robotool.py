from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class RobotTool(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        windowtitle = "Robotool"

        # Create Boxes
        self.main_frame = QVBoxLayout()
        self.path_box_python = QHBoxLayout()
        self.path_box_robot = QHBoxLayout()
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

        # Init Frames
        main_frame = self.init_items_to_frame(self.main_frame)
        self.setLayout(main_frame)

    def init_items_to_frame(self, main_frame):
        self.path_box_python.addWidget(self.python_path_entrie)
        self.path_box_python.addWidget(self.path_python_button)
        self.path_box_robot.addWidget(self.robot_path_entrie)
        self.path_box_robot.addWidget(self.path_robot_button)
        option_box = self.set_option_box()
        self.command_output_box.addWidget(self.command_output_entrie)
        self.bottum_box.addWidget(self.cancel_button)
        self.bottum_box.addWidget(self.run_button)
        self.bottum_box.addWidget(self.advanced_button)

        self.main_frame.addLayout(self.path_box_python)
        self.main_frame.addLayout(self.path_box_robot)
        self.main_frame.addLayout(option_box)
        self.main_frame.addLayout(self.command_output_box)
        self.main_frame.addLayout(self.bottum_box)

        return self.main_frame

    def set_option_box(self):
        self.option_box.addWidget(self.tst_check)
        self.option_box.addWidget(self.tst_inc_check)
        self.option_box.addWidget(self.tst_inc_entrie)
        self.option_box.addWidget(self.tst_exc_check)
        self.option_box.addWidget(self.tst_exc_entrie)

        self.option_box.addWidget(self.tag_check)
        self.option_box.addWidget(self.tag_inc_check)
        self.option_box.addWidget(self.tag_inc_entrie)
        self.option_box.addWidget(self.tag_exc_check)
        self.option_box.addWidget(self.tag_exc_entrie)

        self.option_box.addWidget(self.suite_check)
        self.option_box.addWidget(self.suite_inc_check)
        self.option_box.addWidget(self.suite_inc_entrie)
        self.option_box.addWidget(self.suite_exc_check)
        self.option_box.addWidget(self.suite_exc_entrie)

        return self.option_box




app = QApplication(sys.argv)
dialog = RobotTool()
dialog.show()
app.exec_()
