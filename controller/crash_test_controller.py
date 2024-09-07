from PySide6.QtCore import QObject
from controller.login_controller import LoginController
from controller.home_controller import HomeController
from view.login_view import LoginView
from PySide6.QtCore import Signal, Slot

class CrashController(QObject):
    def __init__(self):
        super(CrashController, self).__init__()
        self.login_controller = LoginController()
        self.home_controller = HomeController()
        
        # binding signals
        self.login_controller.login_success.connect(self.loggin_success_event)

    @Slot()
    def loggin_success_event(self):
        self.hide_login()
        self.show_home()
        
    def show_login(self):
        self.login_controller.login_obj.show_login()

    def hide_login(self):
        self.login_controller.login_obj.hide_login()
        
    def show_home(self):
        self.home_controller.show_home_page()
        
    def hide_home(self):
        self.home_controller.hide_home_page()

