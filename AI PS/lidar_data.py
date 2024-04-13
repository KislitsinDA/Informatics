from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.exceptions import ConnectionException
import time

# pymodbus version 2.5.3

METHOD = 'RTU'
COM_PORT = 'COM3'   # Узнать свой в диспетчере устройств
STOP_BITS = 1
BYTE_SIZE = 8
PARITY = 'N'
BAUD_RATE = 115200
TIMEOUT = 1

client = ModbusClient(method=METHOD,
                      port=COM_PORT,
                      stopbits=STOP_BITS,
                      bytesize=BYTE_SIZE,
                      parity=PARITY,
                      baudrate=BAUD_RATE,
                      strict=False,
                      timeout=TIMEOUT)


while True:
    connection = client.connect()
    time.sleep(2)

    try:
        print('Reading...')
        print(f"Connection is {connection}, socket is {client.is_socket_open()}")
        values = client.read_holding_registers(address=0x0, count=0xA, unit=0x1)
        if values.isError():
            print(f"Modbus error: {values}")
        else:
            print("Values:", values.registers)
            for index, value in enumerate(values.registers):
                print(f"Register {index}: {value}")
        print()

    except ConnectionException as ce:
        print("CE ERROR")
        # print("===ERROR=== \nPort cannot be accessed \n", ce)
    except AttributeError as ae:
        print("AE ERROR", ae)
        connection = client.close()

    time.sleep(1)

