# label.py (D)
from PySide6.QtWidgets import QLabel, QWidget
from typing import Optional

class cls_info(QLabel):
    def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
                 super().__init__(text, parent)
