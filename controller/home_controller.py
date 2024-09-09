from PySide6.QtCore import QObject ,Signal
from view.home_view import HomeView

class HomeController(QObject):
    log_out = Signal()
    def __init__(self):
        super(HomeController, self).__init__()
        self.home_obj = HomeView()
        self.home_obj.logout_pushButton.clicked.connect(self.log_out_pressed)
        
    def show_home_page(self):
        self.home_obj.show_main_frame()
    
    def hide_home_page(self):
        self.home_obj.hide_main_frame()
        
    def log_out_pressed(self):
        self.log_out.emit()