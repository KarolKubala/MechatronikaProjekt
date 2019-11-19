import Tkinter as tk
import ttk
import time
import os
import threading


#https://www.instructables.com/id/UART-Controller-With-Tkinter-and-Python-GUI/ <--- !!

serial_data = ''
filter_data = ''
update_period = 5
serial_object = None


window = tk.Tk() #okno aplikacji
window.title( "Inteligentny Taśmociąg" ) # ustawienie tytułu okna głównego
etykieta = Label(window, text = "Inteligentny Taśmociąg") # etykieta
etykieta.pack()
topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM)

def get_data():
  
  global serial_object
  global filter_data
  
  while(1):
    try:
      serial_data = serial_object.readline().strip('\n').strip('\r') #czytanie danych 
      filter_data = serial_data.split(',')
      print filter_data
     except TypeError:
            pass
      
def connect():
  version_ = button_var.get()
  print version_
  global serial_object
  port = port_entry.get()
  baud = baud_entry.get()
  try:
    if version_ == 2:
      serial_object = serial.Serial('/dev/tty' + str(port), baud)
    return
  t1 = threading.Thread(target = get_data)
  t1.daemon = True
  t1.start()
  
  
  
  ###do dokonczenia
  
  
  
def tryb0(event):
  print("0")

def tryb1(event):
  print("1")
  
def stop(event):
  print("2")




Przycisk1 = Button(topFrame, text = "Tryb: sortowanie po kolorze", fg = "green", command = tryb0) #Przycisk1

Przycisk2 = Button(topFrame, text = "Tryb: sortowanie po ksztalcie", fg = "red", command = tryb1) #Przycisk2
                   
Przycisk3 = Button(bottomFrame, text = "STOP", fg = "blue", command = stop) #Przycisk3


Przycisk1.pack()
Przycisk2.pack()
Przycisk3.pack()

window.mainloop()
