from PySide6.QtCore import QObject
from view.home_view import HomeView

class HomeController(QObject):
    def __init__(self):
        super(HomeController, self).__init__()
        self.home_obj = HomeView()
        
    def show_home_page(self):
        self.home_obj.show_main_frame()