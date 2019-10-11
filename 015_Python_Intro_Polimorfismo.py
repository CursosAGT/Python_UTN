from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                     CLASES                                  ║
║                                    --------                                 ║
║                                                                             ║
║          __init__(self, ...)                                                ║
║              This method is called just before the newly created object is  ║
║              returned for usage.                                            ║
║                                                                             ║
║          __del__(self)                                                      ║
║              Called just before the object is destroyed (which has          ║
║              unpredictable timing, so avoid using this)                     ║
║                                                                             ║
║          __str__(self)                                                      ║
║              Called when we use the print function or when str() is used.   ║
║                                                                             ║
║          __lt__(self, other)                                                ║
║              Called when the less than operator (<) is used. Similarly,     ║
║               there are special methods for all the operators (+, >, etc.)  ║
║                                                                             ║
║          __getitem__(self, key)                                             ║
║              Called when x[key] indexing operation is used.                 ║
║                                                                             ║
║          __len__(self)                                                      ║
║              Called when the built-in len() function is used for            ║
║              the sequence object.                                           ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                           Clases                                            ║
║                                                                             ║
║                           Class (object) Padre                              ║
║                                                                             ║
║                           Objetos                  	                      ║
║                                  estado                                     ║
║                                  propiedades                                ║
║                                  comportamiento                             ║
║                                                                             ║
║                           Instancia                                         ║
║                                                                             ║
║                           Modularizacion                                    ║
║                                                                             ║
║                           Encapsulado                                       ║
║                                                                             ║
║                           Herencia                                          ║
║                                                                             ║
║                           Polimorfismo                                      ║
║                                                                             ║
║                           def funcion (general)                             ║
║                           def metodo (clase)                                ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                           Polimorfismo                                      ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://python-para-impacientes.blogspot.com/2014/02/programacion-orientada-objetos.html
https://www.youtube.com/watch?v=2UNrSiKEI8w
https://www.youtube.com/watch?v=Y_SiIgxc-xI

Un conjunto de caracteres que forman palabras, verbos, etc pueden generar oraciones,
estas parrafos, textos muy grandes divididos en capitulos, en libro, tomos, etc.
Todo depende de como lo reconozcamos. Como python toma la caracteristica del objeto
a partir de que contenga este y de alguna manera esto es subjetivo, dependiendo de como
lo tomo puedo aplicarle distintas acciones+
Un espacio de nombres es una relación de nombres a objetos.
Los objetos tienen individualidad, y múltiples nombres (en muchos ámbitos) pueden vincularse al mismo objeto. Esto se conoce como aliasing en otros lenguajes

Ejemplo pildoras informaticas video 32
https://www.youtube.com/watch?v=kV1cN_bqcSw&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=32
""")
class Coche():
	ruedas = 4
	ejes = 2
	def desplazamiento(self):
		print("Voy en 4 ruedas");
class Moto():
	ruedas = 2
	ejes = 2
	def desplazamiento(self):
		print("Voy en 2 ruedas");
class Camion():
	ruedas = 5
	ejes = 2
	def desplazamiento(self):
		print("Voy en 6 o mas ruedas");
class Monociclo():
	ruedas = 1
	ejes = 1
	def desplazamiento(self):
		print("no voy, me caigo");

def calcular_ruedas_en_el_camino(vehiculo):#<----------------------aca defino a la funcion a la que llamar y tranformo el dato en un objeto
	vehiculo.desplazamiento()#      ^
#       ^---------------------------+                  lo llamo desde un dato cargado en una variable
var = True
while var:
	ingreso=input ("EN QUE VIAJAS (Coche, Moto, Camion o Monociclo 'z para salir') ?:")
	if ingreso.upper()=="COCHE":
		calcular_ruedas_en_el_camino(Coche())
	elif ingreso.upper()=="MOTO":
		calcular_ruedas_en_el_camino(Moto())
	elif ingreso.upper()=="CAMION":
		calcular_ruedas_en_el_camino(Camion())
	elif ingreso.upper()=="MONOCICLO":
		calcular_ruedas_en_el_camino(Monociclo())
	elif ingreso.upper()=="Z":
		break
	else:
		print ("dato no valido :", ingreso.upper())

print("""
El polimorfismo es una propiedad de la herencia por la que objetos de distintas subclases pueden responder a una misma acción.
La polimorfia es implícita en Python, ya que todas las clases son subclases de una superclase común llamada Object.
""")
def rueda_auxilio(vehiculo, auxilio):
	if auxilio:
		vehiculo.ruedas = vehiculo.ruedas +1

print("""Gracias al polimorfismo no tenemos que comprobar si un objeto tiene o no el atributo pvp, simplemente intentamos acceder y si existe premio""")



def calcular_ruedas_auxilio(vehiculo,auxilio):#<----------------------aca defino a la funcion a la que llamar y tranformo el dato en un objeto
	if auxilio:
		print ("Antes"+str(vehiculo.ruedas)+" ruedas");
		vehiculo.ruedas = vehiculo.ruedas +1
		print("Ahora"+str(vehiculo.ruedas)+" ruedas");
		#                   ^---------------------------es una variable que carga un dato, nombre de un objeto

while var:
	ingreso=input ("Y la rueda de auxilio. modificar (Coche, Moto, Camion o Monociclo 'z para salir') ?:")
	if ingreso.upper()=="COCHE":
		calcular_ruedas_auxilio(Coche, "True")
	elif ingreso.upper()=="MOTO":
		calcular_ruedas_auxilio(Moto, "False")
	elif ingreso.upper()=="CAMION":
		calcular_ruedas_auxilio(Camion, "True")
	elif ingreso.upper()=="MONOCICLO":
		calcular_ruedas_auxilio(Monociclo, "False")
	elif ingreso.upper()=="Z":
		break
	else:
		print ("dato no valido :", ingreso.upper())
nuevo(1,"fin");
#################################################################

