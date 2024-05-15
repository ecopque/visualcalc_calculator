# main_window.py (B)
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QMessageBox) #1:

class cls_mainwindow(QMainWindow): #2:
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None: #3:
        super().__init__(parent, *args, **kwargs) #4:

        self.var_centralwidget = QWidget() #5:
        self.var_verticallayout = QVBoxLayout() #5:
        self.var_centralwidget.setLayout(self.var_verticallayout) #6:
        self.setCentralWidget(self.var_centralwidget) #6:

        self.setWindowTitle('VisualCalc Calculator (beta)') #7:

    def mtd_adjustfixedsize(self): #8:
        self.adjustSize() #9:
        self.setFixedSize(self.width(), self.height()) #10:

    def mtd_addwidgettoverticallayout(self, widget: QWidget): #11:
        self.var_verticallayout.addWidget(widget) #12:

    def mtd_setupmenu(self): #13:
        var_menu = self.menuBar() #14:
        first_menu = var_menu.addMenu('File') #15:
        first_option =  first_menu.addAction('Open') #16:

    def mtd_makemsgbox(self): #17:
        return QMessageBox(self) #18:
