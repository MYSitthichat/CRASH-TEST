from PySide6.QtWidgets import QMainWindow
from view.register_frame import Ui_Register


class RegisterView(QMainWindow,Ui_Register):
    def __init__(self, parent=None):
        super(RegisterView, self).__init__(parent)
        self.setupUi(self)
        
    
    def show_register(self):
        self.show()
    
    def hide_register(self):
        self.hide()
        
    def clear_register(self):
        self.name_lineEdit.clear()
        self.lastname_lineEdit.clear()
        self.email_lineEdit.clear()
        self.username_lineEdit.clear()
        self.password_lineEdit.clear()
        self.repassword_lineEdit.clear()