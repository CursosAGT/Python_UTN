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


https://python-para-impacientes.blogspot.com/2014/02/programacion-orientada-objetos.html
https://www.youtube.com/watch?v=2UNrSiKEI8w
https://www.youtube.com/watch?v=Y_SiIgxc-xI
TIPS
Un espacio de nombres es una relación de nombres a objetos.
Cualquier cosa después de un punto es un atributo
Las referencias a nombres en módulos son referencias a atributos:
Ej en la expresión modulo.funcion, modulo es un "objeto módulo" y funcion es un "atributo" de este objeto
Un ámbito es una región textual de un programa en Python donde un espacio de nombres es accesible directamente.
Cuando se ingresa una definición de clase, se crea un nuevo espacio de nombres, el cual se usa como ámbito local;
por lo tanto, todas las asignaciones a variables locales van a este nuevo espacio de nombres.
En particular, las definiciones de funciones asocian el nombre de las funciones nuevas allí.
Una clase se finaliza normalmente se crea un objeto clase que envuelve los contenidos del espacio de nombres creado por la definición de la clase en el ambito
Este objeto clase se asocia al ambito logal original bajo el nombre que se le puso a la clase en el encabezado de su definición (Class Clases_ejemplo).
Los objetos clase soportan dos tipos de operaciones: hacer referencia a atributos e instanciación.

class Clases_ejemplo():
	atributos = 1973
	def instancia(self):
		return 'UTN 2019'

Clases_ejemplo.atributos (numero entero) y Clases_ejemplo.instancia (Función o Metodo).
Asignarcion exterior
	Clases_ejemplo.atributos = 2020
variable = Clases_ejemplo()

...crea una nueva instancia de la clase y asigna este objeto a la variable local "variable".

""")
nuevo(0,"inicio");
#################################################################
#Clase_Clases_01
class Clases_ejemplo:
	atributos = 1973
	def instancia(self):
		return 'UTN 2019'
variable = Clases_ejemplo()
print (variable.atributos)
print (Clases_ejemplo.atributos)
print (variable.instancia())
print (Clases_ejemplo.instancia(0))
vi = variable.instancia
print(vi())
print("""
La única operación que es entendida por los objetos instancia es la referencia de atributos.
Hay dos tipos de nombres de atributos válidos, atributos de datos y métodos.
Los atributos de datos son creados la primera vez que se les asigna algo.
Los atributos de método son funciones que “pertenecen a” un objeto instancia de clase.

class Clases_ejemplo:
	atributos = 1973
	def instancia(self):
		return 'UTN 2019'
variable = Clases_ejemplo()
print (variable.atributos)
print (variable.instancia)
print (input("		continuar?"));
een nuestro ejemplo, variable.instancia es una referencia a un método válido, dado que Clases_ejemplo.instancia es una función, pero variable.atributos no lo es, dado que Clases_ejemplo.atributos no lo es.
Pero variable.instancia no es la misma cosa que Clases_ejemplo.instancia; es un objeto método, no un objeto función.
""")
nuevo(1);
#################################################################
#Clase_Clases_02
class Complejo:
	def __init__(self, parte_real, parte_imaginaria):
		self.real = parte_real
		self.imag = parte_imaginaria

variable = Complejo(3.0, -4.5)
print (variable.real, variable.imag)
print("""
Si aún no comprendés como funcionan los métodos, un vistazo a la implementación puede ayudar a clarificar este tema. Cuando se hace referencia un atributo de instancia y no es un atributo de datos, se busca dentro de su clase. Si el nombre denota un atributo de clase válido que es un objeto función, se crea un objeto método juntando (punteros a) el objeto instancia y el objeto función que ha sido encontrado. Este objeto abstracto creado de esta unión es el objeto método. Cuando el objeto método es llamado con una lista de argumentos, una lista de argumentos nueva es construida a partir del objeto instancia y la lista de argumentos original, y el objeto función es llamado con esta nueva lista de argumentos.
""")
nuevo(2);
#################################################################
#Clase_Clases_03
class Bolsa:
	def __init__(self):
		self.datos = []
	def agregar(self, x):
		self.datos.append(x)
	def dobleagregar(self, x):
		self.agregar(x)
		self.agregar(x)
print("""

El método __init__ crea el objeto y luego lo inicializa, no es el constructor como tal,
El método __new__ sólo construye el objeto.
""")
nuevo(3);
#################################################################
#Clase_Clases_04
class Piel():
	color = "verde"
	textura = "pinchuda"

class Pelo():
	color = "azul"
	largo = 100

class Ojo():
	forma = "oblicua"
	color = "purpura"

class Objeto_prog():
	altura = 170
	peso = 80
	edad = 40
	piel_o = Piel() 	# propiedad compuesta por el objeto Objeto_prog piel
	ojo_o = Ojo()       # propiedad compuesta por el objeto Objeto_prog Ojo
	pelo_o = Pelo();
obj_desde_clase = Objeto_prog();
print (obj_desde_clase.edad);
print (obj_desde_clase.altura);
print (obj_desde_clase.pelo_o);
print (obj_desde_clase.pelo_o.color);
print (obj_desde_clase.pelo_o.largo);
obj_desde_clase.pelo_o = "rosa"
print (obj_desde_clase.pelo_o);
nuevo(4);
#################################################################
#Clase_Clases_05
print ("""
__init__ is called when ever an object of the class is constructed.
That means when ever we will create a student object we will see the message “A student object is created” in the prompt.
You can see the first argument to the method is self. It is a special variable which points to the current object (like this in C++).
The object is passed implicitly to every method available in it, but we have to get it explicitly in every method while writing the methods.
Example shown below. Remember to declare all the possible attributes in the __init__ method itself.
Even if you are not using them right away, you can always assign them as None.""")
class Alumno():
#    'Clase para alumnos'
	numalumnos = 0
	sumanotas = 0

#	print("__init__ is a special method in Python classes, it is the constructor method for a class.")
	def __init__(self, nombre, nota):
		self.nombre = nombre
		self.nota = nota
		Alumno.numalumnos += 1
		Alumno.sumanotas += nota

	def mostrarNombreNota(self):
		return(self.nombre, self.nota);

	def mostrarNumAlumnos(self):
		return(Alumno.numalumnos);

	def mostrarSumaNotas(self):
		return(Alumno.sumanotas);

	def mostrarNotaMedia(self):
		if Alumno.numalumnos > 0:
			return(Alumno.sumanotas/Alumno.numalumnos);
		else:
			return("Sin alumnos");

print("Crear objetos (instancias) de una clase");
print("#Para crear instancias de una clase se llama a la clase por su propio nombre pasando los argumentos que requiera el método constructor __init__ si existe.");
alumno1 = Alumno("Maria", 8);
alumno2 = Alumno("Carlos", 6);
print("Todos los argumentos se pasan escribiéndolos entre paréntesis y separados por comas ('',''). El primer argumento self se omite porque su valor es una referencia al objeto y es implícito para todos los métodos.");
print("Accediendo a los atributos y llamando a los métodos");
print("Para acceder a la variable de un objeto se indica el nombre del objeto, seguido de un punto y el nombre de la variable:");
print(alumno1.nombre)  # María
print(alumno1.nota)  # 8
print("Para modificar la variable de un objeto se utiliza la misma notación para referirse al atributo y después del signo igual (=) se indica la nueva asignación:");
alumno1.nombre = "Carmela"
print("Para acceder a las variables de la clase se sigue la misma notación pero en vez de indicar el nombre del objeto se indica el nombre de la clase instanciada.");
print(Alumno.numalumnos)  # 2
print(Alumno.sumanotas)  # 14
print("Para llamar a un método se indica el nombre de objeto, seguido de un punto y el nombre del método. Si se requieren varios argumentos se pasan escribiéndolos entre paréntesis, separados por comas (","). Si no es necesario pasar argumentos se añaden los paréntesis vacíos '()' al nombre del método.");
print(alumno1.mostrarNombreNota())  # ('Carmen', 8);
print(alumno2.mostrarNombreNota())  # ('Carlos', 6);
print("Para suprimir un atributo:");
del alumno1.nombre
print("Si a continuación, se intenta acceder al valor del atributo borrado o se llama a algún método que lo utilice, se producirá la siguiente excepción:");
print("print(alumno1.mostrarNombreNota())");
print ("se generara el siguiente error 'AttributeError: 'Alumno' object has no attribute 'nombre'");
print("Pare crear nuevamente el atributo realizar una nueva asignación:");
alumno1.nombre = "Carmen"
nuevo(5);
#################################################################
#Clase_Clases_06

class Box:
	def __init__(self, altura, largo, ancho):
		self.altura = altura;
		self.largo = largo;
		self.ancho = ancho;
		self.val_volumen=0
		self.val_base=0
	def volumen(self):
		self.val_volumen = self.altura * self.largo *self.ancho;
		return (self.val_volumen)
	def base(self):
		self.val_base =  self.largo *self.ancho;
		return (self.val_base)
ejemplo1= Box(20,20,30)#<--------------------------------ejemplo1 sera self al entrar a la funcion
print (f"El volumen que ocupla la unidad buscada es de "+ str(ejemplo1.volumen())+" cm^3");
print (f"La superficie que ocupla la unidad buscada es de "+ str(ejemplo1.base())+" cm^2");

ejemplo2= Box(10,15,10)#<--------------------------------ejemplo2 sera self al entrar a la funcion
print (f"El volumen que ocupla la unidad buscada es de "+ str(ejemplo2.volumen())+" cm^3");
print (f"La superficie que ocupla la unidad buscada es de "+ str(ejemplo2.base())+" cm^2");

ejemplo3= Box(50,30,20)#<--------------------------------ejemplo3 sera self al entrar a la funcion
print (f"El volumen que ocupla la unidad buscada es de "+ str(ejemplo3.volumen())+" cm^3");
print (f"La superficie que ocupla la unidad buscada es de "+ str(ejemplo3.base())+" cm^2");
#cada ejemplo es ina instancia u objeto. aqui instanciamos 3 objetos

nuevo(6);
#################################################################
#Clase_Clases_07

class Producto:
	def __init__(self,codigo,nombre,stock,descripcion):
		self.codigo = codigo
		self.nombre = nombre
		self.stock = stock
		self.descripcion = descripcion

	def __str__(self):
		return f"REFERENCIA\t {self.codigo}\n" \
			   f"NOMBRE\t\t {self.nombre}\n" \
			   f"STOCK\t\t {self.stock}\n" \
			   f"DESCRIPCIÓN\t {self.descripcion}\n"
class almacen_1(Producto):
	pass

item1 = Producto("xx2034yy", "Vaso",15, "Vaso de porcelana 50 cc, color blanco con dibujos")
item2 = Producto("25cc25cxc", "copa",50, "Copa cristal x 6 unidades, cristal")
item3 = Producto("sad122", "plato",25, "Plato  x 6 unidades, Blanco")
print(item1)
"""https://docs.hektorprofe.net/python/herencia-en-la-poo/herencia/"""
prod=[item1,item2]
prod.append(item3)

for prod in prod:
	print(prod, "\n----------------------------")
	print(prod.nombre, "\n----------------------------")
	if( isinstance(prod, Producto) ):
		print(prod.codigo, prod.nombre, "\n----------------------------")
nuevo(7);
#################################################################
#Clase_Clases_08
from copy import copy
class Test:
    pass

test1 = Test()
test2 = test1

print("test2 == test1 :-->",test2 == test1)  # ¿Son el mismo objeto?



test1.algo = "zzz"#-------------------ver el orden primero test1 con zzz
test2.algo = "yyy"#-------------------ver el orden ultimo  test2 con yyy
print("test1.algo :-->",test1.algo)
print("test2.algo :-->",test2.algo)
print("test2 == test1 :-->",test2 == test1)  # ¿Son el mismo objeto?

test1.algo = "yyy"#-------------------ver el orden primero test1 con yyy
test2.algo = "zzz"#-------------------ver el orden ultimo  test2 con zzz
print("test1.algo :-->",test1.algo)
print("test2.algo :-->",test2.algo)
print("test2 == test1 :-->",test2 == test1)  # ¿Son el mismo objeto?
try:
    print("test1",test1.algo)
    print("test2",test2.algo)
except Exception as e:
    print(e)
print("\n------from copy import copy --------------------------------")
test1 = Test()
test2 = copy(test1)

print("test2 == test1 :-->",test2 == test1)  # ¿Son el mismo objeto?

test1.algo = "zzz"#-------------------ver el orden primero test1 con zzz
test2.algo = "yyy"#-------------------ver el orden ultimo  test2 con yyy
print("test1.algo :-->",test1.algo)
print("test2.algo :-->",test2.algo)
print("test2 == test1 :-->",test2 == test1)  # ¿Son el mismo objeto?

test1.algo = "yyy"#-------------------ver el orden primero test1 con yyy
test2.algo = "zzz"#-------------------ver el orden ultimo  test2 con zzz
print("test1.algo :-->",test1.algo)
print("test2.algo :-->",test2.algo)
print("test2 == test1 :-->",test2 == test1)  # ¿Son el mismo objeto?
test1.algo = None

try:
    print("test1",test1.algo)
    print("test2",test2.algo)
except Exception as e:
    print(e)

nuevo(6,"fin");
#################################################################
