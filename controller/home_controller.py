from PySide6.QtCore import QObject ,Signal ,Slot
from PySide6.QtWidgets import QMessageBox
from view.home_view import HomeView
from controller.check_comport_controller import SerialPortChecker
from controller.read_loadcell import Readloadcell


class HomeController(QObject):
    log_out_button = Signal()
    modbus_consuccess = False
    def __init__(self):
        super(HomeController, self).__init__()
        self.home_obj = HomeView()
        self.check_port_controller = SerialPortChecker()
        self.read_loadcell_controller = Readloadcell()  
        self.home_obj.logout_pushButton.clicked.connect(self.log_out_pressed)
        self.check_port_controller.start()
        self.check_port_controller.ports_updated.connect(self.port_updated)
        self.read_loadcell_controller.connect_modbus_signal.connect(self.modbus_consuc)
        self.home_obj.connect_pushButton.clicked.connect(self.connect_button_pressed)
        self.home_obj.disconnect_pushButton.clicked.connect(self.disconnect_button_pressed)
        self.home_obj.set_zero_pushButton.clicked.connect(self.set_zero_button_pressed)
        self.read_loadcell_controller.raw_data_loadcell.connect(self.show_loadcell_data)
        
    @Slot()
    @Slot(str)
    
    def set_zero_button_pressed(self):
        print("set zero button pressed")
    
    def show_home_page(self):
        self.home_obj.show_main_frame()
    
    def hide_home_page(self):
        self.home_obj.hide_main_frame()
        
    def log_out_pressed(self):
        self.modbus_consuccess = False
        if self.modbus_consuccess == True:
            self.read_loadcell_controller.stop()
        self.log_out_button.emit()
        
    def port_updated(self, ports):
        if len(ports) == 0:
            self.home_obj.comport_comboBox.setEnabled(False)
            self.home_obj.comport_comboBox.clear()
            self.home_obj.comport_comboBox.addItem("NONE")
        else:
            self.home_obj.comport_comboBox.clear()
            self.home_obj.comport_comboBox.setEnabled(True)
            for port in ports:
                self.home_obj.comport_comboBox.addItem(port.device)
                

    def connect_button_pressed(self):
        self.select_comport = self.home_obj.comport_comboBox.currentText()
        self.read_loadcell_controller.connect_modbus(self.select_comport)
        try:
            if self.modbus_consuccess:           
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("COM PORT CONNECTED")
                msg_box.setWindowTitle("SUCCESS")
                msg_box.exec()
                self.read_loadcell_controller.start()
                self.connection_comport_success()
        except AttributeError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Please select COM port")
            msg_box.setWindowTitle("NO COM PORT SELECTED")
            msg_box.exec()
            
    def disconnect_button_pressed(self):
        self.home_obj.set_enable_comport_combobox()
        self.home_obj.set_enable_connect_button()
        self.home_obj.set_disable_disconnect_button()
        self.home_obj.clear_weight_lineedit()
        self.home_obj.set_disable_weight_lineedit()
        self.home_obj.set_disable_set_zero_button()
        self.home_obj.set_disable_start_button()
        self.home_obj.set_disable_stop_button()
        self.home_obj.set_disable_save_button()
        self.home_obj.set_disable_calibrate_weight_lineedit()
        self.home_obj.set_disable_calibrate_button()
        if self.modbus_consuccess == True:
            self.read_loadcell_controller.stop()
            self.modbus_consuccess = False
  
                
    def connection_comport_success(self):
        if self.modbus_consuccess:
            self.home_obj.set_disable_comport_combobox()
            self.home_obj.set_disable_connect_button()
            self.home_obj.set_enable_disconnect_button()
            self.home_obj.set_enable_weight_lineedit()
            self.home_obj.set_enable_set_zero_button()
            self.home_obj.set_enable_start_button()
            self.home_obj.set_enable_stop_button()
            self.home_obj.set_enable_save_button()
            self.home_obj.set_enable_calibrate_weight_lineedit()
            self.home_obj.set_enable_calibrate_button()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("COM PORT NOT CONNECTED")
            msg_box.setWindowTitle("COM PORT ERROR")
            msg_box.exec()
    
    def modbus_consuc(self):
        self.modbus_consuccess = True
        self.show_loadcell_data()
        
    def show_loadcell_data(self):
        try:
            raw_weight = self.read_loadcell_controller.load_cell_value
            self.home_obj.weight_lineEdit.setText(str(raw_weight))
            
        except AttributeError:
            pass
        
