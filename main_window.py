import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QWidget,
                               QVBoxLayout,
                               QLabel)

class My_MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.my_centralwidget = QWidget()
        self.my_verticallayout = QVBoxLayout()


        self.my_centralwidget.setLayout(self.my_verticallayout)

        self.setCentralWidget(self.my_centralwidget)
