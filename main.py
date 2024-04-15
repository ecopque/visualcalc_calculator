import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QWidget,
                               QVBoxLayout,
                               QLabel)
from main_window import My_MainWindow

if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    my_window = My_MainWindow()
    
    my_label = QLabel('My little text.')
    my_label.setStyleSheet('font-size: 50px;')
    my_window.my_verticallayout.addWidget(my_label)

    my_window.show()
    my_app.exec()
