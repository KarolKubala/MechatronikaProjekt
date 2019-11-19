#GPIO14 PIN 8 - UART_Tx (Serial0)
#GPIO15 PIN 10 - UART_Rx (Serial1)

#https://pyserial.readthedocs.io/en/latest/pyserial_api.html
#https://www.teachmemicro.com/raspberry-pi-serial-uart-tutorial/

#w terminalu: sudo raspi-config 
#nacisnij 5 - Interfacing Options 
#P6 - Serial - Enable UART -> Okno1: No -> Okno2: Yes --> sudo reboot (reboot)
#sudo nano /boot/config.txt --> dtoverlay=pi3-disable-bt (wylacza bluetootha)
#sudo nano /boot/cmdline.txt --> remove the word phase "console=serial0,115200" or "console=ttyAMA0,115200"
#sudo nano /boot/cmdline.txt --> change: dwc_otg.lpm_enable=0 console=tty1 console=serial0(or ttyAMA0),115200 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
#sudo reboot

#to na dole pozwala Raspberry na uruchomienie pliku jako skrypt

#!/usr/bin/env python
import serial
from time import sleep

ser = serial.Serial (port = "/dev/ttyS0", baudrate = 11520,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)    #Open port, baud rate, parzystosc wylaczona(parzystosc sumy wysylanych bitow)
while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    ser.write(received_data)                #transmit data serially 

    #aby otworzyc okno przesylu, na urzadzeniu odbierajacym nalezy otworzyc Serial Monitor i ustawic baudrate na 11520
