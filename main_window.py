# main_window.py (B)
import sys
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout)

class cls_mainwindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Set the basic layout
        self.var_centralwidget = QWidget()
        self.var_verticallayout = QVBoxLayout()

        self.var_centralwidget.setLayout(self.var_verticallayout)
        self.setCentralWidget(self.var_centralwidget)

        # Window title
        self.setWindowTitle('New Monkey Calculator')

    # Last step
    def mtd_adjustfixedsize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def mtd_addwidgettoverticallayout(self, widget: QWidget):
        self.var_verticallayout.addWidget(widget)
        # self.my_adjustFixedSize() #B1:

#B1: Read A1.
