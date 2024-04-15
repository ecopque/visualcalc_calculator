# main_window.py
import sys
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout)

class My_MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Set the basic layout
        self.my_centralwidget = QWidget()
        self.my_verticallayout = QVBoxLayout()

        self.my_centralwidget.setLayout(self.my_verticallayout)
        self.setCentralWidget(self.my_centralwidget)

        # Window title
        self.setWindowTitle('New Calculator - Edson Copque® | linktr.ee/edsoncopque')

    # Last step
    def my_adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def my_addWidgetToVerticalLayout(self, widget: QWidget):
        self.my_verticallayout.addWidget(widget)
        # self.my_adjustFixedSize() #B1:

#B1: Read A1.
