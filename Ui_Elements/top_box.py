from Ui_Elements.Utils import WidgetUtils
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout


class TopBox:
    def __init__(self) -> None:
        self.utils = WidgetUtils()

    def create_labels(self) -> QLabel:
        path_label = self.utils.create_label("Robot testfile: ")
        output_label = self.utils.create_label("Output: ")
        return path_label, output_label
    
    def create_entries(self) -> QLineEdit:
        path_entry = self.utils.create_line_edit("Enter path to robottest files", True)
        output_entry = self.utils.create_line_edit("Enter path to output folder", True)
        return path_entry, output_entry
    
    def create_buttons(self) -> QPushButton:
        path_point_button = self.utils.create_button("...", True)
        output_point_button = self.utils.create_button("...", True)
        return path_point_button, output_point_button
    
    def create_layout_and_add_all(self) -> QVBoxLayout:
        path_label, output_label = self.create_labels()
        path_entry, output_entry = self.create_entries()
        path_point_button, output_point_button = self.create_buttons()
        path_horizontal_layout = self.utils.create_hbox_layout(path_label, path_entry, path_point_button)
        path_output_layout = self.utils.create_hbox_layout(output_label, output_entry, output_point_button)
        layout = self.utils.create_vbox_layout(path_horizontal_layout, path_output_layout)
        return layout