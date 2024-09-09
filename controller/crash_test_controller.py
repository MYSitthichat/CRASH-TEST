from PySide6.QtCore import QObject , Signal , Slot
from controller.login_controller import LoginController
from controller.home_controller import HomeController
from view.login_view import LoginView
from view.home_view import HomeView

class CrashController(QObject):
    def __init__(self):
        super(CrashController, self).__init__()
        self.login_controller = LoginController()
        self.home_controller = HomeController()
        
        # binding signals
        self.login_controller.login_success.connect(self.loggin_success_event)
        self.home_controller.log_out.connect(self.log_out_success_event)

    @Slot()
    def loggin_success_event(self):
        self.hide_login()
        self.show_home()
    
    def log_out_success_event(self):
        self.hide_home()
        self.show_login()
        
    def show_login(self):
        self.login_controller.login_obj.show_login()

    def hide_login(self):
        self.login_controller.login_obj.hide_login()
        
    def show_home(self):
        self.home_controller.show_home_page()
        
    def hide_home(self):
        self.home_controller.hide_home_page()

