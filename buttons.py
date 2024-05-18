# buttons.py (G)
from PySide6.QtWidgets import (QPushButton, QGridLayout) #1:
from variables import var_medium_font_size #2:
from utils import (func_isempty, func_isnumordot, func_isvalidnumber, func_converttointorfloat) #3:
from display import cls_display #4:
from PySide6.QtCore import Slot #5:
# import math

from typing import TYPE_CHECKING #6:
if TYPE_CHECKING: #6:
    from label import cls_info
    from main_window import cls_mainwindow

class cls_button(QPushButton):
    def __init__(self, *args, **kwargs): #7:
        super().__init__(*args, **kwargs)
        self.mtd_configstyle() #7:
    
    def mtd_configstyle(self): #8:
        self.setStyleSheet(f'font-size:{var_medium_font_size}px;') #9:
        self.setMinimumSize(50, 30) #10:
        self.setCheckable(False) #11:

class cls_buttonsgrid(QGridLayout):
    def __init__(self, display: cls_display, info: 'cls_info', window: 'cls_mainwindow', *args, **kwargs) -> None: #12:
        super().__init__(*args, **kwargs)

        self._var_gridmask = [
            ['C', '◀', '^', '/'], #◀ <-
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ] #13:

        self.var_display = display #14:
        self.var_info = info #14:
        self.var_window = window #14:

        self._var_equation = '' #15:
        self._var_equationinitial = 'Your account' #16:
        self._var_left = None #17:
        self._var_right = None #17:
        self._var_operator = None #18:

        self.mtd_equation = self._var_equationinitial #19:
        self._mtd_makegrid() #20:

    @property #getter
    def mtd_equation(self): #21:
        return self._var_equation
    
    @mtd_equation.setter #21:
    def mtd_equation(self, value):
        self._var_equation = value
        self.var_info.setText(value)
    
    def _mtd_makegrid(self): #22:
        self.var_display.var_enterpressed.connect(self._mtd_equal)
        self.var_display.var_backspacedeletepressed.connect(self._mtd_backspace)
        self.var_display.var_scapepressed.connect(self._mtd_clear)
        self.var_display.var_inputpressed.connect(self._mtd_inserttodisplay)
        self.var_display.var_operatorpressed.connect(self._mtd_configleftoperator)

        for i, j in enumerate(self._var_gridmask): #23: #24:
          for i2, var_buttontext in enumerate(j): #25:
              var_button = cls_button(var_buttontext)
              if not func_isnumordot(var_buttontext) and not func_isempty(var_buttontext): #26:
                  var_button.setProperty('cssClass', 'specialButton') #27:
                  self._mtd_configspecialbutton(var_button) #28:
              self.addWidget(var_button, i, i2)

              var_slot = self._mtd_makeslot(self._mtd_inserttodisplay, var_buttontext)
              self._mtd_connectbuttonclicked(var_button, var_slot)

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

        if var_text in ('N'):
            self._mtd_connectbuttonclicked(button, self._mtd_invertnumber)

        if var_text in ('+-/*^'):
            self._mtd_connectbuttonclicked(button, self._mtd_makeslot(self._mtd_configleftoperator, var_text))

        if var_text in ('='):
            self._mtd_connectbuttonclicked(button, self._mtd_equal)
    
    @Slot()
    def _mtd_makeslot(self, method, *args, **kwargs):
        @Slot(bool)
        def mtd_realslot(_):
            method(*args, **kwargs)
        return mtd_realslot

    @Slot()
    def _mtd_invertnumber(self):
        var_displaytext = self.var_display.text()

        if not func_isvalidnumber(var_displaytext):
            return
        
        var_number = func_converttointorfloat(var_displaytext) * -1
        self.var_display.setText(str(var_number))

    @Slot()
    def _mtd_inserttodisplay(self, text):
        # var_buttontext = button.text()
        var_newdisplayvalue = self.var_display.text() + text
        
        if not func_isvalidnumber(var_newdisplayvalue):
            return 
        self.var_display.insert(text)
        self.var_display.setFocus()

    @Slot()
    def _mtd_clear(self, msg):
        print(msg)
        self._var_left = None
        self._var_right = None
        self._var_operator = None
        self.mtd_equation = self._var_equationinitial
        self.var_display.clear()
        self.var_display.setFocus()
        # self.var_info.setText(self.equation)
    
    @Slot()
    def _mtd_configleftoperator(self, text):
        # var_buttontext = button.text()
        var_displaytext = self.var_display.text()
        self.var_display.clear()
        self.var_display.setFocus()

        # If you click on the operator without any number.
        if not func_isvalidnumber(var_displaytext) and self._var_left is None:
            self._mtd_showerror("You didn't type anything.")
            return
        
        # If there is a number on the left, we do nothing. We are waiting for the number on the right
        if self._var_left is None:
            self._var_left = func_converttointorfloat(var_displaytext)
        self._var_operator = text
        self.mtd_equation = f'{self._var_left} {self._var_operator} ???'

    @Slot()
    def _mtd_equal(self):
        var_displaytext = self.var_display.text()

        if not func_isvalidnumber(var_displaytext) or (self._var_left is None):
            self._mtd_showerror('Incomplete account.')
            return
        
        self._var_right = func_converttointorfloat(var_displaytext)
        self.mtd_equation = f'{self._var_left} {self._var_operator} {self._var_right}'
        # self._var_left: func_converttointorfloat #AAA
        var_result: str | func_converttointorfloat = 'Error'
        try:
            if '^' in self.mtd_equation and isinstance(self._var_left, int | float):
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
        self.var_display.setFocus()

        
        if var_result == 'Error':
            self._var_left = None

    @Slot()
    def _mtd_backspace(self):
        self.var_display.backspace()
        self.var_display.setFocus()

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
        self.var_display.setFocus()

        if var_result == var_msgbox.StandardButton.Ok:
            print('Clicked ok')
        elif var_result == var_msgbox.StandardButton.Cancel:
            print('Clicked cancel')
        # var_msgbox.exec()

    def _mtd_showinfo(self, text):
        var_msgbox = self._mtd_makedialog(text)
        var_msgbox.setIcon(var_msgbox.Icon.Information)
       
        var_msgbox.exec()
        self.var_display.setFocus()
