from Ui_Elements.Utils import WidgetUtils
from Ui_Elements.Utils import StringUtils
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog


class TopBox:
    def __init__(self) -> None:
        self.utils = WidgetUtils()
        self.string_utils = StringUtils()

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
    
    def set_function_for_buttons(self, path_button: QPushButton, output_button: QPushButton, path_entry: QLineEdit, output_entry: QLineEdit):
        path_button.clicked.connect(lambda: self.open_file_picker(path_button, path_entry))
        output_button.clicked.connect(lambda: self.open_file_picker(output_button, output_entry))
    
    def open_file_picker(self, button: QPushButton, entry: QLineEdit):
        path = QFileDialog.getExistingDirectoryUrl()
        stripped_path = self.string_utils.get_only_path(path.toString())
        entry.setText(stripped_path)
    
    def create_layout_and_add_all(self) -> QVBoxLayout:
        path_label, output_label = self.create_labels()
        path_entry, output_entry = self.create_entries()
        path_point_button, output_point_button = self.create_buttons()
        self.set_function_for_buttons(path_point_button, output_point_button, path_entry, output_entry)
        path_horizontal_layout = self.utils.create_hbox_layout(path_label, path_entry, path_point_button)
        path_output_layout = self.utils.create_hbox_layout(output_label, output_entry, output_point_button)
        layout = self.utils.create_vbox_layout(path_horizontal_layout, path_output_layout)
        return layout