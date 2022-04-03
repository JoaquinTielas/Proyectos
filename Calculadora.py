from tkinter import *

ventana = Tk()                                                                      #Creo la ventana
ventana.title("Calculadora")                                                        #Titulo la ventana

Texto = Entry(ventana, font = "Arial 12")                                           #Creo el cuadro de texto
Texto.grid(row = 0, column = 0, columnspan = 4, padx = 0, pady = 5)                 #Ubico el cuadro de texto, columnspan indica cuantas columnas debe ocupar, padx e y son para indicar los espacios entre los demas objetos

boton1 = Button(ventana, text = "1", width = 4, height = 1, font = "Arial 15")      #Creo los botones
boton2 = Button(ventana, text = "2", width = 4, height = 1, font = "Arial 15")
boton3 = Button(ventana, text = "3", width = 4, height = 1, font = "Arial 15")
boton4 = Button(ventana, text = "4", width = 4, height = 1, font = "Arial 15")
boton5 = Button(ventana, text = "5", width = 4, height = 1, font = "Arial 15")
boton6 = Button(ventana, text = "6", width = 4, height = 1, font = "Arial 15")
boton7 = Button(ventana, text = "7", width = 4, height = 1, font = "Arial 15")
boton8 = Button(ventana, text = "8", width = 4, height = 1, font = "Arial 15")
boton9 = Button(ventana, text = "9", width = 4, height = 1, font = "Arial 15")
boton0 = Button(ventana, text = "0", width = 11, height = 1, font = "Arial 15")

botonX = Button(ventana, text = "x", width = 4, height = 1, font = "Arial 15")
botonD = Button(ventana, text = "/", width = 4, height = 1, font = "Arial 15")
botonS = Button(ventana, text = "+", width = 4, height = 1, font = "Arial 15")
botonR = Button(ventana, text = "-", width = 4, height = 1, font = "Arial 15")
botonI = Button(ventana, text = "=", width = 4, height = 1, font = "Arial 15")
botonP = Button(ventana, text = ".", width = 4, height = 1, font = "Arial 15")
botonParA = Button(ventana, text = "(", width = 4, height = 1, font = "Arial 15")
botonParC = Button(ventana, text = ")", width = 4, height = 1, font = "Arial 15")
botonB = Button(ventana, text = "AC", width = 4, height = 1, font = "Arial 15")


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
