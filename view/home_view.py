from view.home_frame import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow


class HomeView(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(HomeView, self).__init__(parent)
        self.setupUi(self)
    
    def show_main_frame(self):
        self.show()
    
    def hide_main_frame(self):
        self.hide()
        