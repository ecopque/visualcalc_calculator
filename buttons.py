# buttons.py (G)
from PySide6.QtWidgets import (QPushButton, QGridLayout) #1:
from variables import var_medium_font_size #2:
from utils import (func_isempty, func_isnumordot, func_isvalidnumber, func_converttointorfloat) #3:
from display import cls_display #4:
from PySide6.QtCore import Slot #5:

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
            ['C', '◀', '^', '/'],
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
              self.addWidget(var_button, i, i2) #29:

              var_slot = self._mtd_makeslot(self._mtd_inserttodisplay, var_buttontext) #30:
              self._mtd_connectbuttonclicked(var_button, var_slot) #31:

    def _mtd_connectbuttonclicked(self, button, slot): #32:
        button.clicked.connect(slot) #33: #34:
    
    def _mtd_configspecialbutton(self, button): #35:
        var_text = button.text() #36:
        
        if var_text in ('C'):
            var_slot = self._mtd_makeslot(self._mtd_clear, 'Clean.') #37:
            self._mtd_connectbuttonclicked(button, var_slot) #38:
        
        if var_text in ('◀'):
            self._mtd_connectbuttonclicked(button, self.var_display.backspace) #39:

        if var_text in ('N'):
            self._mtd_connectbuttonclicked(button, self._mtd_invertnumber) #40:

        if var_text in ('+-/*^'):
            self._mtd_connectbuttonclicked(button, self._mtd_makeslot(self._mtd_configleftoperator, var_text)) #41:

        if var_text in ('='):
            self._mtd_connectbuttonclicked(button, self._mtd_equal) #42:
    
    @Slot() #43:
    def _mtd_makeslot(self, method, *args, **kwargs): #44:
        @Slot(bool)
        def mtd_realslot(_): #45:
            method(*args, **kwargs)
        return mtd_realslot

    @Slot()
    def _mtd_invertnumber(self): #46:
        var_displaytext = self.var_display.text() #47:

        if not func_isvalidnumber(var_displaytext): #48:
            return
        
        var_number = func_converttointorfloat(var_displaytext) * -1 #49:
        self.var_display.setText(str(var_number)) #50:

    @Slot()
    def _mtd_inserttodisplay(self, text): #51: #52:
        var_newdisplayvalue = self.var_display.text() + text #53:
        
        if not func_isvalidnumber(var_newdisplayvalue): #54:
            return 
        self.var_display.insert(text) #55:
        self.var_display.setFocus() #56:

    @Slot()
    def _mtd_clear(self, msg): #57: #58:
        print(msg) #59:
        self._var_left = None #60:
        self._var_right = None #60:
        self._var_operator = None #60:
        self.mtd_equation = self._var_equationinitial #61:
        self.var_display.clear() #62:
        self.var_display.setFocus() #63:
    
    @Slot()
    def _mtd_configleftoperator(self, text): #64: #65:
        var_displaytext = self.var_display.text() #66:
        self.var_display.clear() #67:
        self.var_display.setFocus() #68:

        if not func_isvalidnumber(var_displaytext) and self._var_left is None: #69:
            self._mtd_showerror("You didn't type anything.")
            return
        
        if self._var_left is None: #70:
            self._var_left = func_converttointorfloat(var_displaytext)
        self._var_operator = text #71:
        self.mtd_equation = f'{self._var_left} {self._var_operator} ???' #72:

    @Slot()
    def _mtd_equal(self): #73:
        var_displaytext = self.var_display.text() #74:

        if not func_isvalidnumber(var_displaytext) or (self._var_left is None): #75:
            self._mtd_showerror('Incomplete account.') #75:
            return
        
        self._var_right = func_converttointorfloat(var_displaytext) #76:
        self.mtd_equation = f'{self._var_left} {self._var_operator} {self._var_right}' #77:
        var_result: str | func_converttointorfloat = 'Error' #78:

        try: #79:
            if '^' in self.mtd_equation and isinstance(self._var_left, int | float):
                var_result = eval(self.mtd_equation.replace('^', '**'))
            else:
                var_result = eval(self.mtd_equation)
        except ZeroDivisionError:
            self._mtd_showerror('Division by zero.')
        except OverflowError:
            self._mtd_showerror('Overflow: gigantic number.')
        
        self.var_display.clear() #80:
        self.var_info.setText(f'{self.mtd_equation} = {var_result}') #81:
        self._var_left = var_result
        self._var_right = None
        self.var_display.setFocus()

        
        if var_result == 'Error': #82:
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
