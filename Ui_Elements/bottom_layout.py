from Ui_Elements.Utils import WidgetUtils
from PyQt5.QtWidgets import QPushButton, QHBoxLayout


class BottomLayout:
    def __init__(self):
        self.utils = WidgetUtils()

    def create_buttons(self) -> QPushButton:
        run_button = self.utils.create_button("Run", True)
        cancel_button = self.utils.create_button("Cancel", True)
        return run_button, cancel_button

    def create_layout_and_add_all(self) -> QHBoxLayout:
        run_button, cancel_button = self.create_buttons()
        layout = self.utils.create_hbox_layout(run_button, cancel_button)
        return layout
