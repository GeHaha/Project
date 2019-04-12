import sys

sys.path.append("../communcate")
from communcate import Communcate


def test():  
    sensorCommuncate = Communcate()
    sensorCommuncate.open_port()
    sensorCommuncate.set_modbus_config(0x01, 'rtu', 0x03)
    
    sensorCommuncate.request_data()
    sensorCommuncate.print_data()

    # get the data twice
    number = 2
    while (number):
        number = number - 1

        sensorCommuncate.request_data()
        sensorCommuncate.print_data()

    sensorCommuncate.close_port()

# Run the test    
test()  

    