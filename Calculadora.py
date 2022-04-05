from tkinter import *

ventana = Tk()                                                                      #Creo la ventana
ventana.title("Calculadora")                                                        #Titulo la ventana

i = 0

Texto = Entry(ventana, font = "Arial 12")                                           #Creo el cuadro de texto
Texto.grid(row = 0, column = 0, columnspan = 4, padx = 0, pady = 5)                 #Ubico el cuadro de texto, columnspan indica cuantas columnas debe ocupar, padx e y son para indicar los espacios entre los demas objetos

def click_boton(valor):
    Texto.insert(i, valor)
    i = i + 1

boton1 = Button(ventana, text = "1", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton(1))      #Creo los botones
boton2 = Button(ventana, text = "2", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 9, height = 1, font = "Arial 15", command = lambda: click_boton(0))

botonX = Button(ventana, text = "x", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton("x"))
botonD = Button(ventana, text = "/", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton("/"))
botonS = Button(ventana, text = "+", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton("+"))
botonR = Button(ventana, text = "-", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton("-"))
botonI = Button(ventana, text = "=", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton())
botonP = Button(ventana, text = ".", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton("."))
botonParA = Button(ventana, text = "(", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton("("))
botonParC = Button(ventana, text = ")", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton(")"))
botonB = Button(ventana, text = "AC", width = 4, height = 1, font = "Arial 15", command = lambda: click_boton())


boton1.grid(row = 4, column = 0, padx = 2, pady = 2)                                 #Ubico los botones
boton2.grid(row = 4, column = 1, padx = 2, pady = 2) 
boton3.grid(row = 4, column = 2, padx = 2, pady = 2) 
boton4.grid(row = 3, column = 0, padx = 2, pady = 2) 
boton5.grid(row = 3, column = 1, padx = 2, pady = 2) 
boton6.grid(row = 3, column = 2, padx = 2, pady = 2) 
boton7.grid(row = 2, column = 0, padx = 2, pady = 2) 
boton8.grid(row = 2, column = 1, padx = 2, pady = 2) 
boton9.grid(row = 2, column = 2, padx = 2, pady = 2) 
boton0.grid(row = 5, column = 0, padx = 2, pady = 2, columnspan = 2)                 #Columnspan para indicar cuantas columnas ocupa
botonX.grid(row = 1, column = 4, padx = 2, pady = 2) 
botonD.grid(row = 2, column = 4, padx = 2, pady = 2) 
botonS.grid(row = 3, column = 4, padx = 2, pady = 2) 
botonR.grid(row = 4, column = 4, padx = 2, pady = 2) 
botonI.grid(row = 5, column = 4, padx = 2, pady = 2) 
botonP.grid(row = 5, column = 2, padx = 2, pady = 2) 
botonParA.grid(row = 1, column = 0, padx = 2, pady = 2) 
botonParC.grid(row = 1, column = 1, padx = 2, pady = 2) 
botonB.grid(row = 1, column = 2, padx = 2, pady = 2) 




ventana.mainloop()
