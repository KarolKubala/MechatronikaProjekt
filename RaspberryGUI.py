import tkinter as tk

window = tk.Tk() #okno aplikacji
window.title( "Inteligentny Taśmociąg" ) # ustawienie tytułu okna głównego
etykieta = Label(window, text = "Inteligentny Taśmociąg") # etykieta
etykieta.pack()
topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM)



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
