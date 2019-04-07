import sys

sys.path.append("../communcate")
from data_pack import DataPack

def test():
   package = DataPack("sensor of modbus")
   package.set_data("\x01\x03\x08\x00Ä\t?\x13Ö\x00\x00áû")
   package.print_data()
   
   package2 = DataPack()
   package2.set_data("\x01\x03\x08\x00Ä\tB\x13½\x00\x00ü-")
   package.print_data()

# Run the test
test()