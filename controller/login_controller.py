# import the Object class from the Pyside6
from PySide6.QtCore import QObject
from view.login_view import LoginView
from PySide6.QtCore import Signal


from PySide6.QtCore import Signal  # Add this import statement

class LoginController(QObject):
    login_success = Signal()
    def __init__(self):
        super(LoginController, self).__init__()
        self.login_obj = LoginView()
        
        # add events handlers
        self.login_obj.pushButton.clicked.connect(self.check_login)


    def check_login(self):
        self.login_success.emit()