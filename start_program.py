from Ui_Elements.bottom_layout import BottomLayout
from Ui_Elements.middel_layout import MiddleLayout
from Ui_Elements.top_box import TopBox
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

def create_window() -> QWidget:
    window = QWidget()
    layout = QVBoxLayout()
    layout.addLayout(get_top_layout())
    layout.addLayout(get_middle_layout())
    layout.addLayout(get_bottom_layout(window))
    window.setLayout(layout)
    window.setFixedSize(500, 300)
    return window

def get_top_layout() -> QVBoxLayout:
    return TopBox().create_layout_and_add_all()

def get_middle_layout() -> QVBoxLayout:
    return MiddleLayout().create_layout_and_add_all()

def get_bottom_layout(main_window: QWidget) -> QVBoxLayout:
    return BottomLayout().create_layout_and_add_all(main_window)

if __name__ == "__main__":
    app = QApplication([])
    window = create_window()
    window.show()
    app.exec_()
