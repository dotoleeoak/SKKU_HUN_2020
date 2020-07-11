import sys
from PySide2.QtWidgets import QApplication, QWidget
from InUse import UiInUse
from LogIn import UiLogIn
from SignUp import *


class InUse(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # self.ui = UiInUse()
        # self.ui = UiLogIn()
        # self.ui = UiSignUp()
        # self.ui = UiSignUpName()
        # self.ui = UiSignUpContact()
        self.ui = UiSignUpID()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    inUse = InUse()
    inUse.show()
    sys.exit(app.exec_())
