# main_window.py (B)
import sys
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QMessageBox)

class cls_mainwindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Set the basic layout
        self.var_centralwidget = QWidget()
        self.var_verticallayout = QVBoxLayout()

        self.var_centralwidget.setLayout(self.var_verticallayout)
        self.setCentralWidget(self.var_centralwidget)

        # Window title
        self.setWindowTitle('[beta] Graphic Calculator | eCop PI[A}')

    # Last step
    def mtd_adjustfixedsize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def mtd_addwidgettoverticallayout(self, widget: QWidget):
        self.var_verticallayout.addWidget(widget)
        # self.my_adjustFixedSize() #B1:

    def mtd_setupmenu(self):
        var_menu = self.menuBar()
        first_menu = var_menu.addMenu('File')
        first_option =  first_menu.addAction('Open')

    def mtd_makemsgbox(self):
        return QMessageBox(self)

#B1: Read A1.
