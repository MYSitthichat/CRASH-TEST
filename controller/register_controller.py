from PySide6.QtCore import QObject , Signal
from view.register_view import RegisterView


class RegisterController(QObject):
    save_button = Signal()
    cancle_button = Signal()
    def __init__(self):
        super(RegisterController, self).__init__()
        self.register_obj = RegisterView()
        
        # add events handlers
        self.register_obj.cancle_pushButton.clicked.connect(self.cancle_pushbutton)
        self.register_obj.save_pushButton.clicked.connect(self.save_pushbutton)

    def cancle_pushbutton(self):
        self.cancle_button.emit()
        
    def save_pushbutton(self):
        self.save_button.emit()
        
    def show_register(self):
        self.register_obj.show_register()
        
    def hide_register(self):
        self.register_obj.hide_register()