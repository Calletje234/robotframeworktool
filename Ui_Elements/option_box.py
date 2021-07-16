from PyQt5.QtWidgets import *


class OptionBox(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Create Box
        self.option_box = QGridLayout()

        # Create Entry
        self.tst_inc_entry = QLineEdit()
        # self.tst_exc_entry = QLineEdit()
        self.tag_inc_entry = QLineEdit()
        self.tag_exc_entry = QLineEdit()
        self.suite_inc_entry = QLineEdit()
        # self.suite_exc_entry = QLineEdit()

        # Create Checkboxes
        self.tst = QCheckBox("Test")
        self.tst_inc = QCheckBox("Name of Test")
        # self.tst_exc = QCheckBox("Exclude")
        self.tag = QCheckBox("Tag")
        self.tag_inc = QCheckBox("Include")
        self.tag_exc = QCheckBox("Exclude")
        self.suite = QCheckBox("Suite")
        self.suite_inc = QCheckBox("Name of Suite")
        # self.suite_exc = QCheckBox("Exclude")

        # Init Checks for toogling
        self.check_tst = 0
        self.check_tst_inc = 0
        # self.check_tst_exc = 0
        self.check_tag = 0
        self.check_tag_inc = 0
        self.check_tag_exc = 0
        self.check_suite = 0
        self.check_suite_inc = 0
        # self.check_suite_exc = 0

        # Set Initial State
        self.tst_inc.setEnabled(False)
        # self.tst_exc.setEnabled(False)
        self.tst_inc_entry.setEnabled(False)
        # self.tst_exc_entry.setEnabled(False)
        self.tag_inc.setEnabled(False)
        self.tag_exc.setEnabled(False)
        self.tag_inc_entry.setEnabled(False)
        self.tag_exc_entry.setEnabled(False)
        self.suite_inc.setEnabled(False)
        # self.suite_exc.setEnabled(False)
        self.suite_inc_entry.setEnabled(False)
        # self.suite_exc_entry.setEnabled(False)

        self.add_item_to_frame()
        self.set_checkbox_fuction()

    def add_item_to_frame(self):
        self.option_box.addWidget(self.tst, 0, 0)
        self.option_box.addWidget(self.tst_inc, 1, 1)
        # self.option_box.addWidget(self.tst_exc, 2, 1)
        self.option_box.addWidget(self.tag, 3, 0)
        self.option_box.addWidget(self.tag_inc, 4, 1)
        self.option_box.addWidget(self.tag_exc, 5, 1)
        self.option_box.addWidget(self.suite, 6, 0)
        self.option_box.addWidget(self.suite_inc, 7, 1)
        # self.option_box.addWidget(self.suite_exc, 8, 1)
        self.option_box.addWidget(self.tst_inc_entry, 1, 2)
        # self.option_box.addWidget(self.tst_exc_entry, 2, 2)
        self.option_box.addWidget(self.tag_inc_entry, 4, 2)
        self.option_box.addWidget(self.tag_exc_entry, 5, 2)
        self.option_box.addWidget(self.suite_inc_entry, 7, 2)
        # self.option_box.addWidget(self.suite_exc_entry, 8, 2)

    def set_checkbox_fuction(self):
        self.tst.toggled.connect(lambda: self.update_tst_button())
        self.tst_inc.toggled.connect(lambda: self.update_tst_inc_entrie())
        # self.tst_exc.toggled.connect(lambda: self.update_tst_exc_entrie())
        self.tag.toggled.connect(lambda: self.update_tag_button())
        self.tag_inc.toggled.connect(lambda: self.update_tag_inc_entrie())
        self.tag_exc.toggled.connect(lambda: self.update_tag_exc_entrie())
        self.suite.toggled.connect(lambda: self.update_suite_button())
        self.suite_inc.toggled.connect(lambda: self.update_suite_inc_entrie())
        # self.suite_exc.toggled.connect(lambda: self.update_suite_exc_entrie())

    def update_tag_button(self):
        if self.check_tag == 0:
            self.tag_inc.setEnabled(True)
            self.tag_exc.setEnabled(True)
            self.check_tag = 1
        elif self.check_tag == 1:
            if self.check_tag_inc == 1 and self.check_tag_exc == 1:
                self.tag_inc.toggle()
                self.tag_exc.toggle()
            elif self.check_tag_inc == 1:
                self.tag_inc.toggle()
            elif self.check_tag_exc == 1:
                self.tag_exc.toggle()
            else:
                pass

            self.tag_inc.setEnabled(False)
            self.tag_exc.setEnabled(False)
            self.check_tag = 0

    def update_tag_inc_entrie(self):
        if self.check_tag_inc == 0:
            self.tag_inc_entry.setEnabled(True)
            self.check_tag_inc = 1
        elif self.check_tag_inc == 1:
            self.tag_inc_entry.setEnabled(False)
            self.check_tag_inc = 0

    def update_tag_exc_entrie(self):
        if self.check_tag_exc == 0:
            self.tag_exc_entry.setEnabled(True)
            self.check_tag_exc = 1
        elif self.check_tag_exc == 1:
            self.tag_exc_entry.setEnabled(False)
            self.check_tag_exc = 0

    def update_tst_inc_entrie(self):
        if self.check_tst_inc == 0:
            self.tst_inc_entry.setEnabled(True)
            self.check_tst_inc = 1
        elif self.check_tst_inc == 1:
            self.tst_inc_entry.setEnabled(False)
            self.check_tst_inc = 0

    # def update_tst_exc_entrie(self):
    #     if self.check_tst_exc == 0:
    #         self.tst_exc_entry.setEnabled(True)
    #         self.check_tst_exc = 1
    #     elif self.check_tst_exc == 1:
    #         self.tst_exc_entry.setEnabled(False)
    #         self.check_tst_exc = 0

    def update_tst_button(self):
        if self.check_tst == 0:
            self.tst_inc.setEnabled(True)
            self.check_tst = 1
        elif self.check_tst == 1:
            if self.check_tst_inc == 1:
                self.tst_inc.toggle()
            else:
                pass
            self.tst_inc.setEnabled(False)
            self.check_tst = 0

    def update_suite_button(self):
        if self.check_suite == 0:
            self.suite_inc.setEnabled(True)
            self.check_suite = 1
        elif self.check_suite == 1:
            if self.check_suite_inc == 1:
                self.suite_inc.toggle()
            else:
                pass
            self.suite_inc.setEnabled(False)
            self.check_suite = 0

    def update_suite_inc_entrie(self):
        if self.check_suite_inc == 0:
            self.suite_inc_entry.setEnabled(True)
            self.check_suite_inc = 1
        else:
            self.suite_inc_entry.setEnabled(False)
            self.check_suite_inc = 0

    # def update_suite_exc_entrie(self):
    #     if self.check_suite_exc == 0:
    #         self.suite_exc_entry.setEnabled(True)
    #         self.check_suite_exc = 1
    #     else:
    #         self.suite_exc_entry.setEnabled(False)
    #         self.check_suite_exc = 0

    def get_tst_inc_entry(self):
        if self.check_tst_inc == 0:
            return 0
        else:
            return self.tst_inc_entry.text()

    # def get_tst_exc_entry(self):
    #     if self.check_tst_exc == 0:
    #         return 0
    #     else:
    #         return self.tst_exc_entry.text()

    def get_tag_inc_entry(self):
        if self.check_tag_inc == 0:
            return 0
        else:
            return self.tag_inc_entry.text()

    def get_tag_exc_entry(self):
        if self.check_tag_exc == 0:
            return 0
        else:
            return self.tag_exc_entry.text()

    def get_suite_inc_entry(self):
        if self.check_suite_inc == 0:
            return 0
        else:
            return self.suite_inc_entry.text()

    # def get_suite_exc_entry(self):
    #     if self.check_suite_exc == 0:
    #         return 0
    #     else:
    #         return self.suite_exc_entry.text()

    def return_options_box(self):
        return self.option_box
