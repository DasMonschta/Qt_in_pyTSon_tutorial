import ts3defines, ts3lib, os.path
from ts3plugin import ts3plugin, PluginHost
from PythonQt.QtGui import QDialog
from pytsonui import setupUi
from ts3lib import getPluginPath


class Tutorial(ts3plugin):
    name = "Tutorial GUI"
    requestAutoload = False
    version = "1.0"
    apiVersion = 22
    author = "Luemmel"
    description = "This is a tutorial"
    offersConfigure = True
    commandKeyword = ""
    infoTitle = None
    hotkeys = []
    menuItems = []
    dlg = None

    def __init__(self):
        pass

    def configure(self, qParentWidget):
        self.open_dlg()

    # function to open the dialog
    def open_dlg(self):
        if not self.dlg:
            self.dlg = SettingsDialog(self)
        self.dlg.show()
        self.dlg.raise_()
        self.dlg.activateWindow()


class SettingsDialog(QDialog):
    def __init__(self, tutorial, parent=None):
        super(QDialog, self).__init__(parent)
        # path to .ui-file
        setupUi(self, os.path.join(getPluginPath(), "pyTSon", "scripts", "tutorial", "dialog.ui"))
        self.setWindowTitle("Tutorial")
        # connect a function to the submit button
        # btn_submit cause we named the button like that in Qt Creator
        self.btn_submit.clicked.connect(self.action)

    # on button clicked
    def action(self):
        # get the text from the textarea and print it to the current tab
        # in_textarea cause we named the textarea like that in Qt Creator
        text = self.in_textarea.toPlainText()
        ts3lib.printMessageToCurrentTab(text)



