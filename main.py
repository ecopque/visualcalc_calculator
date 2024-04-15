import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QWidget,
                               QVBoxLayout,
                               QLabel)
from main_window import My_MainWindow

if __name__ == '__main__':
    my_app = QApplication(sys.argv)

    my_window = QMainWindow()
    my_centralwidget = QWidget()
    my_verticallayout = QVBoxLayout()

    my_label = QLabel('My little text.')

    my_centralwidget.setLayout(my_verticallayout)
    my_verticallayout.addWidget(my_label)
    my_window.setCentralWidget(my_centralwidget)
    my_window.show()

    my_app.exec()
