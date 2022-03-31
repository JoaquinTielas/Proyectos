import tkinter
from turtle import bgcolor
ventana = tkinter.Tk()
ventana.geometry("500x400")
Titulo = tkinter.Label(ventana,text="Calculadora", bg = "red")
Titulo.pack(side= tkinter.BOTTOM, fill= tkinter.X)


ventana.mainloop()

