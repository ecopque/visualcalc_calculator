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

#1: Módulo sys, fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador.
#2: Este trecho importa as classes QApplication e QLabel do módulo QtWidgets do PySide6. Estas são classes de interface gráfica do usuário (GUI) que permitem criar aplicações com interface gráfica.
#3: Importa a classe cls_mainwindow do arquivo main_window.py. É a definição da janela principal da aplicação.
#4: Importa a classe QIcon do módulo QtGui do PySide6. Esta classe permite definir ícones para a aplicação.
#5: Importa PATH_WINDOW_ICON_PATH do arquivo variables.py. É o caminho para o ícone da janela.
#6: Importa a classe cls_display do arquivo display.py. É a classe para exibir informações na interface gráfica.
#7: Importa a classe cls_info do arquivo label.py. Esta classe é uma versão especializada de QLabel.
#8: Importa a função func_setuptheme do arquivo styles.py. Esta função serve para configurar o tema da interface gráfica.
#9: Importa a classe cls_buttonsgrid do arquivo buttons.py. Esta classe é responsável pela exibição e interação com botões na interface gráfica.
#10: Verifica se o script está sendo executado como o programa principal.
#11: Cria uma instância da aplicação QApplication, que é a base para todas as aplicações Qt. sys.argv é uma lista de argumentos de linha de comando.
#12: Cria uma instância da classe cls_mainwindow, que é a janela principal da aplicação.
#13: Configura o tema da interface gráfica.
#14: Cria uma instância de QLabel com o texto. É um rótulo para exibir a versão da aplicação.
#15: Define o estilo do rótulo para ter um tamanho de fonte de 10 pixels.
#16: Adiciona o rótulo ao layout vertical da janela.
#17: Cria uma instância de QIcon com o caminho para o ícone da janela.
#18: Define o ícone da janela principal e da aplicação.
#19: Cria uma instância de cls_info com um texto.
#20: Adiciona a informação ao layout vertical da janela.
#21: Cria uma instância de cls_display. É um widget para exibição de texto na interface gráfica.
#22: Define um texto de espaço reservado para o var_display.
#23: Adiciona o widget de exibição ao layout vertical da janela.
#24: Cria uma instância.
#25: Adiciona o layout dos botões ao layout vertical da janela.
#26: Define uma mensagem para exibir na barra de status da janela.
#27: Adiciona um novo widget de exibição ao layout vertical da janela.
#28: Ajusta o tamanho fixo da janela.
#29: Configura o menu da janela.
#30: Exibe a janela.
#31: Inicia o loop de eventos da aplicação. Isso garante que a aplicação continue em execução até que seja encerrada pelo usuário.
