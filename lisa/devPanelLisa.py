from pydm import Display
from PyQt5 import QtGui

class DevPanel(Display):

    def __init__(self, parent=None, args=None):
        super(DevPanel, self).__init__(parent=parent, args=args)

    def ui_filename(self):
        return 'devPanel.ui'
        
    def updatePower(self):
        button = self.ui.devPanelLisa

intelclass = DevPanel
