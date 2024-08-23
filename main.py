import sys

from buttons import Button, ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from style import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)
    
    #Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)
    
    # Display
    display = Display()
    window.addWidgetToVLayout(display)
    

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)
   
    # Button
    # button1 = Button('Texto do botão')
    # buttonsGrid.addWidget(button1)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()