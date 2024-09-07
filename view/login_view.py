from view.login_frame import Ui_login
from PySide6.QtWidgets import QMainWindow


class LoginView(QMainWindow,Ui_login):
    def __init__(self, parent=None):
        super(LoginView, self).__init__(parent)
        self.setupUi(self)
    
    def show_login(self):
        self.show()

    def hide_login(self):
        self.hide()
