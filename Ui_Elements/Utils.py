from PyQt5.QtWidgets import QCheckBox, QPushButton, QLineEdit, QVBoxLayout, QLabel, QHBoxLayout



class WidgetUtils:
    def create_button(self, button_name: str, isEnabled: bool) -> QPushButton:
        button = QPushButton(button_name)
        button.setEnabled(isEnabled)
        return button
    
    def create_checkbox(self, checkbox_name: str, isEnabled: bool, isChecked: bool) -> QCheckBox:
        checkbox = QCheckBox(checkbox_name)
        checkbox.setChecked(isChecked)
        checkbox.setEnabled(isEnabled)
        return checkbox
    
    def create_line_edit(self, placeholder: str, isEnabled: bool) -> QLineEdit:
        entry = QLineEdit()
        entry.setPlaceholderText(placeholder)
        entry.setEnabled(isEnabled)
        return entry
    
    def create_label(self, label_name: str) -> QLabel:
        label = QLabel(label_name)
        return label
    
    def create_vbox_layout(self, *items_to_add) -> QVBoxLayout:
        layout = QVBoxLayout()
        for item in items_to_add:
            if type(item) == QHBoxLayout or type(item) == QVBoxLayout:
                layout.addLayout(item)
            else:
                layout.addWidget(item)
        return layout
    
    def create_hbox_layout(self, *items_to_add) -> QHBoxLayout:
        layout = QHBoxLayout()
        for item in items_to_add:
            if type(item) == QHBoxLayout or type(item) == QVBoxLayout:
                layout.addLayout(item)
            else:
                layout.addWidget(item)
        return layout