# buttons.py (G)
from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import var_medium_font_size
from utils import func_isempty, func_isnumordot, func_isvalidnumber
from display import cls_display
from PySide6.QtCore import Slot


class cls_button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mtd_configstyle()
    
    def mtd_configstyle(self):
        self.setStyleSheet(f'font-size:{var_medium_font_size}px;')
        self.setMinimumSize(50, 30)
        self.setCheckable(False)

class cls_buttonsgrid(QGridLayout):
    def __init__(self, display: cls_display, info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._var_gridmask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.var_display = display
        self.var_info = info
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
    
    def _mtd_makebuttondisplayslot(self, method, *args, **kwargs):
        @Slot(bool)
        def mtd_realslot(_):
            method(*args, **kwargs)
        return mtd_realslot

    def _mtd_insertbuttontextdisplay(self, button):
        var_buttontext = button.text()
        var_newdisplayvalue = self.var_display.text() + var_buttontext
        
        if not func_isvalidnumber(var_newdisplayvalue):
            return 
        self.var_display.insert(var_buttontext)
