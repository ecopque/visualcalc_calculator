# buttons.py (G)
from PySide6.QtWidgets import (QPushButton, QGridLayout)
from variables import var_medium_font_size
from utils import (func_isempty, func_isnumordot, func_isvalidnumber)
from display import cls_display
from PySide6.QtCore import Slot
import math

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from display import cls_display
    from label import cls_info
    from main_window import cls_mainwindow

class cls_button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mtd_configstyle()
    
    def mtd_configstyle(self):
        self.setStyleSheet(f'font-size:{var_medium_font_size}px;')
        self.setMinimumSize(50, 30)
        self.setCheckable(False)

class cls_buttonsgrid(QGridLayout):
    def __init__(self, display: cls_display, info: 'cls_info', window: 'cls_mainwindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._var_gridmask = [
            ['C', '◀', '^', '/'], #◀ <-
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.var_display = display
        self.var_info = info
        self.var_window = window
        # self.var_info.setText('kkk') # main, label, button. ;-)
        self._var_equation = ''
        self._var_equationinitial = 'Your account'
        self._var_left = None
        self._var_right = None
        self._var_operator = None

        self.mtd_equation = self._var_equationinitial
        self._mtd_makegrid()

    @property #getter
    def mtd_equation(self):
        return self._var_equation
    
    @mtd_equation.setter
    def mtd_equation(self, value):
        self._var_equation = value
        self.var_info.setText(value)
    
    def _mtd_makegrid(self):
        self.var_display.var_eqrequested.connect(lambda: print('Signal received.', type(self).__name__))

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
        
        if var_text in ('C'):
            var_slot = self._mtd_makeslot(self._mtd_clear, 'Clean.')
            self._mtd_connectbuttonclicked(button, var_slot)
            # button.clicked.connect(self.var_display.clear)
        
        if var_text in ('◀'):
            self._mtd_connectbuttonclicked(button, self.var_display.backspace)

        if var_text in ('+-/*^'):
            self._mtd_connectbuttonclicked(button, self._mtd_makeslot(self._mtd_operatorclicked, button))

        if var_text in ('='):
            self._mtd_connectbuttonclicked(button, self._mtd_equal)


    
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
        self._var_left = None
        self._var_right = None
        self._var_operator = None
        self.mtd_equation = self._var_equationinitial
        self.var_display.clear()
        # self.var_info.setText(self.equation)
    
    def _mtd_operatorclicked(self, button):
        var_buttontext = button.text()
        var_displaytext = self.var_display.text()
        self.var_display.clear()

        # If you click on the operator without any number.
        if not func_isvalidnumber(var_displaytext) and self._var_left is None:
            self._mtd_showerror("You didn't type anything.")
            return
        
        # If there is a number on the left, we do nothing. We are waiting for the number on the right
        if self._var_left is None:
            self._var_left = float(var_displaytext)
        self._var_operator = var_buttontext
        self.mtd_equation = f'{self._var_left} {self._var_operator} ???'

        print(var_buttontext)

    def _mtd_equal(self):
        var_displaytext = self.var_display.text()

        if not func_isvalidnumber(var_displaytext):
            self._mtd_showerror('Incomplete account.')
            return
        
        self._var_right = float(var_displaytext)
        self.mtd_equation = f'{self._var_left} {self._var_operator} {self._var_right}'
        # self._var_left: float #AAA
        var_result: str | float = 'Error'
        try:
            if '^' in self.mtd_equation and isinstance(self._var_left, float):
                var_result = eval(self.mtd_equation.replace('^', '**'))
                # var_result = math.pow(self._var_left, self._var_right) #AAA
            else:
                var_result = eval(self.mtd_equation)
        except ZeroDivisionError:
            self._mtd_showerror('Division by zero.')
        except OverflowError:
            self._mtd_showerror('Overflow: gigantic number.')
        
        self.var_display.clear()
        self.var_info.setText(f'{self.mtd_equation} = {var_result}')
        self._var_left = var_result
        self._var_right = None
        
        if var_result == 'Error':
            self._var_left = None

    def _mtd_makedialog(self, text):
        var_msgbox = self.var_window.mtd_makemsgbox()
        var_msgbox.setText(text)
        return var_msgbox
    
    def _mtd_showerror(self, text):
        var_msgbox = self._mtd_makedialog(text)
        var_msgbox.setIcon(var_msgbox.Icon.Warning)
        var_msgbox.setStandardButtons(var_msgbox.StandardButton.Ok | var_msgbox.StandardButton.Cancel)
        var_msgbox.button(var_msgbox.StandardButton.Cancel).setText('Calcelll')
        
        var_result = var_msgbox.exec()
        if var_result == var_msgbox.StandardButton.Ok:
            print('Clicked ok')
        elif var_result == var_msgbox.StandardButton.Cancel:
            print('Clicked cancel')
        # var_msgbox.exec()

    def _mtd_showinfo(self, text):
        var_msgbox = self._mtd_makedialog(text)
        var_msgbox.setIcon(var_msgbox.Icon.Information)
       
        var_msgbox.exec()
