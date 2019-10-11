from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║              Unidad 5 - MySQL, Parte 1                                      ║
║                 * INSERT, UPDATE, DELETE, SELECT                            ║
║                 * FECHAS Y HORAS                                            ║
║                 * %LIKE%                                                    ║
║                 * JOIN                                                      ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                           Python List/Array Methods                         ║
║                          ---------------------------                        ║
║                                                                             ║
║       Operator     Description                                              ║
║                                                                             ║
║       Button       The Button widget is used to display buttons in          ║
║                    your application.                                        ║
║              Option   Description                                           ║
║              activebackground-                                              ║
║                 Background color when the button is under the cursor        ║
║              activeforeground-                                              ║
║                 Foreground color when the button is under the cursor        ║
║              bd     -                                                       ║
║                 Border width in pixels. Default is 2.                       ║
║              bg     -                                                       ║
║                 Normal background color.                                    ║
║              command-                                                       ║
║                 Function or method to be called when the button is clicked. ║
║              fg     -                                                       ║
║                 Normal foreground (text) color.                             ║
║              font   -                                                       ║
║                 Text font to be used for the button's label.                ║
║              height -                                                       ║
║                 Height of the button in text lines (for textual buttons)    ║
║                 or pixels (for images).                                     ║
║              highlightcolor-                                                ║
║                 The color of the focus highlight when the widget has        ║
║                 focus.                                                      ║
║              image  -                                                       ║
║                 Image to be displayed on the button (instead of text).      ║
║              justify-                                                       ║
║                 How to show multiple text lines: LEFT to left-justify each  ║
║                 line; CENTER to center them; or RIGHT to right-justify.     ║
║              padx   -                                                       ║
║                 Additional padding left and right of the text.              ║
║              pady   -                                                       ║
║                 Additional padding above and below the text.                ║
║              relief -                                                       ║
║                 Relief specifies the type of the border. Some of the values ║
║                                                                             ║
║                 are SUNKEN, RAISED, GROOVE, and RIDGE.                      ║
║              state  -                                                       ║
║                 Set this option to DISABLED to gray out the button and make ║
║                 it unresponsive. Has the value ACTIVE when the mouse        ║
║                 is over it. Default is NORMAL.                              ║
║              underline-                                                     ║
║                 Default is -1, meaning that no character of the text on     ║
║                 the button will be underlined. If nonnegative,              ║
║                 the corresponding text character will be underlined.        ║
║              width  -                                                       ║
║                 Width of the button in letters (if displaying text)         ║
║                 or pixels (if displaying an image).                         ║
║              wraplength-                                                    ║
║                 If this value is set to a positive number, the text         ║
║                 lines will be wrapped to fit within this length.            ║
║                                                                             ║
║              Medthod-     Description                                       ║
║              flash() -                                                      ║
║                 Causes the button to flash several times between active     ║
║                 and normal colors. Leaves the button in the state it was    ║
║                 in originally. Ignored if the button is disabled.           ║
║              invoke()-                                                      ║
║                 Calls the button's callback, and returns what that function ║
║                 returns. Has no effect if the button is disabled or there   ║
║                 is no callback.                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║       Canvas       The Canvas widget is used to draw shapes, such as lines, ║
║                    ovals, polygons and rectangles, in your application.     ║
║                                                                             ║
║       Checkbutton  The Checkbutton widget is used to display a number of    ║
║                    options as checkboxes. The user can select multiple      ║
║                    options at a time.                                       ║
║                                                                             ║
║       Entry        The Label widget is used to provide a single-line caption║
║                    field for accepting values from a user.                  ║
║                                                                             ║
║       Frame        The Frame widget is used as a container widget to        ║
║                    organize other widgets.                                  ║
║                                                                             ║
║       Label        Returns the index of the first element with the specified║
║                    for other widgets. It can also contain images.           ║
║                                                                             ║
║       Listbox      The Listbox widget is used to provide a list of options  ║
║                    to a user.                                               ║
║                                                                             ║
║       Menubutton   The Menubutton widget is used to display menus in your   ║
║                    application.                                             ║
║                                                                             ║
║       Menu         The Menu widget is used to provide various commands to   ║
║                    a user. These commands are contained inside Menubutton.  ║
║                                                                             ║
║       Message      The Message widget is used to display multiline text     ║
║                    fields for accepting values from a user.                 ║
║                                                                             ║
║       Radiobutton  The Radiobutton widget is used to display a number of    ║
║                    options as radio buttons. The user can select only one   ║
║                    option at a time.                                        ║
║                                                                             ║
║       Scale        The Scale widget is used to provide a slider widget.     ║
║                                                                             ║
║       Scrollbar    The Scrollbar widget is used to add scrolling capability ║
║                     to various widgets, such as list boxes.                 ║
║                                                                             ║
║       Text         The Text widget is used to display text in multiple lines║
║                                                                             ║
║       Toplevel     The Toplevel widget is used to provide a separate window ║
║                     container.                                              ║
║                                                                             ║
║       Spinbox      The Spinbox widget is a variant of the standard Tkinter  ║
║                    Entry widget, which can be used to select from a fixed   ║
║                    number of values.                                        ║
║                                                                             ║
║       PanedWindow  A PanedWindow is a container widget that may contain any ║
║                     number of panes, arranged horizontally or vertically.   ║
║                                                                             ║
║       LabelFrame   A labelframe is a simple container widget. Its primary   ║
║                     purpose is to act as a spacer or container for complex  ║
║                     window layouts.                                         ║
║                                                                             ║
║       tkMessageBox This module is used to display message boxes in you      ║
║                     applications.                                           ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║              Unidad 8,0                                                     ║
║              pip install Pillow==2.2.2                                      ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
https://www.youtube.com/watch?v=CppgV8inf7g&pbjreload=10
https://python-para-impacientes.blogspot.com/2015/12/tkinter-interfaces-graficas-en-python-i.html
https://python-para-impacientes.blogspot.com/2015/12/tkinter-disenando-frame_pantalla_raizs-graficas.html
""");
nuevo(0,"inicio");
#################################################################
#Clase_P_graf_01

from tkinter import *
print ("https://python-para-impacientes.blogspot.com/2015/12/tkinter-interfaces-graficas-en-python-i.html")
print ("http://pharalax.com/blog/python-desarrollo-de-interfaces-graficas-con-tkinter-labelsbuttonsentrys/")
print ("https://www.w3resource.com/python/python-tutorial.php/")
print ("https://www.w3schools.in/python-tutorial/")
print ("https://www.w3schools.com/python/default.asp")
print ("https://www.w3schools.com/python/python_examples.asp")
print ("https://www.tutorialspoint.com/python3/python_gui_programming.htm")
print ("https://www.pythondiario.com")
print ("https://www.tutorialspoint.com/python3/tk_button.htm")
print ("/")


def iniciar_pantalla_raiz():
	pantalla_raiz=Tk()
	pantalla_raiz.title("Mi primer pantalla")
	pantalla_raiz.geometry("640x480")
	btn4 = Button(pantalla_raiz, text= "Salir", bg= "Black", fg= "red", command=pantalla_raiz.destroy)
	btn4.grid(column=1, row=7)
	pantalla_raiz.mainloop
var = input ("inicio pantalla grafica '1'(S/N)")
if var.upper() =="S":
	iniciar_pantalla_raiz()
nuevo(1);
#################################################################
#Clase_P_graf_02
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
def iniciar2_pantalla_raiz():

	# Define la frame_pantalla_raiz principal de la aplicación

	pantalla_raiz = Tk()

	# Define las dimensiones de la frame_pantalla_raiz, que se ubicará en
	# el centro de la pantalla. Si se omite esta línea la
	# frame_pantalla_raiz se adaptará a los widgets que se coloquen en
	# ella.

	pantalla_raiz.geometry('300x200') # anchura x altura

	# Asigna un color de fondo a la frame_pantalla_raiz. Si se omite
	# esta línea el fondo será gris

	pantalla_raiz.configure(bg = 'beige')

	# Asigna un título a la frame_pantalla_raiz

	pantalla_raiz.title('Aplicación')

	# Define un botón en la parte inferior de la frame_pantalla_raiz
	# que cuando sea presionado hará que termine el programa.
	# El primer parámetro indica el nombre de la frame_pantalla_raiz 'raiz'
	# donde se ubicará el botón
	ttk.Button(pantalla_raiz, text='Salir', command=pantalla_raiz.destroy).pack(side=BOTTOM)
	ttk.Button(pantalla_raiz, text='terminar programa', command=quit).pack(side=BOTTOM)

	# Después de definir la frame_pantalla_raiz principal y un widget botón
	# la siguiente línea hará que cuando se ejecute el programa
	# construya y muestre la frame_pantalla_raiz, quedando a la espera de
	# que alguna persona interactúe con ella.

	# Si la persona presiona sobre el botón Cerrar 'X', o bien,
	# sobre el botón 'Salir' el programa llegará a su fin.

	pantalla_raiz.mainloop()
var = input ("inicio pantalla grafica '2'(S/N)")
if var.upper() =="S":
	iniciar2_pantalla_raiz()
nuevo(2);
#################################################################
#Clase_P_graf_03
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
def iniciar3_pantalla_raiz():

	pantalla_raiz=Tk()
	frame_pantalla_raiz=Frame(pantalla_raiz)
	frame_pantalla_raiz.pack()
	pantalla_raiz.geometry("300x200")
	pantalla_raiz.configure(bg = "#ff55ff")
	pantalla_raiz.title("UTN 2019 app")
	frame_pantalla_raiz = Frame(pantalla_raiz, width=640,height=480)
	frame_pantalla_raiz.pack(fill="both", expand="True")

	operacion=""
	reset_pantalla=False
	resultado=0
	password_personal=StringVar()
	Label(frame_pantalla_raiz, text="Usuario",font="15",fg="blue").grid(column=0, row=3, padx=5,pady=5, sticky="e")#este weste noth sour
	usuario_personal=StringVar()
	Cuadro_text_usuario=Entry(frame_pantalla_raiz, textvariable=usuario_personal)
	Cuadro_text_usuario.grid(column=1, row=3, padx=5,pady=5)
	Cuadro_text_usuario.config(background="black", fg="#03f943", justify="right")

	Label(frame_pantalla_raiz, text="password",font="15",fg="blue").grid(column=0, row=4, padx=5,pady=5, sticky="e")

	Cuadro_text_password=Entry(frame_pantalla_raiz, textvariable=password_personal)
	Cuadro_text_password.grid(column=1, row=4, padx=5,pady=5)
	Cuadro_text_password.config(background="black", fg="#03f943", justify="right")


	def codigo_btn0():
		print("envio un dato desde programa a un cuadro de texto")
		usuario_personal.set("mi_nombre_y_edad")
		password_personal.set("mi perro")

	def codigo_btn1(usuario_,password_):
		print("envio un dato desde un cuadro de texto a pantalla")
		print ("Username: " + str(usuario_))
		print ("Password: " + str(password_))
		usuario_personal.set("ok")
		password_personal.set("_*_")

	def codigo_btn2():
		print("envio un dato desde archivo a un cuadro de texto")
		archivo_de_texto=open("datos_pantalla.txt","r")# abre el archivo text.txt para lectura en bloque
		linea_texto_a_memoria=archivo_de_texto.readlines();
		print ("Username: " + str(linea_texto_a_memoria[0]))
		print ("Password: " + str(linea_texto_a_memoria[1]))
		usuario_personal.set(linea_texto_a_memoria[0])
		password_personal.set(linea_texto_a_memoria[1])
		archivo_de_texto.close();

	def codigo_btn3(usuario_,password_):
		datos_a_guardar = {}
		print("envio un dato desde un cuadro de texto a archivo")
		print ("Username: " + str(usuario_))
		print ("Password: " + str(password_))
		datos_a_guardar = {usuario_:password_}
		archivo_de_texto=open("datos_pantalla.txt","w")# abre el archivo datos_pantalla.txt para agregar datos
		archivo_de_texto.write(str(usuario_)+"\n");
		archivo_de_texto.write(str(password_));
		archivo_de_texto.close();
		usuario_personal.set("ok")
		password_personal.set("_*_")

	btn0 = Button(frame_pantalla_raiz,text="recuerdame", bg="black", fg="red", command=codigo_btn0)
	btn0.grid(column=0, row=0)
	btn1 = Button(frame_pantalla_raiz,text="mandar a pantalla", bg="white", fg="red", command=lambda:codigo_btn1(usuario_personal.get(),password_personal.get()))
	btn1.grid(column=1, row=0)
	btn2 = Button(frame_pantalla_raiz,text="desde archivo", bg="yellow", fg="red", command=lambda:codigo_btn2())
	btn2.grid(column=0, row=1)
	btn2 = Button(frame_pantalla_raiz,text="a archivo", bg="orange", fg="yellow", command=lambda:codigo_btn3(usuario_personal.get(),password_personal.get()))
	btn2.grid(column=1, row=1)
	btn4 = Button(frame_pantalla_raiz, text= "QUIT", bg="orange", fg= "black", command=pantalla_raiz.destroy)
	btn4.grid(column=1, row=7)
	frame_pantalla_raiz.mainloop()
var = input ("inicio pantalla grafica '3'(S/N)")
if var.upper() =="S":
	iniciar3_pantalla_raiz()
nuevo(3);
#################################################################
#Clase_P_graf_04
from tkinter import *    # Carga módulo tk (widgets estándar)
def iniciar4_pantalla_raiz():
	pantalla_raiz=Tk()
	pantalla_raiz.geometry("300x200")
	pantalla_raiz.configure(bg = "#ff55ff")
	pantalla_raiz.title("UTN 2019 app")

	pantalla_raiz.title("Aplicacion grafica en python")
	etiqueta_pantalla_raiz = Label(pantalla_raiz, text=etiquieta)
	boton_pantalla_raiz = Button(pantalla_raiz, text="OK!!", command=pantalla_raiz.destroy)

	etiqueta_pantalla_raiz.pack()
	boton_pantalla_raiz.pack()
	pantalla_raiz.mainloop()
var = input ("inicio pantalla grafica '4'(S/N)")
if var.upper() =="S":
	etiquieta= input ("ingrese su nombre:")
	iniciar4_pantalla_raiz()
nuevo(4);
#################################################################
#Clase_P_graf_05
from tkinter import *
from tkinter import ttk

# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué
# construye y muestra la frame_pantalla_raiz con todos sus widgets:

class C5_pantalla_raiz():


	def __init__(self):
		def ok_dato():
			nombre=ingreso.get()
			etiqueta.config(text="hola "+str(nombre)+" ingresa tu usuario")
		texto_ingreso =""
		pantalla_raiz = Tk()
		pantalla_raiz.config(width="600", height="650")
		pantalla_raiz.configure(bg = 'beige')
		pantalla_raiz.title('Aplicación')
		frame_pantalla_raiz=Frame(pantalla_raiz)
		frame_pantalla_raiz = Frame(pantalla_raiz, width=640,height=480)
		frame_pantalla_raiz.grid(column=0, row=0,padx=(5,5),pady=(10,10))
		frame_pantalla_raiz.columnconfigure(0,weight=1)
		frame_pantalla_raiz.rowconfigure(0,weight=1)
		frame_pantalla_raiz.config(bg = 'red')
		frame_pantalla_raiz.pack(fill="both", expand="True", anchor="center")
		etiqueta = Label(frame_pantalla_raiz,text="Ingrese su nombre : ")
		etiqueta.grid(column=1,row=2)
		ingreso=Entry(frame_pantalla_raiz,width=15,textvariable=texto_ingreso)
		ingreso.grid(column=3,row=2)
		btn0=Button(frame_pantalla_raiz, text='ok',command=ok_dato)
		btn0.grid(column=3,row=4)
		btn1=Button(frame_pantalla_raiz, text='salir',command=pantalla_raiz.destroy)
		btn1.grid(column=2,row=4)

		pantalla_raiz.mainloop()
def iniciar5_pantalla_raiz():
	llamar=C5_pantalla_raiz()

	return 0

# Mediante el atributo __name__ tenemos acceso al nombre de un
# un módulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el módulo es ejecutado de forma
# independiente (en ese caso __name__ = '__main__') o es
# importado:

if __name__ == '__main__':
	var = input ("inicio pantalla grafica '5'(S/N)")
	if var.upper() =="S":
		iniciar5_pantalla_raiz()


nuevo(5);
#################################################################
#Clase_P_graf_06
import time
import tkinter

def iniciar6_pantalla_raiz():
	def funcion():
		print("Espere por favor")
		pantalla_raiz.iconify()
		time.sleep(5)
		print("listo")
		pantalla_raiz.deiconify()
	pantalla_raiz = Tk()
	pantalla_raiz.geometry('300x200')
	pantalla_raiz.configure(bg = 'beige')
	pantalla_raiz.title('Aplicación')
	etiqueta_pantalla_raiz = Label(pantalla_raiz, text="Gracias por esperar")
	etiqueta_pantalla_raiz.pack()
	boton_pantalla_raiz = Button(pantalla_raiz, text='Minimizar', bg="orange", fg="red", command=funcion())
	boton_pantalla_2_raiz = Button(pantalla_raiz, text="SALIR", bg="orange", fg="red", command=pantalla_raiz.destroy).pack(side=BOTTOM)
	pantalla_raiz.mainloop
var = input ("inicio pantalla grafica '6'(S/N)")
if var.upper() =="S":
	iniciar6_pantalla_raiz()
nuevo(6);
#################################################################
#Clase_P_graf_07----------------------------------------------------------------------------ver cerrar
import tkinter as tk
from tkinter import *
from tkinter import ttk
class iniciar7_pantalla_raiz( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Hola UTN")

        self.button1 = Button( self, text = "crear", width = 25, command = self.windows_crear)
        self.button1.grid( row = 2, column = 0, columnspan = 1, sticky = W+E+N+S )
        self.button2 = Button( self, text = "cerrar", width = 25, command=lambda:  self.windows_cerrar )
        self.button2.grid( row = 3, column = 0, columnspan = 1, sticky = W+E+N+S )
    def windows_crear(self):
        self.newWindow = funcion_2()
    def windows_cerrar(self):
        self.destroy()
        return (0)

class funcion_2(Frame):
	def __init__(self):
		new =tk.Frame.__init__(self)
		new = Toplevel(self)
		new.title("Agrego mas pantallas")
		new.button = tk.Button(  text = "Cierro", width = 25,command=lambda:self.windows_cerrar )
		new.button.pack()
	def windows_cerrar(self):
		self.destroy()
		return (0)

def main():
	var = input ("inicio pantalla grafica '7'(S/N)")
	if var.upper() =="S":
		iniciar7_pantalla_raiz().mainloop()
if __name__ == '__main__':
    main()
nuevo(7);
#################################################################
#Clase_P_graf_08
from tkinter import *
from tkinter import messagebox
def iniciar8_pantalla_raiz():
	pantalla_raiz = Tk()
	pantalla_raiz.geometry("200x100")
	def Saludar_Hola():
	   messagebox.showinfo("Buen dia", "Como va la vida")
	Boton1 = Button(pantalla_raiz, text = "Todo bien?", command = Saludar_Hola)
	Boton1.place(x = 35,y = 50)
	boton_pantalla_raiz = Button(pantalla_raiz, text="SALIR", bg="brown", fg="red", command=pantalla_raiz.destroy).pack(side=BOTTOM)
	pantalla_raiz.mainloop()
var = input ("inicio pantalla grafica '8'(S/N)")
if var.upper() =="S":iniciar8_pantalla_raiz()
nuevo(8);
#################################################################
#Clase_P_graf_09
from tkinter import *
from tkinter import messagebox
def iniciar9_pantalla_raiz():
	pantalla_raiz = Tk()
	text = Text(pantalla_raiz)
	text.insert(INSERT, "Hola.....")
	text.insert(END, "Chau.....")
	text.pack()
	text.tag_add("Aqui", "1.0", "1.4")
	text.tag_add("Inicio", "1.8", "1.13")
	text.tag_config("Aqui", background = "yellow", foreground = "blue")
	text.tag_config("Inicio", background = "black", foreground = "green")
	boton_pantalla_raiz = Button(pantalla_raiz, text="SALIR", bg="orange", fg="red", command=pantalla_raiz.destroy).pack(side=BOTTOM)
	pantalla_raiz.mainloop()
var = input ("inicio pantalla grafica '9'(S/N)")
if var.upper() =="S":iniciar9_pantalla_raiz()
nuevo(9);
#################################################################
#Clase_P_graf_010
from tkinter import *
from tkinter import messagebox
def iniciar10_pantalla_raiz():
	pantalla_raiz = Tk()
	frame_pantalla_raiz = Frame(pantalla_raiz)
	frame_pantalla_raiz.pack()
	bottomframe = Frame(pantalla_raiz)
	bottomframe.pack( side = BOTTOM )
	redbutton = Button(frame_pantalla_raiz, text = "Red", fg = "red")
	redbutton.pack( side = LEFT)
	greenbutton = Button(frame_pantalla_raiz, text = "brown", fg="brown")
	greenbutton.pack( side = LEFT )
	bluebutton = Button(frame_pantalla_raiz, text = "Blue", fg = "Blue")
	bluebutton.pack( side = LEFT )
	blackbutton = Button(bottomframe, text = "red", fg = "red")
	blackbutton.pack( side = BOTTOM)
	boton_pantalla_raiz = Button(bottomframe, text="SALIR", bg="brown", fg="red", command=pantalla_raiz.destroy).pack(side=BOTTOM)
	pantalla_raiz.mainloop()
var = input ("inicio pantalla grafica '10'(S/N)")
if var.upper() =="S":iniciar10_pantalla_raiz()
nuevo(10);
#################################################################
#Clase_P_graf_011;
from tkinter import *
from tkinter import messagebox
def iniciar11_pantalla_raiz():

	pantalla_raiz = Tk()
	pantalla_raiz.geometry("200x100")
	mb =  Menubutton ( pantalla_raiz, text = "Contenedor", relief = RAISED )
	mb.grid()
	mb.menu  =  Menu ( mb, tearoff = 0 )
	mb["menu"]  =  mb.menu

	elemento_1  = IntVar()
	elemento_2 = IntVar()

	mb.menu.add_checkbutton ( label = "1er elemento",
							  variable = elemento_1 )
	mb.menu.add_checkbutton ( label = "2do elemento",
							  variable = elemento_2 )

	mb.pack()
	boton_pantalla_raiz = Button(pantalla_raiz, text="SALIR", bg="brown", fg="red", command=pantalla_raiz.destroy).pack(side=BOTTOM)
	pantalla_raiz.mainloop()
var = input ("inicio pantalla grafica '11'(S/N)")
if var.upper() =="S":iniciar11_pantalla_raiz()
nuevo(11);
#################################################################
#Clase_P_graf_012
from tkinter import *
from tkinter import messagebox
def iniciar12_pantalla_raiz():

	pantalla_raiz = Tk()
	Lb1 = Listbox(pantalla_raiz)
	Lb1.insert(1, "Python")
	Lb1.insert(2, "Perl")
	Lb1.insert(3, "C")
	Lb1.insert(4, "PHP")
	Lb1.insert(5, "JSP")
	Lb1.insert(6, "Ruby")
	Lb1.pack()
	var = StringVar()
	label = Label( pantalla_raiz, textvariable = var, relief = RAISED )
	var.set("Hola. Como va todo?")
	label.pack()
	boton_pantalla_raiz = Button(pantalla_raiz, text="SALIR", bg="brown", fg="red", command=pantalla_raiz.destroy).pack(side=BOTTOM)
	pantalla_raiz.mainloop()
var = input ("inicio pantalla grafica '12'(S/N)")
if var.upper() =="S":iniciar12_pantalla_raiz()
nuevo(12);
#################################################################
#Clase_P_graf_013
from tkinter import *
from tkinter import messagebox
def iniciar13_pantalla_raiz():

	pantalla_raiz = Tk()
	def eleccion():
	   seleccionado = "eleccioneccione su oipcion " + str(var.get())
	   label.config(text = seleccionado)
	var = IntVar()
	R1 = Radiobutton(pantalla_raiz, text = "Option 1", variable = var, value = 1,  command = eleccion)
	R1.pack( anchor = W )

	R2 = Radiobutton(pantalla_raiz, text = "Option 2", variable = var, value = 2,  command = eleccion)
	R2.pack( anchor = W )

	R3 = Radiobutton(pantalla_raiz, text = "Option 3", variable = var, value = 3,	  command = eleccion)
	R3.pack( anchor = W)

	label = Label(pantalla_raiz)
	label.pack()
	boton_pantalla_raiz = Button(pantalla_raiz, text="SALIR", bg="brown", fg="red", command=pantalla_raiz.destroy).pack(side=BOTTOM)
	pantalla_raiz.mainloop()
var = input ("inicio pantalla grafica '13'(S/N)")
if var.upper() =="S":iniciar13_pantalla_raiz()
nuevo(13);
#################################################################
#Clase_P_graf_014
from tkinter import *
from tkinter import messagebox
def iniciar14_pantalla_raiz():

	pantalla_raiz = Tk()
	def donothing():
	   filewin = Toplevel(pantalla_raiz)
	   button = Button(filewin, text="Luego se definiran los comandos")
	   button.pack()

	Barra_menu = Menu(pantalla_raiz)
	Item_Menu = Menu(Barra_menu, tearoff = 0)
	Item_Menu.add_command(label = "Recargar", command = donothing)
	Item_Menu.add_command(label = "Abrir", command = donothing)
	Item_Menu.add_command(label = "Grabar", command = donothing)
	Item_Menu.add_command(label = "Grabar como", command = donothing)
	Item_Menu.add_command(label = "Cerrar", command = donothing)
	Item_Menu.add_separator()
	Item_Menu.add_command(label = "Salir", command = pantalla_raiz.destroy)
	Barra_menu.add_cascade(label = "Archivo", menu = Item_Menu)

	Edit_Menu = Menu(Barra_menu, tearoff=0)
	Edit_Menu.add_command(label = "Deshacer", command = donothing)
	Edit_Menu.add_separator()

	Edit_Menu.add_command(label = "Copiar", command = donothing)
	Edit_Menu.add_command(label = "Cortar", command = donothing)
	Edit_Menu.add_command(label = "Pegar", command = donothing)
	Edit_Menu.add_command(label = "Borrar", command = donothing)
	Edit_Menu.add_command(label = "Seleccionar todo", command = donothing)
	Barra_menu.add_cascade(label = "Editar", menu = Edit_Menu)

	Help_Menu = Menu(Barra_menu, tearoff=0)
	Help_Menu.add_command(label = "Help Index", command = donothing)
	Help_Menu.add_command(label = "About...", command = donothing)
	Barra_menu.add_cascade(label = "Help", menu = Help_Menu)

	pantalla_raiz.config(menu = Barra_menu)
	pantalla_raiz.mainloop()
var = input ("inicio pantalla grafica '14'(S/N)")
if var.upper() =="S":iniciar14_pantalla_raiz()
nuevo(14);
#################################################################
#Clase_P_graf_015

from tkinter import *

# pip install pillow
from PIL import Image, ImageTk#<--------------------------------------------

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open("brazo_robotico.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

var = input ("inicio pantalla grafica '15'(S/N)")
if var.upper() =="S":
	iniciar14_pantalla_raiz()
	root = Tk()
	app = Window(root)
	root.wm_title("Tkinter")
	root.geometry("400x300")
	root.mainloop()
nuevo(15);
#################################################################
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                               Pantallas graficas                            ║
║                              -------------------                            ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              virtual enviroment                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
Install Python
Install Pip
Install VirtualEnv
pip install VirtualEnv
Install VirtualEnvWrapper-win
pip install VirtualEnvWrapper
Install flask

pip install flask

https://djangocentral.com/how-to-a-create-virtual-environment-for-python/
https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv
https://docs.python.org/3/tutorial/venv.html
https://docs.python-guide.org/dev/virtualenvs/
https://code.visualstudio.com/docs/python/environments
https://virtualenv.pypa.io/en/stable/
https://towardsdatascience.com/python-virtual-environments-made-easy-fe0c603fe601
https://www.geeksforgeeks.org/python-virtual-environment/
https://rukbottoland.com/blog/tutorial-de-python-virtualenv/
https://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/

https://www.youtube.com/watch?v=K_7viALbzqg
https://www.youtube.com/watch?v=N5vscPTWKOk
""")
