import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QWidget,
                               QVBoxLayout,
                               QLabel)

class My_MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)