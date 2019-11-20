import Tkinter as tk
import ttk
import time
import os
import threading


#https://www.instructables.com/id/UART-Controller-With-Tkinter-and-Python-GUI/ <--- !!
#zmienne
serial_data = ''
filter_data = ''
serial_object = None

#funkcje
def connect(): #funkcja tworzy watek polaczenia UART przy przycisnieciu przycisku  po wypelnieniu okna PORT i BAUD 
 
  global serial_object
  port = port_entry.get()
  baud = baud_entry.get()
  try:
      try:
        serial_object = serial.Serial('/dev/tty' + str(port), baud)       
 except ValueError:
    print "Enter Baud and Port"
    return
  t1 = threading.Thread(target = get_data)
  t1.daemon = True #demon - program dzialajacy w sposob ciagly i instnieje w celu obslugi zadan do innych programow 
  t1.start()
  
def get_data():
  
  global serial_object
  global filter_data
  
  while(1):
    try:
      serial_data = serial_object.readline().strip('\n').strip('\r') #ciagly odczyt danych
      filter_data = serial_data.split(',')
      print filter_data
     except TypeError:
            pass
   
def send(): #przesyl danych 
  send_data = button_var.get()
  if not send_data:
    print "Sent Nothing"
    serial_object.write(send_data)
  
def disconnect():
  try:
    serial_object.close()
   except AttributeError:
    print "Closed without using.."
    window.quit()
  
#glowna petla
if __name__ == "__main__":
  
  text = Text(width = 30, height = 5)
 
  window = tk.Tk() #okno aplikacji
  window.title( "Inteligentny Tasmociąg" ) # ustawienie tytułu okna głównego
  etykieta = Label(window, text = "Inteligentny Tasmociąg") # etykieta
#   etykieta.pack()
  topFrame = Frame(window)
#   topFrame.pack()
  bottomFrame = Frame(window)
#   bottomFrame.pack(side = BOTTOM)

  baud   = Label(text = "Baud").place(x = 100, y = 348)
  port   = Label(text = "Port").place(x = 200, y = 348)

  #entry
  baud_entry = entry(width = 7)
  baud_entry.place(x = 100, y = 365)
  port_entry = entry(width = 7)
  port_entry.place(x = 200, y = 365)

  
  #buttons
  Przycisk1=Button(text = "Wyslij", command = send, width = 6).place(x = 150, y = 250)
  connect = Button(text = "Polacz", command = connect).place(x = 15, y = 360)
  Przycisk2= Button(bottomFrame, text = "STOP", fg = "blue", command = disconnect, width = 6)
  #radio button
  button_var = IntVar()
  radio_1 = Radiobutton(text = "Tryb: sortowanie po kolorze", variable = button_var, value = 1).place(x = 10, y = 315)
  radio_2 = Radiobutton(text = "Tryb: sortowanie po ksztalcie", variable = button_var, value = 2).place(x = 110, y = 315)

#   Przycisk1.pack()
#   Przycisk2.pack()
#   Przycisk3.pack()

  
  window.geometry('500x500')
  window.mainloop()
