# label.py (E)
from PySide6.QtWidgets import (QLabel, QWidget) #1:
from variables import var_small_font_size #2:
from PySide6.QtCore import Qt #3:

class cls_info(QLabel): #4:
    def __init__(self, text: str, parent: QWidget | None = None) -> None: #5:
                 super().__init__(text, parent) #6:
                 self.mtd_configstyle()
    
    def mtd_configstyle(self): #7:
            self.setStyleSheet(f'font-size: {var_small_font_size}px;')
            self.setAlignment(Qt.AlignmentFlag.AlignRight)
