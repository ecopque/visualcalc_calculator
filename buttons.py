# buttons.py (G)
from PySide6.QtWidgets import QPushButton, QGridLayout

from variables import var_medium_font_size

from utils import func_isempty, func_isnumordot

from display import cls_display

class cls_button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mtd_configstyle()
    
    def mtd_configstyle(self):
        self.setStyleSheet(f'font-size:{var_medium_font_size}px;')
        self.setMinimumSize(50, 30)

class cls_buttonsgrid(QGridLayout):
    def __init__(self, display: cls_display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._var_gridmask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.var_display = display
        self._mtd_makegrid()
    
    def _mtd_makegrid(self):
        for i, j in enumerate(self._var_gridmask):
          for i2, j2 in enumerate(j):
              var_button = cls_button(j2)
              #if j2 not in '0123456789.':
              if not func_isnumordot(j2) and not func_isempty(j2):
                  var_button.setProperty('cssClass', 'specialButton')     
              self.addWidget(var_button, i, i2)

              var_buttonslot = self._mtd_makebuttondisplayslot(
                  self._mtd_insertbuttontextdisplay,
                  var_button,
                  )
              var_button.clicked.connect(var_buttonslot)
    
    def _mtd_makebuttondisplayslot(self, x, *args, **kwargs):
        def mtd_realslot():
            x(*args, **kwargs)
        return mtd_realslot

    def _mtd_insertbuttontextdisplay(self, button):
        self.var_display.setText('Clicked')
        print(123, button.text())
