# buttons.py (G)
from PySide6.QtWidgets import (QPushButton, QGridLayout)
from variables import var_medium_font_size
from utils import (func_isempty, func_isnumordot, func_isvalidnumber)
from display import cls_display
from PySide6.QtCore import Slot

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from display import cls_display
    from label import cls_info

class cls_button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mtd_configstyle()
    
    def mtd_configstyle(self):
        self.setStyleSheet(f'font-size:{var_medium_font_size}px;')
        self.setMinimumSize(50, 30)
        self.setCheckable(False)

class cls_buttonsgrid(QGridLayout):
    def __init__(self, display: cls_display, info: 'cls_info', *args, **kwargs) -> None:
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
        # self.var_info.setText('kkk') # main, label, button. ;-)
        self._equation = ''
        self._left = None
        self._right = None
        self._operator = None
        self._mtd_makegrid()

    @property #getter
    def mtd_equation(self):
        return self._equation
    
    @mtd_equation.setter
    def mtd_equation(self, value):
        self._equation = value
        self.var_info.setText(value)
    
    def _mtd_makegrid(self):
        for i, j in enumerate(self._var_gridmask):
          for i2, j2 in enumerate(j):
              var_button = cls_button(j2)
              #if j2 not in '0123456789.':
              if not func_isnumordot(j2) and not func_isempty(j2):
                  var_button.setProperty('cssClass', 'specialButton')
                  self._mtd_configspecialbutton(var_button)   
              self.addWidget(var_button, i, i2)

              var_slot = self._mtd_makeslot(self._mtd_insertbuttontextdisplay, var_button)
              self._mtd_connectbuttonclicked(var_button, var_slot)
            #   var_button.clicked.connect(var_slot)

    def _mtd_connectbuttonclicked(self, button, slot):
        button.clicked.connect(slot)
    
    def _mtd_configspecialbutton(self, button):
        var_text = button.text()
        
        if var_text == ('C'):
            var_slot = self._mtd_makeslot(self._mtd_clear, 'Clean.')
            self._mtd_connectbuttonclicked(button, var_slot)
            # button.clicked.connect(self.var_display.clear)

        if var_text in ('+-/*'):
            self._mtd_connectbuttonclicked(button, self._mtd_makeslot(self._mtd_operatorclicked, button))
    
    def _mtd_makeslot(self, method, *args, **kwargs):
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

    def _mtd_clear(self, msg):
        print(msg)
        self.var_display.clear()
    
    def _mtd_operatorclicked(self, button):
        var_buttontext2 = button.text()
        var_displaytext = self.var_display.text()
        self.var_display.clear()
        print(var_buttontext2)
