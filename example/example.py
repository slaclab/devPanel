from pydm import Display
from PyQt5 import QtGui

class Example(Display):

    def __init__(self, parent=None, args=None):
        super(Example, self).__init__(parent=parent, args=args)
        self.ui.testButton.clicked.connect(lambda:self.updateOutput("Button Pushed"))
        self.ui.testCheckBox.stateChanged.connect(self.buttonToggled)

    def ui_filename(self):
        return 'example.ui'
        
    def updateOutput(self, output):
        print(output)
        self.ui.outputBox.setText(output)
        
    def buttonToggled(self):
        self.ui.outputBox.setText("Checkbox is " + ("checked"
                                  if self.ui.testCheckBox.isChecked()
                                  else "not checked"))

intelclass = Example
