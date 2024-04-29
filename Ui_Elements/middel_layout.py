from Ui_Elements.Utils import WidgetUtils
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QCheckBox


class MiddleLayout:
    def __init__(self) -> None:
        self.utils = WidgetUtils()

    def create_checkboxes(self) -> QCheckBox:
        tag_checkbox = self.utils.create_checkbox("Tag", True, False)
        include_checkbox = self.utils.create_checkbox("Include: ", False, False)
        exclude_checkbox = self.utils.create_checkbox("Exclude: ", False, False)
        specific_test_checkbox = self.utils.create_checkbox("Specific test: ", True, False)
        return tag_checkbox, include_checkbox, exclude_checkbox, specific_test_checkbox
    
    def create_entries(self) -> QLineEdit:
        include_entry = self.utils.create_line_edit("Enter include tag", False)
        exclude_entry = self.utils.create_line_edit("Enter exclude tag", False)
        specific_test_entry = self.utils.create_line_edit("Enter specific test", False)
        return include_entry, exclude_entry, specific_test_entry
    
    def setup_main_checkbox(self, main_checkbox: QCheckBox, child_checkbox: QCheckBox):
        if main_checkbox.isChecked():
            child_checkbox.setEnabled(True)
        else:
            child_checkbox.setEnabled(False)
            child_checkbox.setChecked(False)

    def setup_checkbox_with_entries(self, checkbox: QCheckBox, entry: QLineEdit):
        if checkbox.isChecked():
            entry.setEnabled(True)
        else:
            entry.setEnabled(False)
            entry.clear()

    def setup_functions(self, tag_checkbox: QCheckBox, include_checkbox: QCheckBox, exclude_checkbox: QCheckBox, specific_test_checkbox: QCheckBox, include_entry: QLineEdit, exclude_entry: QLineEdit, specific_test_entry: QLineEdit):
        tag_checkbox.stateChanged.connect(lambda: self.setup_main_checkbox(tag_checkbox, include_checkbox))
        tag_checkbox.stateChanged.connect(lambda: self.setup_main_checkbox(tag_checkbox, exclude_checkbox))

        include_checkbox.stateChanged.connect(lambda: self.setup_checkbox_with_entries(include_checkbox, include_entry))
        exclude_checkbox.stateChanged.connect(lambda: self.setup_checkbox_with_entries(exclude_checkbox, exclude_entry))

        specific_test_checkbox.stateChanged.connect(lambda: self.setup_checkbox_with_entries(specific_test_checkbox, specific_test_entry))

    def create_layout_and_add_all(self) -> QVBoxLayout:
        tag_checkbox, include_checkbox, exclude_checkbox, specific_test_checkbox = self.create_checkboxes()
        include_entry, exclude_entry, specific_test_entry = self.create_entries()
        self.setup_functions(tag_checkbox, include_checkbox, exclude_checkbox, specific_test_checkbox, include_entry, exclude_entry, specific_test_entry)
        tag_horizontal_layout = self.utils.create_hbox_layout(tag_checkbox)
        include_horizontal_layout = self.utils.create_hbox_layout(include_checkbox, include_entry)
        exclude_horizontal_layout = self.utils.create_hbox_layout(exclude_checkbox, exclude_entry)
        specific_test_horizontal_layout = self.utils.create_hbox_layout(specific_test_checkbox, specific_test_entry)
        layout = self.utils.create_vbox_layout(tag_horizontal_layout, include_horizontal_layout, exclude_horizontal_layout, specific_test_horizontal_layout)
        return layout

        
