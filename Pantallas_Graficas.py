from tkinter import *
def iniciar_pantalla_raiz():
	pantalla_raiz=Tk()
	pantalla_raiz.title("Mi primer pantalla")
	pantalla_raiz.geometry("640x480")
	btn4 = Button(pantalla_raiz, text= "Salir", bg= "Black", fg= "red", command=pantalla_raiz.destroy)
	btn4.grid(column=1, row=7)
	pantalla_raiz.mainloop
iniciar_pantalla_raiz()
var = input ("inicio pantalla grafica '2'(S/N)")


