# main.py (A)
import sys #1:
from PySide6.QtWidgets import (QApplication, QLabel) #2:
from main_window import cls_mainwindow #3:
from PySide6.QtGui import QIcon #4:
from variables import PATH_WINDOW_ICON_PATH #5:
from display import cls_display #6:
from label import cls_info #7:
from styles import func_setuptheme #8:
from buttons import cls_buttonsgrid #9:

if __name__ == '__main__': #10:
    
    var_app = QApplication(sys.argv) #11:
    var_window = cls_mainwindow() #12:
    
    func_setuptheme() #13:
    
    var_label = QLabel('Version: 1.0') #14:
    var_label.setStyleSheet('font-size: 10px;') #15:
    var_window.mtd_addwidgettoverticallayout(var_label) #16:

    var_icon = QIcon(str(PATH_WINDOW_ICON_PATH)) #17:
    var_window.setWindowIcon(var_icon) #18:
    var_app.setWindowIcon(var_icon) #18:

    var_info = cls_info('Your new account') #19:
    var_window.mtd_addwidgettoverticallayout(var_info) #20:

    var_display = cls_display() #21:
    var_display.setPlaceholderText('Enter your operation') #22:
    var_window.mtd_addwidgettoverticallayout(var_display) #23:

    var_buttonsgrid = cls_buttonsgrid(var_display, var_info, var_window) #24:
    var_window.var_verticallayout.addLayout(var_buttonsgrid) #25:

    xxx = var_window.statusBar() #26:
    xxx.showMessage('Edson Copque® | ➤linktr.ee/edsoncopque | ➤github/ecopque') #26:

    var_window.mtd_addwidgettoverticallayout(cls_display('Take your notes.')) #27:
    var_window.mtd_adjustfixedsize() #28:
    
    var_window.mtd_setupmenu() #29:
    
    var_window.show() #30:
    var_app.exec() #31:
