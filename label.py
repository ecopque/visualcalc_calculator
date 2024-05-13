# label.py (E)
from PySide6.QtWidgets import (QLabel, QWidget)
# from typing import Optional
from variables import var_small_font_size
from PySide6.QtCore import Qt

class cls_info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
                 super().__init__(text, parent)
                 self.mtd_configstyle()
    
    def mtd_configstyle(self):
            self.setStyleSheet(f'font-size: {var_small_font_size}px;')
            self.setAlignment(Qt.AlignmentFlag.AlignRight)
