from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import MEDIUM_FONT_SIZE
from ulteis import isNumOrDot, isEmpty

class Button(QPushButton):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.configStyle()
    
  def configStyle(self):
    font = self.font()
    font.setPixelSize(MEDIUM_FONT_SIZE)
    self.setFont(font)
    self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    
    self._gridMask = [
      ['C', '◀', '^', '/'],
      ['7', '8', '9', '*'],
      ['4', '5', '6', '-'],
      ['1', '2', '3', '+'],
      ['',  '0', '.', '='],
    ]
    self._makeGrid()
    
  def _makeGrid(self):
    for rowNumber, rowData in enumerate(self._gridMask):
      for columnNumber, ButtonText in enumerate(rowData):
        button = Button(ButtonText)
        
        if not isNumOrDot(ButtonText) and not isEmpty(ButtonText):
          button.setProperty('cssClass', 'specialButton')
        
        self.addWidget(button, rowNumber, columnNumber)