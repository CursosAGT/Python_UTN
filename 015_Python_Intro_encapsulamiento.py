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
	╚═════════════════════════════════════════════════════════════════════════════╝
	La encapsulación se refiere a impedir el acceso a determinados métodos y atributos de los objetos estableciendo así qué puede utilizarse
	desde fuera de la clase.

	En Python suele hacer es que el acceso a una variable o función sea privada o pública si viene determinado por
	su nombre si es o no precedido con dos guiones bajos "__xxxxxxx o __yyyyyy():"
	(NOTA: no debe terminar también con otros dos guiones bajos ya que los métodos cuyo nombre comienza y termina con dos guiones bajos
	(__init__(self, args), __del__(self),__new__(cls, args),__str__(self),__cmp__(self, otro),__len__(self),etc.)
	son métodos especiales que Python llama automáticamente bajo ciertas circunstancias.)


	class Ejemplo:
		def publico(self):
			print ("Publico")
		def __privado(self):
			print ("Privado")
	ej = Ejemplo()
	ej.publico()
	ej.__privado()#<---------------------------error

	""")
nuevo(0,"inicio");
print("""
Las variables que comienzan por un guion bajo (_foo) son consideradas privadas.  Su nombre indica a otros programadores que no son publicas:  son un detalle de implementación del que no se puede depender — entre otras cosas porque podrían desaparecer en cualquier momento

""")
class Objeto(object):
	def __init__(self, nombre, secreto):
		self.nombre = nombre
		self._secreto = secreto
objeto_1 = Objeto("Pepe", "canta en la ducha")
print ("Secreto:", objeto_1._secreto)
objeto_1._secreto = "no se baña"
print ("Secreto:", objeto_1._secreto)
limpiar()
print("""
Dos guiones bajos al comienzo del nombre (__spam) llevan el ocultamiento un paso mas allá, enmarañando(name-mangling) la variable de forma que sea mas difícil verla desde fuera
""")
class Objeto(object):
	def __init__(self, nombre, secreto):
		self.nombre = nombre
		self.__secreto = secreto
objeto_1 = Objeto("Pepe", "canta en la ducha")
print ("Secreto:", objeto_1._secreto)
objeto_1.__secreto = "no se baña"
print ("Secreto:", objeto_1._secreto)



#################################################################
#Ejercicio_Clases_01
class ejemplo():
	def __init__(self):
		self.para_todos="every body"
		self.__para_pocos="Algunos pocos"
	def metodo_para_todos(self):
		print("Accediste a un lugar sin seguridad")
	def __metodo_para_pocos(self):
		print("Accediste a un lugar con seguridad")
	def get_mostrar__metodo_para_pocos(self):
		return self.__para_pocos
	def set_Cargar__metodo_para_pocos(self, valor):
		self.__para_pocos = valor.upper()
		return self.__para_pocos
Elemento1=ejemplo()

print (Elemento1.para_todos)
#print (Elemento1.__para_pocos)#error<--------------------ver que no existe y comentar
try:
	print (Elemento1.__para_pocos)#error<--------------------ver que no existe y comentar
except(AttributeError,TypeError):
	print("Error, no existe",TypeError )
print("~~~~metodos~~~~")
Elemento1.metodo_para_todos()
#Elemento1.metodo_para_pocos()#error<--------------------ver que no existe y comentar
try:
	Elemento1.metodo_para_pocos()#error<--------------------ver que no existe y comentar
except(AttributeError,TypeError):
	print("Error, no existe",TypeError )
Elemento1._ejemplo__metodo_para_pocos()

print("~~~~modif_un_atributo_privado~~~~")
print ("como acceder a un metodo privado")


print ("antes :",Elemento1.get_mostrar__metodo_para_pocos())
Elemento1.set_Cargar__metodo_para_pocos("solo los que yo quiera")
print ("despues :",Elemento1.get_mostrar__metodo_para_pocos())

nuevo(1);
#################################################################
#Ejercicio_Clases_02
class Mascota:
	def __init__(self,nombre, especie=None, raza=None, patas=4,  edad=None):
		self.nombre=nombre;
		self.especie=especie;
		self.raza=raza;
		self.patas=patas;#self.__patas=patas;-------------------------------------cambios
		self.edad=edad;
	def nombrar(self, dato_nombre):
		self.nombre =dato_nombre;
	def datar(self,especie=None, raza=None, patas=4, nombre=None, edad=None):
		self.especie=especie;
		self.raza=raza;
		self.patas=patas;#self.__patas=patas;-------------------------------------cambios
		self.nombre=nombre;
		self.edad=edad;
	def mostrar(self):
		print (f"Mi  mascota tiene las sig caracteristicas: ",self.especie,self.raza,self.patas,self.nombre,self.edad);
		#                                                                            self.__patas-------------------------------------cambios
perro= Mascota("Wanda","Can","Weimaraner",4,6)
gato1= Mascota("Manchas","Felino","calle",4,5)
gato2 =Mascota("Grey")
perro.mostrar()
gato1.mostrar()
gato2.mostrar()
gato2.nombre="Grey"
gato2.especie="Felino"
gato2.raza="calle"
gato2.patas=4
gato2.edad=2
gato2.mostrar()
x=input("cuntinuar?")
gato2.nombre="Grey"
gato2.especie="Felino"
gato2.raza="calle"
gato2.patas=8#<---------------------------¿como?  esta modificacion se hace desde afuera de la clase
gato2.edad=200#<--------------------------¿como?  esta modificacion se hace desde afuera de la clase
gato2.mostrar()

x=input("cuntinuar?")
gato2.datar (nombre="Grey", especie="Felino", raza="calle", patas=4,  edad=2)#esta modificacion se hace desde un metodo interno de la clase
gato2.mostrar()
gato2.datar (nombre="Grey", especie="Felino", raza="angora", patas=8,  edad=2)#esta modificacion se hace desde un metodo interno de la clase
#                                                                  ^
#                                                                  |______________¿como?
gato2.mostrar()

nuevo(2);
#################################################################
#Ejercicio_Clases_03
class Mascota2:
	def __init__(self,nombre, especie=None, raza=None, patas=4,  edad=None):
		self.nombre=nombre;
		self.especie=especie;
		self.raza=raza;
		self.__patas=patas;#self.patas=patas------------------------------encapsulado
		self.edad=edad;
	def nombrar2(self, dato_nombre):
		self.nombre =dato_nombre;
	def datar2(self,especie=None, raza=None, patas=4, nombre=None, edad=None):
		self.especie=especie;
		self.raza=raza;
		self.__patas=patas;#self.patas=patas------------------------------encapsulado
		self.nombre=nombre;
		self.edad=edad;
	def mostrar2(self):
		print (f"Mi  mascota tiene las sig caracteristicas: ",self.especie,self.raza,self.__patas,self.nombre,self.edad);
		#                                                                            self.patas-------------------------------------cambios
perro= Mascota2("Wanda","Can","Weimaraner",4,6)
gato1= Mascota2("Manchas","Felino","calle",4,5)
gato2 =Mascota2("Grey")
perro.mostrar2()
gato1.mostrar2()
gato2.mostrar2()
gato2.nombre="Grey"
gato2.especie="Felino"
gato2.raza="calle"
gato2.patas=4
gato2.edad=2
gato2.mostrar2()
x=input("cuntinuar?")
gato2.nombre="Grey"
gato2.especie="Felino"
gato2.raza="calle"
gato2.patas=8#<---------------------------¿como?  esta modificacion se hace desde afuera de la clase
gato2.edad=200#<--------------------------¿como?  esta modificacion se hace desde afuera de la clase
gato2.mostrar2()

x=input("cuntinuar?")
gato2.datar2 (nombre="Grey", especie="Felino", raza="calle", patas=4,  edad=2)#esta modificacion se hace desde un metodo interno de la clase
gato2.mostrar2()
gato2.datar2 (nombre="Grey", especie="Felino", raza="angora", patas=8,  edad=2)#esta modificacion se hace desde un metodo interno de la clase
#                                                                  ^
#                                                                  |______________¿como?
gato2.mostrar2()

nuevo(3,"fin");
#################################################################

