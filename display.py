#display.py (D)
from PySide6.QtWidgets import QLineEdit #1:
from variables import (var_big_font_size, var_text_margin, var_minimum_width) #2:
from PySide6.QtCore import (Qt, Signal) #3: #4:
from PySide6.QtGui import QKeyEvent #5:
from utils import (func_isempty, func_isnumordot) #6:

from typing import TYPE_CHECKING #7:
if TYPE_CHECKING:
    from buttons import cls_button
var_button: 'cls_button'

class cls_display(QLineEdit): #8:
    var_enterpressed = Signal() #9:
    var_backspacedeletepressed = Signal() #9:
    var_scapepressed = Signal() #9:
    var_inputpressed = Signal(str) #9:
    var_operatorpressed = Signal(str) #9:

    def __init__(self, *args, **kwargs): #10:
        super().__init__(*args, **kwargs) #10:
        self.mtd_configstyle() #10:

    def mtd_configstyle(self): #11:
        self.setStyleSheet(f'font-size: {var_big_font_size}px;') #11:
        self.setMinimumHeight(var_big_font_size * 2) #11:
        self.setAlignment(Qt.AlignmentFlag.AlignRight) #11:

        var_margins = [] #12:
        for _ in range(4): #12:
            var_margins.append(var_text_margin) #12:
        self.setTextMargins(var_margins[0], var_margins[1], var_margins[2], var_margins[3]) #12:
        self.setMinimumWidth(var_minimum_width) #13:

    def keyPressEvent(self, event: QKeyEvent) -> None: #14:
        var_text = event.text().strip() #15:
        var_key = event.key() #15:
        var_keysqt = Qt.Key #15:
        
        var_isenter = (var_key == var_keysqt.Key_Enter) or (var_key == var_keysqt.Key_Return) or (var_key == var_keysqt.Key_Equal) #16:

        var_isbackspacedelete = (var_key == var_keysqt.Key_Backspace) or (var_key == var_keysqt.Key_Delete) or (var_key == var_keysqt.Key_D) #17:
        
        var_isescape = (event.key() == Qt.Key.Key_Escape) or (var_key == var_keysqt.Key_C) #18:

        var_isoperator = (var_key == var_keysqt.Key_Plus) or (var_key == var_keysqt.Key_Minus) or (var_key == var_keysqt.Key_Slash) or (var_key == var_keysqt.Key_Asterisk) or (var_key == var_keysqt.Key_P) #19:

        if var_isenter or var_text == ('='): #20:
            print(f'var_isenter: Enter or "=" button.', type(self).__name__) #21:
            self.var_enterpressed.emit() #22:
            return event.ignore() #23:

        if var_isbackspacedelete:
            print('var_isbackspacedelete: Backspace button.', type(self).__name__)
            self.var_backspacedeletepressed.emit()
            return event.ignore()

        if var_isescape or var_text.lower() == ('c'):
            print('var_isescape: Escape or "C/c" button.', type(self).__name__)
            self.var_scapepressed.emit()
            return event.ignore()
        
        if var_isoperator:
            print('var_isoperator: Operators button.', type(self).__name__)
            if var_text.lower() == ('p'):
                var_text = ('^')
            self.var_operatorpressed.emit(var_text)
            return event.ignore()

        if func_isempty(var_text): #24:
            return event.ignore() #24:
        print('Text', var_text)

        if func_isnumordot(var_text): #25:
            print('varInputPressed', type(self).__name__) #25:
            self.var_inputpressed.emit(var_text) #25:
            return event.ignore() #25:
