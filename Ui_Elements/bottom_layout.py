from Ui_Elements.Utils import WidgetUtils
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget


class BottomLayout:
    def __init__(self):
        self.utils = WidgetUtils()

    def create_buttons(self) -> QPushButton:
        run_button = self.utils.create_button("Run", True)
        cancel_button = self.utils.create_button("Cancel", True)
        return run_button, cancel_button
    
    def set_button_functions(self, run_button: QPushButton, cancel_button: QPushButton, main_window: QWidget):
        run_button.clicked.connect(lambda: self.run_button_clicked())
        cancel_button.clicked.connect(lambda: self.cancel_button_clicked(main_window))

    def run_button_clicked(self):
        pass

    def cancel_button_clicked(self, main_window: QWidget):
        main_window.close()
        
    def create_layout_and_add_all(self, main_window: QWidget) -> QHBoxLayout:
        run_button, cancel_button = self.create_buttons()
        self.set_button_functions(run_button, cancel_button, main_window)
        layout = self.utils.create_hbox_layout(run_button, cancel_button)
        return layout
