# main.py
import sys
from PySide6.QtWidgets import (QApplication, QLabel)
from main_window import My_MainWindow

from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Create the application:
    my_app = QApplication(sys.argv)
    my_window = My_MainWindow()
    
    #
    my_label = QLabel('My little text.')
    my_label.setStyleSheet('font-size: 50px;')

    my_window.my_addWidgetToVerticalLayout(my_label)
    my_window.my_adjustFixedSize() #A1:

    # Defining icon
    my_icon = QIcon(str(WINDOW_ICON_PATH))
    my_window.setWindowIcon(my_icon)
    my_app.setWindowIcon(my_icon)

    # Runs everything
    my_window.show()
    my_app.exec()

#A1: We could put it inside #B1 / def my_addWidgetToVerticalLayout.
