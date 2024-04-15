# main.py (A)
import sys
from PySide6.QtWidgets import (QApplication, QLabel)
from main_window import cls_mainwindow

from PySide6.QtGui import QIcon
from variables import PATH_WINDOW_ICON_PATH

if __name__ == '__main__':
    # Create the application:
    var_app = QApplication(sys.argv)
    var_window = cls_mainwindow()
    
    #
    var_label = QLabel('My little text.')
    var_label.setStyleSheet('font-size: 50px;')

    var_window.mtd_addwidgettoverticallayout(var_label)
    var_window.mtd_adjustfixedsize() #A1:

    # Defining icon
    var_icon = QIcon(str(PATH_WINDOW_ICON_PATH))
    var_window.setWindowIcon(var_icon)
    var_app.setWindowIcon(var_icon)

    # Runs everything
    var_window.show()
    var_app.exec()

#A1: We could put it inside #B1 / def my_addWidgetToVerticalLayout.
