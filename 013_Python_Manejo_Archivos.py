from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║              Unidad 7 - Fechas, Horas, Archivos                             ║
║                 * Modulo time, datetime                                     ║
║                 * Manejo de fechas y horas                                  ║
║                 * Operaciones con archivos                                  ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                     archivar                                ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://www.w3schools.in/python-tutorial/gui-programming/
""");
nuevo(0,"inicio");
#################################################################
#Clase_Archivos_Ej_001
from Python_Metodos_propia import *




valor1=0.1
valor2=0.1
while True:
	try:
		valor1=float(input("valor 1 : "))
		valor2=float(input("valor 2 : "))
		break
	except ValueError:
		print("Error. solo nomeros")
print ("resultado suma : "+str(resultado_suma_metodo(valor1,valor2)))
print ("resultado resta : "+str(resultado_resta_metodo(valor1,valor2)))
print ("resultado multiplicacion : "+str(resultado_multiplica_metodo(valor1,valor2)))
print ("resultado divicion : "+str(resultado_divide_metodo(valor1,valor2)))
print ("resultado portenciacion : "+str(resultado_portenciacion_metodo(valor1,valor2)))
print ("resultado radicacion2 : "+str(resultado_radicacion2_metodo(valor1,valor2)))
print ("resultado porcentage : "+str(resultado_porcentage_metodo(valor1,valor2)))
print ("resultado cociente : "+str(resultado_cociente_metodo(valor1,valor2)))
print ("resultado resto : "+str(resultado_resto_metodo(valor1,valor2)))
print (input("ej 009-1        continuar?"));
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
def iniciar_pantalla_raiz():
	iniciar_pantalla_raiz=Tk()#                                Define la ventana principal de la aplicación
	iniciar_pantalla_raiz.title("Mi primer pantalla")#         ancho   x alto
	iniciar_pantalla_raiz.geometry("640x640")#                 Define las dimensiones de la ventana, que se ubicará en el centro de la pantalla. Si se omite esta línea la # ventana se adaptará a los widgets que se coloquen en ella.
	iniciar_pantalla_raiz.configure(bg = "white")#				 Asigna un color de fondo a la ventana.
	#ttk.Button(iniciar_pantalla_raiz, text='Exit', command=quit).pack(side=BOTTOM)
	#iniciar_pantalla_raiz.iconbitmap("icono.png")
	#frame1_iniciar_pantalla_raiz(iniciar_pantalla_raiz)

	# Define un botón en la parte inferior de la ventana que cuando sea presionado hará que termine el programa.
	# El primer parámetro indica el nombre de la ventana 'iniciar_pantalla_raiz' donde se ubicará el botón

	iniciar_pantalla_raiz.title('Aplicación')
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado suma : "+str(resultado_suma_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado suma : "+str(resultado_suma_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado resta : "+str(resultado_resta_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado multiplicacion : "+str(resultado_multiplica_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado divicion : "+str(resultado_divide_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado portenciacion : "+str(resultado_portenciacion_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado radicacion2 : "+str(resultado_radicacion2_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado porcentage : "+str(resultado_porcentage_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado cociente : "+str(resultado_cociente_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado resto : "+str(resultado_resto_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()

	img = PhotoImage(file="brazo_robotico.png")
	widget = Label(iniciar_pantalla_raiz, image=img).pack()

	# Define un botón en la parte inferior de la frame_iniciar_pantalla_raiz
	# que cuando sea presionado hará que termine el programa.
	# El primer parámetro indica el nombre de la frame_iniciar_pantalla_raiz 'raiz'
	# donde se ubicará el botón
	ttk.Button(iniciar_pantalla_raiz, text='Salir', command=iniciar_pantalla_raiz.destroy).pack(side=BOTTOM)
	#ttk.Button(iniciar_pantalla_raiz, text='terminar programa', command=quit).pack(side=BOTTOM)

	# Después de definir la frame_iniciar_pantalla_raiz principal y un widget botón
	# la siguiente línea hará que cuando se ejecute el programa
	# construya y muestre la frame_iniciar_pantalla_raiz, quedando a la espera de
	# que alguna persona interactúe con ella.

	# Si la persona presiona sobre el botón Cerrar 'X', o bien,
	# sobre el botón 'Salir' el programa llegará a su fin.
	iniciar_pantalla_raiz.mainloop()
iniciar_pantalla_raiz();
