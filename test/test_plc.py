import time
from pymodbus.client import ModbusSerialClient

# coil == M
# register == D
# AD1 = loadcell
# D10 = loadcell_register

comport = 'COM6'
client = ModbusSerialClient(method='rtu', port=comport, stopbits=1, bytesize=8, parity='N', baudrate=4800, timeout=1)
client.connect()
time.sleep(1)
# print(client.is_socket_open())
# client.write_coil(slave=1,address=3,value=0)
# client.write_register(slave=1,address=100,value=100)
while True:
    # m0_resualt = client.read_coils(slave=1,address=1,count=1)
    D100_resualt = client.read_holding_registers(slave=1,address=10,count=1)
    print(D100_resualt.registers[0])
    
    # if m0_resualt.bits[0] == True:
    #     client.write_coil(slave=1,address=1,value=0)
    #     print("turn off")
    # if m0_resualt.bits[0] == False:
    #     client.write_coil(slave=1,address=1,value=1)
    #     print("turn on")
    
    time.sleep(1)