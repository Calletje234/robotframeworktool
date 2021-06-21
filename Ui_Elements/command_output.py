from PyQt5.QtWidgets import *


class CommandBox:
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

    def set_command_output(self, output_text):
        self.command_output_entry.setText(output_text)
