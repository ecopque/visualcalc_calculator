# buttons.py (G)
from PySide6.QtWidgets import QPushButton, QGridLayout

from variables import var_medium_font_size

class cls_button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mtd_configstyle()
    
    def mtd_configstyle(self):
        self.setStyleSheet(f'font-size:{var_medium_font_size}px;')
        self.setMinimumSize(50, 30)

class cls_buttonsgrid(QGridLayout):
    ...
