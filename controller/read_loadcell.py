from pymodbus.client import ModbusSerialClient
from PySide6.QtCore import QThread,Signal,QObject

# coil == M
# register == D
# AD1 = loadcell
# D10 = loadcell_register

class Readloadcell(QThread,QObject):
    connect_modbus_signal = Signal()
    raw_data_loadcell = Signal(int)
    def __init__(self):    
        super(Readloadcell, self).__init__()
        self.running = True

    def run(self):
        while self.running:
            try:
                if self.client.is_socket_open():
                    read_loadcell_response = self.client.read_holding_registers(slave=1,address=10,count=1)
                    self.load_cell_value = read_loadcell_response.registers[0]
                    self.raw_data_loadcell.emit(self.load_cell_value)
                else:
                    self.client.connect()
                self.msleep(100)  
            except:
                pass
            
    def stop(self):
        self.client.close()
        self.running = False
        self.wait()
    
    def connect_modbus(self,comport):
        self.client = ModbusSerialClient(method='rtu', port=comport, stopbits=1, bytesize=8, parity='N', baudrate=4800, timeout=1)
        self.client.connect()
        if self.client.is_socket_open():
            self.running = True
            self.connect_modbus_signal.emit()
        else:
            self.client.connect()
        
    