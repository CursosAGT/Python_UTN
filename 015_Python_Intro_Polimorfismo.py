from Estructura import *
nuevo(0,"inicio");
##################################################################################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print('''
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
║                           Objetos                                           ║
║                                  self.                                      ║
║                                                                             ║
║                           Clases                                            ║
║                                  Atributos (del objeto)                     ║
║                                  métodos (funciones del objeto)             ║
║                                                                             ║
║                           Constructor                                       ║
║                                  __init__                                   ║
║                                  __str__                                    ║
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
║                               _oculta                                       ║
║                               __privada                                     ║
║                                                                             ║
║                           Herencia Simple y múltiple                        ║
║                           	Orden de herencia                             ║
║                               super()                                       ║
║                               isinstance                                    ║
║                                                                             ║
║                           Polimorfismo                                      ║
║                                                                             ║
║                           Abstracción                                       ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                           Polimorfismo                                      ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://python-para-impacientes.blogspot.com/2014/02/programacion-orientada-objetos.html
https://www.youtube.com/watch?v=2UNrSiKEI8w
https://www.youtube.com/watch?v=Y_SiIgxc-xI

Un conjunto de caracteres que forman palabras, verbos, etc pueden generar oraciones,estas párrafos, textos muy grandes divididos en capítulos, en libro, tomos, etc.
Todo depende de como lo reconozcamos. Como python toma la característica del objeto a partir de que contenga este y de alguna manera esto es subjetivo, dependiendo de como
lo tomo puedo aplicarle distintas acciones+
Un espacio de nombres es una relación de nombres a objetos.
Los objetos tienen individualidad, y múltiples nombres (en muchos ámbitos) pueden vincularse al mismo objeto. Esto se conoce como aliasing en otros lenguajes


La palabra polimorfismo, del latín polys morphos (varias formas), se refiere a la habilidad de objetos de distintas clases de responder al mismo mensaje.
Esto se puede conseguir a través de la herencia: un objeto de una clase derivada es al mismo tiempo un objeto de la clase padre, de forma que allí donde se requiere un objeto de la clase padre también se puede utilizar uno de la clase hija.
Python, al ser de tipado dinámico, no impone restricciones a los tipos que se le pueden pasar a una función, por ejemplo, más allá de que el objeto se comporte como se espera: si se va a llamar a un método f() del objeto pasado como parámetro, por ejemplo, evidentemente el objeto tendrá que contar con ese método.



Ejemplo pildoras informaticas video 32
https://www.youtube.com/watch?v=kV1cN_bqcSw&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=32
''')


nuevo(0,"iniciar");
##################################################################################################################################
#Ej polimorfismo 0
print('''duck typing''')

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
	ruedas = 6
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

print('''
El polimorfismo es una propiedad de la herencia por la que objetos de distintas subclases pueden responder a una misma acción.
La polimorfia es implícita en Python, ya que todas las clases son subclases de una superclase común llamada Object.
''')
def rueda_auxilio(vehiculo, auxilio):
	if auxilio:
		vehiculo.ruedas = vehiculo.ruedas +1

print('''Gracias al polimorfismo no tenemos que comprobar si un objeto tiene o no el atributo pvp, simplemente intentamos acceder y si existe premio''')



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

nuevo(1)
##################################################################################################################################
#Ej polimorfismo 2
class Turno_noche:
	def horario(self):
		print ("de 18 a 23")
class Turno_tarde:
	def horario(self):
		print ("de 12 a 18")
class Turno_mañana:
	def horario(self):
		print ("de 8 a 12")
def funcion_horarios(banda_horaria):
	banda_horaria.horario()
alumno_1 = Turno_mañana()
alumno_2 = Turno_tarde()
alumno_3 = Turno_noche()
alumno_4 = Turno_noche()
alumno_5 = Turno_mañana()
alumno_6 = Turno_mañana()
alumno_7 = Turno_tarde()

dato = int(input("ingrese el Nº alumno buscado (1 a 7)"))
if dato == 1 : funcion_horarios(alumno_1)
elif dato == 2 : funcion_horarios(alumno_2)
elif dato == 3 : funcion_horarios(alumno_3)
elif dato == 4 : funcion_horarios(alumno_4)
elif dato == 5 : funcion_horarios(alumno_5)
elif dato == 6 : funcion_horarios(alumno_6)
elif dato == 7 : funcion_horarios(alumno_7)
else: print("Alumno no encontrado")
nuevo(2);
##################################################################################################################################
#Ej polimorfismo 3
class Ensalada():
	'''documentación 'como hacer una ensalada' '''
	lista_ensalada=[]
	def __init__(self,elemento):
		'''documentación Estructura común a todo los elementos'''
		self.elemento_ensalada = elemento
		self.lista_ensalada.append(elemento)
	def Mezclar():
		'''documentación común a todo los elementos'''
		print(f"Mezclar: (acción general de clase) {Ensalada.lista_ensalada}")
	def Condimentar():
		'''documentación común a todo los elementos'''
		print(f"Condimento (acción general de clase) {Ensalada.lista_ensalada}")
class Tomate_hacer(Ensalada):
	'''documentación de como preparar los Tomates'''
	def Lavar (self):
		'''documentación de como se limpian los tomate'''
		print(f"Lavar {self.elemento_ensalada} con agua clorada")
	def Cortar (self):
		'''documentación de como se cortan los tomate'''
		print(f"Cortar {self.elemento_ensalada} en cubos")
	def hacer(self):
		self.Lavar()
		self.Cortar()
class Lechuga_hacer(Ensalada):
	'''documentación de como preparar las Lechugas'''
	def Lavar (self):
		'''documentación de como se limpian las Lechuga'''
		print(f"Lavar {self.elemento_ensalada} temojandola x 20 minutos con una gota de lavandina")
	def Cortar (self):
		'''documentación de como se cortan las Lechuga'''
		print(f"Cortar {self.elemento_ensalada} en tiras")
	def hacer(self):
		self.Lavar()
		self.Cortar()
class Cebolla_hacer(Ensalada):
	'''documentación de como preparar la Cebolla'''
	def Pelar (self):
		'''documentación de como se pelan las cebolla'''
		print(f"Pelar {self.elemento_ensalada}")
	def Lavar (self):
		'''documentación de como se limpian las cebolla'''
		print(f"Lavar {self.elemento_ensalada} que no quede antraz")
	def Cortar (self):
		'''documentación de como se cortan las cebolla'''
		print(f"Cortar {self.elemento_ensalada} en plumas")
	def hacer(self):
		self.Pelar()
		self.Lavar()
		self.Cortar()
class Huevos_hacer(Ensalada):
	'''documentación de como preparar los huevos'''
	def Lavar (self):
		'''documentación de como se limpian los huevos'''
		print(f"Lavar {self.elemento_ensalada} hasta sacar toda suciedad")
	def Hervir (self):
		'''documentación de como se Hierve los huevos'''
		print(f"Hervir {self.elemento_ensalada} durante 10 minutos")
	def Pelar (self):
		'''documentación de como se pelan los huevos'''
		print(f"Pelar {self.elemento_ensalada} debajo de un chorro de agua clorada")
	def Cortar (self):
		'''documentación de como se cortan los huevos'''
		print(f"Cortar {self.elemento_ensalada} ya hervidos en fetas")
	def hacer(self):
		self.Lavar()
		self.Hervir()
		self.Pelar()
		self.Cortar()
class Lentejas_hacer(Ensalada):
	def Lavar (self):
		'''documentación de como se limpian las lentejas'''
		print(f"Lavar {self.elemento_ensalada} varias veces reposo y saco otras semillas que se mezclaron")
	def Hervir (self):
		'''documentación de como se Hierve las lentejas'''
		print(f"Hervir {self.elemento_ensalada} hasta q esten blandas")
	def hacer(self):
		self.Lavar()
		self.Hervir()
primer_elemento = Lechuga_hacer("Lechuga")
primer_elemento.hacer()
print("~~~~~~~~~~~~~");
Segundo_elemento = Cebolla_hacer("Cebolla")
Segundo_elemento.hacer()
print("~~~~~~~~~~~~~");
tercer_elemento = Lentejas_hacer("Lentejas")
tercer_elemento.hacer()
print("~~~~~~~~~~~~~");
Cuarto_elemento = Tomate_hacer("Tomate")
Cuarto_elemento.hacer()
print("~~~~~~~~~~~~~");
Ensalada.Mezclar()
print("~~~~~~~~~~~~~");
quinto_elemento = Huevos_hacer("Huevos")
quinto_elemento.hacer()
print("~~~~~~~~~~~~~");
Ensalada.Condimentar()
print("~~~~~~~~~~~~~");
Ensalada.Mezclar()
print("~~~~~~~~~~~~~");
print(Ensalada.__doc__)
print(quinto_elemento.__doc__)
print(quinto_elemento.Lavar.__doc__)
print(quinto_elemento.Hervir.__doc__)
print(quinto_elemento.Pelar.__doc__)
print(quinto_elemento.Cortar.__doc__)

nuevo(3,"fin");
