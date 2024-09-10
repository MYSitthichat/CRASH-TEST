from PySide6.QtCore import QObject , Signal , Slot
from controller.login_controller import LoginController
from controller.home_controller import HomeController
from controller.register_controller import RegisterController
from view.login_view import LoginView
from view.home_view import HomeView
from controller.databass_controller import DatabassController
from PySide6.QtWidgets import QMessageBox



class CrashController(QObject):
    def __init__(self):
        super(CrashController, self).__init__()
        self.login_controller = LoginController()
        self.home_controller = HomeController()
        self.register_controller = RegisterController()
        self.databass_controller = DatabassController()
        self.databass_controller.create_databass()
        self.login_controller.login_success.connect(self.loggin_success_event)
        self.login_controller.register_success.connect(self.register_success_event)
        self.register_controller.cancle_register.connect(self.cancel_register_event)
        self.register_controller.save_success.connect(self.save_register_event)
        self.home_controller.log_out.connect(self.log_out_success_event)


    @Slot()
    def loggin_success_event(self):
        self.username = self.login_controller.login_obj.user_lineEdit.text()
        self.password = self.login_controller.login_obj.password_lineEdit.text()
        user = self.databass_controller.check_user(self.username, self.password)
        if user:
            self.hide_login()
            self.show_home()
        else:
            self.login_controller.login_obj.user_lineEdit.clear()
            self.login_controller.login_obj.password_lineEdit.clear()
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Username or Password is wrong Please Register")
            msg_box.setWindowTitle("Login Error")
            msg_box.exec()
        self.login_controller.login_obj.clear_login()
    
    def save_register_event(self):
        self.register_name = self.register_controller.register_obj.name_lineEdit.text()
        self.register_lastname = self.register_controller.register_obj.lastname_lineEdit.text()
        self.register_email = self.register_controller.register_obj.email_lineEdit.text()
        self.register_username = self.register_controller.register_obj.username_lineEdit.text()
        self.register_password = self.register_controller.register_obj.password_lineEdit.text()
        self.register_repassword = self.register_controller.register_obj.repassword_lineEdit.text()
        if self.register_password != self.register_repassword:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Password is not same")
            msg_box.setWindowTitle("Register Error")
            msg_box.exec()
        else:
            self.databass_controller.add_user(self.register_name, self.register_lastname, self.register_email, self.register_username, self.register_password)
            self.register_controller.register_obj.clear_register()
            self.hide_register()
            self.show_login()
            print("Register Success")
        
    def log_out_success_event(self):
        self.hide_home()
        self.show_login()
        
    def register_success_event(self):
        self.hide_login()
        self.show_register()    
        
    def cancel_register_event(self):
        self.hide_register()
        self.show_login()
    
    def show_login(self):
        self.login_controller.login_obj.show_login()

    def hide_login(self):
        self.login_controller.login_obj.hide_login()
        
    def show_home(self):
        self.home_controller.show_home_page()
        
    def hide_home(self):
        self.home_controller.hide_home_page()
        
    def show_register(self):
        self.register_controller.show_register()
    
    def hide_register(self):
        self.register_controller.hide_register()

