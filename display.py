#display.py (D)
from PySide6.QtWidgets import QLineEdit
from variables import (var_big_font_size, var_text_margin, var_minimum_width)
from PySide6.QtCore import (Qt, Signal)
from PySide6.QtGui import QKeyEvent

from typing import TYPE_CHECKING # Just test.
if TYPE_CHECKING:
    from buttons import cls_button
var_button: 'cls_button'

class cls_display(QLineEdit):
    var_eqrequested = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mtd_configstyle()

    def mtd_configstyle(self):
        self.setStyleSheet(f'font-size: {var_big_font_size}px;')
        self.setMinimumHeight(var_big_font_size * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        var_margins = []
        for _ in range(4):
            var_margins.append(var_text_margin)
        self.setTextMargins(var_margins[0], var_margins[1], var_margins[2], var_margins[3])
        # var_margins = [var_text_margin for _ in range(4)]
        # self.setTextMargins(*var_margins)
        self.setMinimumWidth(var_minimum_width)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        var_key = event.key()
        var_keysqt = Qt.Key
        var_isenter = (var_key == var_keysqt.Key_Enter) or (var_key == var_keysqt.Key_Return)

        if var_isenter:
            print('Enter button.', type(self).__name__)
            self.var_eqrequested.emit()
            return event.ignore
        # return super().keyPressEvent(event)
