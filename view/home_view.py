from view.home_frame import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow


class HomeView(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(HomeView, self).__init__(parent)
        self.setupUi(self)
        self.set_disable_disconnect_button()
        self.set_disable_weight_lineedit()
        self.set_disable_set_zero_button()
        self.set_disable_start_button()
        self.set_disable_stop_button()
        self.set_disable_save_button()
        self.set_disable_calibrate_weight_lineedit()
        self.set_disable_calibrate_button()

    def show_main_frame(self):
        self.show()
    
    def hide_main_frame(self):
        self.hide()
        
    def set_enable_connect_button(self):
        self.connect_pushButton.setEnabled(True)
        self.connect_pushButton.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #aaff7f, stop: 1 #aaff7f);")
        
    def set_disable_connect_button(self):
        self.connect_pushButton.setEnabled(False)
        self.connect_pushButton.setStyleSheet("background-color: gray; color: white;")
        
    def set_enable_disconnect_button(self):
        self.disconnect_pushButton.setEnabled(True)
        self.disconnect_pushButton.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #aefeff, stop: 1 #aefeff);")
    
    def set_disable_disconnect_button(self):
        self.disconnect_pushButton.setEnabled(False)
        self.disconnect_pushButton.setStyleSheet("background-color: gray; color: white;")
    
    def set_enable_comport_combobox(self,):
        self.comport_comboBox.setEnabled(True)
        self.comport_comboBox.setStyleSheet("background:rgb(255, 255, 255)")
        
    def set_disable_comport_combobox(self):
        self.comport_comboBox.setEnabled(False)
        self.comport_comboBox.setStyleSheet("background-color: gray; color: white;")
        
    def set_enable_weight_lineedit(self):
        self.weight_lineEdit.setEnabled(False)
        self.weight_lineEdit.setStyleSheet("background:rgb(255, 255, 255)")
        
    def set_disable_weight_lineedit(self):
        self.weight_lineEdit.setEnabled(False)
        self.weight_lineEdit.setStyleSheet("background-color: gray; color: white;")    
        
    def set_enable_set_zero_button(self):
        self.set_zero_pushButton.setEnabled(True)
        self.set_zero_pushButton.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0000ff, stop: 1 #ffffff);")
    
    def set_disable_set_zero_button(self):
        self.set_zero_pushButton.setEnabled(False)
        self.set_zero_pushButton.setStyleSheet("background-color: gray; color: white;")
    
    def set_enable_start_button(self):
        self.start_pushButton.setEnabled(True)
        self.start_pushButton.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #62c300, stop: 1 #ffffff);")
        
    def set_disable_start_button(self):
        self.start_pushButton.setEnabled(False)
        self.start_pushButton.setStyleSheet("background-color: gray; color: white;")
        
    def set_enable_stop_button(self):
        self.stop_pushButton.setEnabled(True)
        self.stop_pushButton.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ff0000, stop: 1 #ffffff);")
        
    def set_disable_stop_button(self):
        self.stop_pushButton.setEnabled(False)
        self.stop_pushButton.setStyleSheet("background-color: gray; color: white;")
        
    def set_enable_save_button(self):
        self.save_pushButton.setEnabled(True)
        self.save_pushButton.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00ffff, stop: 1 #ffffff);")
    
    def set_disable_save_button(self):
        self.save_pushButton.setEnabled(False)
        self.save_pushButton.setStyleSheet("background-color: gray; color: white;")
        
    def clear_weight_lineedit(self):
        self.weight_lineEdit.clear()
    
    def set_enable_calibrate_weight_lineedit(self):
        self.calibrate_weight_lineEdit.setEnabled(True)
        self.calibrate_weight_lineEdit.setStyleSheet("background:rgb(255, 255, 255)")
    
    def set_disable_calibrate_weight_lineedit(self):
        self.calibrate_weight_lineEdit.setEnabled(False)
        self.calibrate_weight_lineEdit.setStyleSheet("background-color: gray; color: white;")  
    
    def set_enable_calibrate_button(self):
        self.calibrate_pushButton.setEnabled(True)
        self.calibrate_pushButton.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ff00ff, stop: 1 #ffffff);")
        
    def set_disable_calibrate_button(self):
        self.calibrate_pushButton.setEnabled(False)
        self.calibrate_pushButton.setStyleSheet("background-color: gray; color: white;") 
    