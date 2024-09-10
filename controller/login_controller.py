# import the Object class from the Pyside6
from PySide6.QtCore import QObject , Signal
from view.login_view import LoginView

class LoginController(QObject):
    login_success = Signal()
    register_success = Signal()
    def __init__(self):
        super(LoginController, self).__init__()
        self.login_obj = LoginView()
        
        # add events handlers
        self.login_obj.login_pushButton.clicked.connect(self.login_button_click)
        self.login_obj.register_pushButton.clicked.connect(self.check_register)

    def login_button_click(self):
        self.login_success.emit()
        
    def check_register(self):
        self.register_success.emit()