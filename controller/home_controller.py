from PySide6.QtCore import QMetaMethod, QObject ,Signal ,Slot
from PySide6.QtWidgets import QMessageBox
from view.home_view import HomeView
from controller.check_comport_controller import SerialPortChecker
import serial


comport_buadrate = 9600

class HomeController(QObject):
    log_out_button = Signal()
    def __init__(self):
        super(HomeController, self).__init__()
        self.home_obj = HomeView()
        self.check_port_controller = SerialPortChecker()
        self.home_obj.logout_pushButton.clicked.connect(self.log_out_pressed)
        self.check_port_controller.start()
        self.check_port_controller.ports_updated.connect(self.port_updated)
        self.home_obj.connect_pushButton.clicked.connect(self.connect_button_pressed)
        self.home_obj.disconnect_pushButton.clicked.connect(self.disconnect_button_pressed)
        
    @Slot()
    
    def show_home_page(self):
        self.home_obj.show_main_frame()
    
    def hide_home_page(self):
        self.home_obj.hide_main_frame()
        
    def log_out_pressed(self):
        self.log_out_button.emit()
        
    def port_updated(self, ports):
        if len(ports) == 0:
            self.home_obj.comport_comboBox.clear()
            self.home_obj.comport_comboBox.addItem("NONE")
            return
        # if len(ports) >= 1:
        else:
            self.home_obj.comport_comboBox.clear()
            for port in ports:
                self.home_obj.comport_comboBox.addItem(port.device)

                
    def connect_button_pressed(self):
        self.select_comport = self.home_obj.comport_comboBox.currentText()
        if self.select_comport != "NONE":
            try:
                self.serial_connection = serial.Serial(self.select_comport, baudrate=comport_buadrate, timeout=1)
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("COM PORT CONNECTED")
                msg_box.setWindowTitle("SUCCESS")
                msg_box.exec()
                self.serial_connection.close()
                self.connection_comport_success()
            except serial.SerialException as e:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText("COM PORT NOT AVAILABLE")
                msg_box.setWindowTitle("COM PORT ERROR")
                msg_box.exec()

        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Please select COM port")
            msg_box.setWindowTitle("NO COM PORT SELECTED")
            msg_box.exec()
            
    def disconnect_button_pressed(self):
        self.home_obj.set_enable_comport_combobox()
        self.home_obj.set_enable_connect_button()
        self.home_obj.set_disable_disconnect_button()
        self.home_obj.set_disable_weight_lineedit()
        self.home_obj.set_disable_set_zero_button()
        self.home_obj.set_disable_start_button()
        self.home_obj.set_disable_stop_button()
        self.home_obj.set_disable_save_button()
        self.serial_connection.close()        
                
    def connection_comport_success(self):
        self.serial_connection = serial.Serial(self.select_comport, baudrate=comport_buadrate, timeout=1)
        if self.serial_connection.isOpen():
            self.home_obj.set_disable_comport_combobox()
            self.home_obj.set_disable_connect_button()
            self.home_obj.set_enable_disconnect_button()
            self.home_obj.set_enable_weight_lineedit()
            self.home_obj.set_enable_set_zero_button()
            self.home_obj.set_enable_start_button()
            self.home_obj.set_enable_stop_button()
            self.home_obj.set_enable_save_button()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("COM PORT NOT CONNECTED")
            msg_box.setWindowTitle("COM PORT ERROR")
            msg_box.exec()


    
        