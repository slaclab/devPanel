from pydm import Display
from PyQt5 import QtGui, QtCore, QtWidgets
import sys

class devPanelMaddy(Display):



    def __init__(self, parent=None, args=None):
        super(devPanelMaddy, self).__init__(parent=parent, args=args)
        self.ui.WIZARD.clicked.connect(lambda:self.updateOutput("You're a WIZARD, Harry"))
        self.ui.what_wizard.stateChanged.connect(self.buttonToggled)
        

    def ui_filename(self):
        return 'devPanelMaddy.ui'
        
    def updateOutput(self, output):
        print(output)
        self.ui.wizard_text.setText(output)
        
    def buttonToggled(self):
        self.ui.wizard_text.setText("An amazing one o'course!"
                                  if self.ui.what_wizard.isChecked()
                                  else "I hope you have a Felix Felicis type of day!")

intelclass = devPanelMaddy


