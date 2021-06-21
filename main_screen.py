from PyQt5.QtWidgets import *
from Ui_Elements.advanced_window import AdvancedWindow
from Ui_Elements.command_output import CommandBox
from Ui_Elements.option_box import OptionBox
from Ui_Elements.path_box import PathBox
from command_constructor import CommandConstruct


class MainScreen(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Robo Tool")

        # Create Layouts
        self.main_frame = QVBoxLayout()
        self.bottum_buttons = QHBoxLayout()

        # Get UI Elements
        self.path_ui = PathBox()
        self.option_ui = OptionBox()
        self.command_ui = CommandBox()
        self.advanced_window = AdvancedWindow()
        self.path = self.path_ui.return_path_box()
        self.option_box = self.option_ui.return_options_box()
        self.command_output = self.command_ui.return_command_box()

        # Create Buttons
        self.advanced_button = QPushButton("Advanced")
        self.cancel_button = QPushButton("Cancel")
        self.run_button = QPushButton("Run")

        # Add Function To Buttons
        self.advanced_button.clicked.connect(lambda: self.advanced_button_clicked())
        self.cancel_button.clicked.connect(lambda: self.cancel_button_clicked())
        self.run_button.clicked.connect(lambda: self.run_button_clicked())

        self.add_buttons_to_layout()
        self.setLayout(self.add_item_to_frame())
        self.setGeometry(300, 400, 650, 750)

    def add_buttons_to_layout(self):
        self.bottum_buttons.addWidget(self.advanced_button)
        self.bottum_buttons.addWidget(self.cancel_button)
        self.bottum_buttons.addWidget(self.run_button)

    def add_item_to_frame(self):
        self.main_frame.addLayout(self.path)
        self.main_frame.addLayout(self.option_box)
        self.main_frame.addLayout(self.command_output)
        self.main_frame.addLayout(self.bottum_buttons)
        return self.main_frame

    def advanced_button_clicked(self):
        self.advanced_window.show()

    def cancel_button_clicked(self):
        self.main_frame.close()
        self.advanced_window.close()

    def run_button_clicked(self):
        python_path = self.path_ui.get_python_path()
        robot_path = self.path_ui.get_robot_path()
        output_path = self.path_ui.get_output_dir_path()
        planner_date = self.advanced_window.get_date()
        tst_inc = self.option_ui.get_tst_inc_entry()
        tst_exc = self.option_ui.get_tst_exc_entry()
        tag_inc = self.option_ui.get_tag_inc_entry()
        tag_exc = self.option_ui.get_tag_exc_entry()
        suite_inc = self.option_ui.get_suite_inc_entry()
        suite_exc = self.option_ui.get_suite_exc_entry()
        command = CommandConstruct(python_path, robot_path, output_path, planner_date, tst_inc, tst_exc, tag_inc,
                                   tag_exc, suite_inc, suite_exc)
        text = command.construct_command()
        self.command_ui.set_command_output(text)