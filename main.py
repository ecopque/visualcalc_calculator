# main.py (A)
import sys
from PySide6.QtWidgets import (QApplication, QLabel)
from main_window import cls_mainwindow
from PySide6.QtGui import QIcon
from variables import PATH_WINDOW_ICON_PATH
from display import cls_display
from label import cls_info
from styles import func_setuptheme
from buttons import (cls_buttonsgrid)

if __name__ == '__main__':
    # Create the application:
    var_app = QApplication(sys.argv)
    var_window = cls_mainwindow()
    
    # styles.py
    func_setuptheme()
    
    # Qlabel
    var_label = QLabel('Version: 1.0')
    var_label.setStyleSheet('font-size: 10px;')

    var_window.mtd_addwidgettoverticallayout(var_label)
    # var_window.mtd_adjustfixedsize() #A1:

    # Defining icon
    var_icon = QIcon(str(PATH_WINDOW_ICON_PATH))
    var_window.setWindowIcon(var_icon)
    var_app.setWindowIcon(var_icon)

    # label.py
    var_info = cls_info('Your account333')
    var_window.mtd_addwidgettoverticallayout(var_info)

    # Display
    var_display = cls_display()
    # var_display = cls_display('aaa')
    var_display.setPlaceholderText('Enter your operation')
    var_window.mtd_addwidgettoverticallayout(var_display)

    # Grid
    var_buttonsgrid = cls_buttonsgrid(var_display, var_info)
    var_window.var_verticallayout.addLayout(var_buttonsgrid)

    #Status bar
    xxx = var_window.statusBar()
    xxx.showMessage('Edson Copque® | ➤linktr.ee/edsoncopque | ➤github ecopque')

    var_window.mtd_addwidgettoverticallayout(cls_display('Take your notes.'))
    var_window.mtd_adjustfixedsize() #A1:
    
    # Menubar xxxxxxxxxxx
    var_window.mtd_setupmenu()
    
    # Runs everything
    var_window.show()
    var_app.exec()

#A1: We could put it inside #B1 / def my_addWidgetToVerticalLayout.
