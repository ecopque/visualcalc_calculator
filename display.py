#display.py (D)
from PySide6.QtWidgets import QLineEdit
from variables import var_big_font_size
from PySide6.QtCore import Qt

class cls_display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mtd_configstyle()

    def mtd_configstyle(self):
        self.setStyleSheet(f'font-size: {var_big_font_size}px;')
        self.setMinimumHeight(var_big_font_size * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)