#GPIO14 PIN 8 - UART_Tx (Serial0)
#GPIO15 PIN 10 - UART_Rx (Serial1)

#https://pyserial.readthedocs.io/en/latest/pyserial_api.html

#w terminalu: sudo raspi-config 
#nacisnij 5 - Interfacing Options 
#P6 - Serial - Enable UART -> Okno1: No -> Okno2: Yes --> Reboot

import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate

while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    ser.write(received_data)                #transmit data serially 
