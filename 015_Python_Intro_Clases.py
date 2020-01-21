from Estructura import *
nuevo(0,"inicio");
##################################################################################################################################
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
╚═════════════════════════════════════════════════════════════════════════════╝

https://python-para-impacientes.blogspot.com/2014/02/programacion-orientada-objetos.html
https://www.youtube.com/watch?v=2UNrSiKEI8w
https://www.youtube.com/watch?v=Y_SiIgxc-xI
""")
nuevo(0)
print("""

Para entender este paradigma primero tenemos que comprender qué es una clase y qué es un objeto. Un objeto es una entidad que agrupa un
estado y una funcionalidad relacionadas. El estado del objeto se define a través de variables llamadas 'atributos', mientras que la funcionalidad
se modela a través de funciones a las que se les conoce con el nombre de 'métodos' del objeto.


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
		return 'UTN 2020'

Clases_ejemplo.atributos (numero entero) y Clases_ejemplo.instancia (Función o Metodo).
Asignarcion exterior
	Clases_ejemplo.atributos = 2020
variable = Clases_ejemplo()

...crea una nueva instancia de la clase y asigna este objeto a la variable local "variable".

""")
nuevo(0);
##################################################################################################################################
#Ejercicio_Clases_01

print("""
La única operación que es entendida por los objetos instancia es la referencia de atributos.
Hay dos tipos de nombres de atributos válidos, atributos de datos y métodos.
Los atributos de datos son creados la primera vez que se les asigna algo.
Los atributos de método son funciones que "pertenecen a" un objeto instancia de clase.

class Clases_ejemplo:
	atributos_A = 1973
	atributos_M = 9
	atributos_D = 22
	def Hacer_Metodo(self):
		en_metodo = "UTN_2020"
		return (en_metodo)
""")
class Clases_ejemplo:
	atributos_A = 1973
	atributos_M = 9
	atributos_D = 22
	def Hacer_Metodo(self):
		en_metodo = "UTN_2020"
		return (en_metodo)
print("Desde la 'clases'  imprimo los atributos, aun no hay objetos instanciados")
print ("Clases_ejemplo.atributos_A",Clases_ejemplo.atributos_A)
print ("Clases_ejemplo.atributos_M",Clases_ejemplo.atributos_M)
print ("Clases_ejemplo.atributos_D",Clases_ejemplo.atributos_D)
print("Desde la 'clases'  llamo al metodo y como aun no hay objetos instanciados paso 0 como self")
print ("Clases_ejemplo.Hacer_Metodo(0)",Clases_ejemplo.Hacer_Metodo(0))
print("\n\n")

print("Mi primer objeto instanciado")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Obj_instanciado_1 = Clases_ejemplo()
print("Atributos desde el objetos 1 instanciado")
print ("Obj_instanciado_1.atributos_A",Obj_instanciado_1.atributos_A)
print ("Obj_instanciado_1.atributos_M",Obj_instanciado_1.atributos_M)
print ("Obj_instanciado_1.atributos_D",Obj_instanciado_1.atributos_D)
print("Metodo desde el objetos 1 instanciado")
print ("Obj_instanciado_1.Hacer_Metodo",Obj_instanciado_1.Hacer_Metodo())

vi = Obj_instanciado_1.Hacer_Metodo
print(vi())

print("Mi segundo objeto instanciado")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Obj_instanciado_2 = Clases_ejemplo()
print("Atributos desde el objetos 2 instanciado")
print ("Obj_instanciado_2.atributos_A",Obj_instanciado_2.atributos_A)
print ("Obj_instanciado_2.atributos_M",Obj_instanciado_2.atributos_M)
print ("Obj_instanciado_2.atributos_D",Obj_instanciado_2.atributos_D)
print("Metodo desde el objetos 2 instanciado")
print ("Obj_instanciado_2.Hacer_Metodo",Obj_instanciado_2.Hacer_Metodo())
pausa()
print("""
cambio x afuera de la funcion los valores de los atributos

Obj_instanciado_2.atributos_A=1999
Obj_instanciado_2.atributos_M=12
Obj_instanciado_2.atributos_D=31
""")
Obj_instanciado_2.atributos_A=1999
Obj_instanciado_2.atributos_M=12
Obj_instanciado_2.atributos_D=31

print("Mi segundo objeto modificado")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Atributos desde el objetos 2 instanciado")
print ("Obj_instanciado_2.atributos_A",Obj_instanciado_2.atributos_A)
print ("Obj_instanciado_2.atributos_M",Obj_instanciado_2.atributos_M)
print ("Obj_instanciado_2.atributos_D",Obj_instanciado_2.atributos_D)

pausa()
print("""
En nuestro ejemplo, variable.instancia es una referencia a un método válido, dado que Clases_ejemplo.instancia es una función, pero variable.atributos no lo es, dado que Clases_ejemplo.atributos no lo es.
Pero variable.instancia no es la misma cosa que Clases_ejemplo.instancia; es un objeto método, no un objeto función.


Características de la Programación Orientada a Objeto modelo de programación:

Abstracción
Se refiere a que un elemento pueda aislarse del resto de elementos y de su contexto para centrar el interés en lo qué hace y no en cómo lo hace (caja negra).

Modularidad
Es la capacidad de dividir una aplicación en partes más pequeñas independientes y reutilizables llamadas módulos.

Encapsulación
Consiste en reunir todos los elementos posibles de una entidad al mismo nivel de abstracción para aumentar la cohesión, contando con la posibilidad de ocultar los atributos de un objeto (en Python, sólo se ocultan en apariencia).

Herencia
se refiere a que una clase pueda heredar las características de una clase superior para obtener objetos similares. Se heredan tanto los atributos como los métodos. Éstos últimos pueden sobrescribirse para adaptarlos a las necesidades de la nueva clase. A la posibilidad de heredar atributos y métodos de varias clases se denomina Herencia Múltiple.

Polimorfismo
Alude a la posibilidad de identificar de la misma forma comportamientos similares asociados a objetos distintos. La idea es que se sigan siempre las mismas pautas aunque los objetos y los resultados sean otros.

Variables de Clases y Variables de Instancias
En lenguajes que crean objetos a partir de clases, un objeto es una instancia de una clase. Y de una misma clase se pueden mantener activas en un programa más de una instancia al mismo tiempo.
Una variable de clase es compartida por todas las instancias de una clase. Se definen dentro de la clase (después del encabezado de la clase) pero nunca dentro de un método. Este tipo de variables no se utilizan con tanta frecuencia como las variables de instancia.
Una variable de instancia se define dentro de un método y pertenece a un objeto determinado de la clase instanciada.

""")

nuevo(1);
##################################################################################################################################
#Ejercicio_Clases_02

print("""
Las clases las definimos  mediante la palabra clave class seguida del nombre de la clase con la primera letra en mayúscula y nunca un numero al comienzo.

El método __init__ (nombre por convención) se ejecuta al instanciar, crear un nuevo objeto desde una clase
Este se realiza automáticamente sin tener que llamarlo, su primer parámetro es siempre self. E indica que se referiere al objeto actual.
Imprescindible para luego poder acceder a los atributos y métodos del objeto diferenciando.
En este caso al ejecutarse inmediatamente al ingresar un objeto a la clase pide el método que enviemos el valor de entrenamiento del trabajador como parámetro obligatorio.

Para crear un objeto se escribiría el nombre de la clase seguido de cualquier parámetro que sea necesario entre paréntesis.
Estos parámetros son los que se pasarán al método __init__ , que como decíamos es el método que se llama al instanciar la clase.
Juan = Trabajo(15)# creo el objeto Juan con la clase trabajo y un valor de entrenamiento de 15 que es requerido por__init__
pero en def __init__(self, entrenamiento): hay 2 parámetros, self es el nombre del objeto que se crea y lo enviá python directamente sin tener que añadirlo entre los argumentos enviados a la clase y/o metodo

Ahora que ya hemos creado nuestro objeto, podemos acceder a sus
atributos y métodos mediante la sintaxis objeto.atributo y objeto.
metodo() :

	class Trabajo:
		def __init__(self,nombre,apellido, practicas_realizadas):#constructor
			self.gracia = nombre+","+apellido
			self.entrenamiento = practicas_realizadas
			print (f"{self.gracia} es un empleado con {self.entrenamiento} horas de entrenamiento")
		def Iniciar_trabajo(self):
			print("\tEtapa:")
			if self.entrenamiento >= 20:
				print (f"\t\t{self.gracia} es un empleado que termino sus hs de aprendizaje. Empieza a trabajar")
			else:
				print (f"\t\t{self.gracia} sigue en etapa de aprendizaje")
		def Definir_estado(self):
			print("---------------------------------------------")
			print("--------------Definir_estado-----------------")
			if self.entrenamiento < 20:
				print ("A ",self.gracia, " le quedan ", 20- self.entrenamiento, " horas de entrenamiento, ya tiene", self.entrenamiento, "hs")
				self.entrenamiento += 5
				print ("Agrego 5 hs de entrenamiento quedan ", 20- self.entrenamiento, " horas.")
			else:
				print ("Colocar al empleado en un cargo")
			self.Iniciar_trabajo()
""")

class Trabajo:
	def __init__(self,nombre,apellido, practicas_realizadas):#constructor
		self.gracia = nombre+","+apellido
		self.entrenamiento = practicas_realizadas
		print (f"{self.gracia} es un empleado con {self.entrenamiento} horas de entrenamiento")
	def Iniciar_trabajo(self):
		print("\tEtapa:")
		if self.entrenamiento >= 20:
			print (f"\t\t{self.gracia} es un empleado que termino sus hs de aprendizaje. Empieza a trabajar")
		else:
			print (f"\t\t{self.gracia} sigue en etapa de aprendizaje")
	def Definir_estado(self):
		print("---------------------------------------------")
		print("--------------Definir_estado-----------------")
		if self.entrenamiento < 20:
			print ("A ",self.gracia, " le quedan ", 20- self.entrenamiento, " horas de entrenamiento, ya tiene", self.entrenamiento, "hs")
			self.entrenamiento += 5
			print ("Agrego 5 hs de entrenamiento quedan ", 20- self.entrenamiento, " horas.")
		else:
			print ("Colocar al empleado en un cargo")
		self.Iniciar_trabajo()
print("Intanciamos 3 objetos con sus datos")
Empleado_1=Trabajo("Juan","XX",14)
Empleado_2=Trabajo("Pedro","YY",1)
Empleado_3=Trabajo("Luis","ZZ",21)
print("Definimos los 3 estados")
Empleado_1.Definir_estado()
Empleado_2.Definir_estado()
Empleado_3.Definir_estado()
print("Definimos los 3 estados")
Empleado_1.Definir_estado()
Empleado_2.Definir_estado()
Empleado_3.Definir_estado()

nuevo(2);
##################################################################################################################################
#Ejercicio_Clases_03
print("""
	class Complejo:
		def __init__(self, parte_real, parte_imaginaria):
			self.real = parte_real
			self.imag = parte_imaginaria

	variable = Complejo(3, "i")
	print ("raiz de -9 =",variable.real, variable.imag )
	""")
class Complejo:
	def __init__(self, parte_real, parte_imaginaria):
		self.real = parte_real
		self.imag = parte_imaginaria

variable = Complejo(3, "i")
print ("####################################")
print ("#\traiz de -9 =",variable.real, variable.imag )
print ("####################################")
print("""
Si aún no comprendés como funcionan los métodos, un vistazo a la implementación puede ayudar a clarificar este tema. Cuando se hace referencia un atributo de instancia y no es un atributo de datos, se busca dentro de su clase. Si el nombre denota un atributo de clase válido que es un objeto función, se crea un objeto método juntando (punteros a) el objeto instancia y el objeto función que ha sido encontrado. Este objeto abstracto creado de esta unión es el objeto método. Cuando el objeto método es llamado con una lista de argumentos, una lista de argumentos nueva es construida a partir del objeto instancia y la lista de argumentos original, y el objeto función es llamado con esta nueva lista de argumentos.
""")
nuevo(3);
##################################################################################################################################
#Ejercicio_Clases_04
class Bolsa:
	def __init__(self):
		self.datos = []
		self.cantidad=0
	def agregar(self):
		self.datos.append(1)
		self.cantidad=self.cantidad+1
	def agregar_varios(self, cant):
		for bucle in range (cant):
			self.agregar()

bags=Bolsa()

print("Fui a la panadería me dieron 1")
bags.agregar()
print("Fui al súper y me dieron 3")
bags.agregar_varios(3)
print("Fui a la farmacia y me dieron 1")
bags.agregar()
print("estructura de tipos de bolsas", bags.datos)
print("Cantidad total",bags.cantidad)
print("""
El método __init__ crea el objeto y luego lo inicializa, no es el constructor como tal,
El método __new__ sólo construye el objeto.
""")
nuevo(4);
##################################################################################################################################
#Ejercicio_Clases_05
print("""
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
	altura_en_Objeto_prog = 170
	peso_en_Objeto_prog = 80
	edad_en_Objeto_prog = 40
	piel_en_Objeto_prog = Piel() 		# Atributo de este objeto es otro objeto que posee varios atributos ( podría tener  métodos propios)
	ojo_en_Objeto_prog = Ojo()			# Atributo de este objeto es otro objeto que posee varios atributos ( podría tener  métodos propios)
	pelo_en_Objeto_prog = Pelo();
obj_desde_clase = Objeto_prog();
""")
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
	altura_en_Objeto_prog = 170
	peso_en_Objeto_prog = 80
	edad_en_Objeto_prog = 40
	piel_en_Objeto_prog = Piel() 		# Atributo de este objeto es otro objeto que posee varios atributos ( podría tener  métodos propios)
	ojo_en_Objeto_prog = Ojo()			# Atributo de este objeto es otro objeto que posee varios atributos ( podría tener  métodos propios)
	pelo_en_Objeto_prog = Pelo();
obj_desde_clase = Objeto_prog();
print ("muestro obj_desde_clase.edad_en_Objeto_prog :",obj_desde_clase.edad_en_Objeto_prog);
print ("muestro obj_desde_clase.altura_en_Objeto_prog :",obj_desde_clase.altura_en_Objeto_prog);
print ("muestro obj_desde_clase.pelo_en_Objeto_prog :",obj_desde_clase.pelo_en_Objeto_prog);# no es error es un objeto y este tienen no solo múltiples atributos sino que lleva métodos y no se pueden imprimir
print  ("muestro obj_desde_clase.pelo_en_Objeto_prog -  es un objeto dentro de un objeto que podría contener múltiples atributos y métodos por eso no se pueden mostrar")
pausa()
print  ("\nmuestro obj_desde_clase.pelo_en_Objeto_prog.color -  es un atributo de un objeto dentro de un objeto se pueden mostrar")
print ("muestro obj_desde_clase.pelo_en_Objeto_prog.color :",obj_desde_clase.pelo_en_Objeto_prog.color);
print ("muestro obj_desde_clase.pelo_en_Objeto_prog.largo :",obj_desde_clase.pelo_en_Objeto_prog.largo);
print("\n")
obj_desde_clase.pelo_en_Objeto_prog = "se pelo"# aca destruyo la herencia. impongo un valor al objeto
print('grabo obj_desde_clase.pelo_en_Objeto_prog = "se pelo" \n')
print ("muestro obj_desde_clase.pelo_en_Objeto_prog :",obj_desde_clase.pelo_en_Objeto_prog);# ver q es igual a la linea del supuesto error
print('Ya no hereda de la clases pelo. ese dato es reemplazado por "se pelo" así que no hay mas color ni largo')
nuevo(5);
##################################################################################################################################
#Ejercicio_Clases_06
print ("""
__init__ is called when ever an object of the class is constructed.
That means when ever we will create a student object we will see the message "A student object is created" in the prompt.
You can see the first argument to the method is self. It is a special variable which points to the current object (like this in C++).
The object is passed implicitly to every method available in it, but we have to get it explicitly in every method while writing the methods.
Example shown below. Remember to declare all the possible attributes in the __init__ method itself.
Even if you are not using them right away, you can always assign them as None.
	class Alumno():
		numalumnos = 0
		sumanotas = 0

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
""")
nuevo(0)
class Alumno():
#    'Clase para alumnos'
	numalumnos = 0
	sumanotas = 0
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
print(alumno1.nombre)  					# María
print(alumno1.nota)  					# 8
print("Para modificar la variable de un objeto se utiliza la misma notación para referirse al atributo y después del signo igual (=) se indica la nueva asignación:");
alumno1.nombre = "Carmela"
print("Para acceder a las variables de la clase se sigue la misma notación pero en vez de indicar el nombre del objeto se indica el nombre de la clase instanciada.");
print("cantidad de alumnos: ",Alumno.numalumnos)  # 2
print("promedio de notas: ",Alumno.sumanotas/Alumno.numalumnos, " o ", Alumno.mostrarNotaMedia)  #
print("Para llamar a un método se indica el nombre de objeto, seguido de un punto y el nombre del método. Si se requieren varios argumentos se pasan escribiéndolos entre paréntesis, separados por comas (","). Si no es necesario pasar argumentos se añaden los paréntesis vacíos '()' al nombre del método.");
print(alumno1.mostrarNombreNota())  	# ('Carmela', 8);
print(alumno2.mostrarNombreNota())  	# ('Carlos', 6);
print("Para suprimir un atributo:");
del alumno1.nombre						# Para suprimir un atributo
#print(alumno1.mostrarNombreNota())		# ('Carmela', 8); da un error
print(alumno2.mostrarNombreNota())  	# ('Carlos', 6);
print("Si a continuación, se intenta acceder al valor del atributo borrado o se llama a algún método que lo utilice, se producirá la siguiente excepción:");
print("print(alumno1.mostrarNombreNota())");
print ("se generara el siguiente error 'AttributeError: 'Alumno' object has no attribute 'nombre'");
print("Pare crear nuevamente el atributo realizar una nueva asignación:");
alumno1.nombre = "Carmen"
alumno1.nota = 10
print(alumno1.mostrarNombreNota())		# ('Carmen', 10);
print(alumno2.mostrarNombreNota())		# ('Carlos', 6);

print("cantidad de alumnos: ",Alumno.numalumnos)  # 2


print("promedio de notas: ",Alumno.sumanotas/Alumno.numalumnos, " o ", Alumno.mostrarNotaMedia)  #
print("Esto es un error x q el promedio seria 8. Pero yo al no crear un nuevo alumno no actualice la suma de notas")

nuevo(6);
##################################################################################################################################
#Ejercicio_Clases_07

class Box:
	def __init__(self,nombre, altura, largo, ancho):
		self.nombre= nombre.capitalize();
		self.altura = float(altura);
		self.largo = float(largo);
		self.ancho = float(ancho);
		self.val_volumen=0
		self.val_base=0
	def volumen(self):
		self.val_volumen = self.altura * self.largo *self.ancho;
		return (self.val_volumen)
	def base(self):
		self.val_base =  self.largo *self.ancho;
		return (self.val_base)
	def datos(self):
		return (f"\nEl articulo {self.nombre} tiene un largo de {self.largo} un ancho de {self.ancho}y una altura de {self.altura} \n" \
				f"\tEl volumen es de {self.val_volumen} cm^3 con una base de {self.val_base} cm^2")

ejemplo1= Box("caja_med",20,20,30)#<--------------------------------ejemplo1 sera self al entrar a la funcion
print (f"El volumen que ocupa la unidad buscada es de "+ str(ejemplo1.volumen())+" cm^3");
print (f"La superficie que ocupa la unidad buscada es de "+ str(ejemplo1.base())+" cm^2");
print("--------------------------")
ejemplo2= Box("caja_chica",10,15,10)#<--------------------------------ejemplo2 sera self al entrar a la funcion
print (f"El volumen que ocupa la unidad buscada es de "+ str(ejemplo2.volumen())+" cm^3");
print (f"La superficie que ocupa la unidad buscada es de "+ str(ejemplo2.base())+" cm^2");
print("--------------------------")
ejemplo3= Box("caja_grande",50,30,20)#<--------------------------------ejemplo3 sera self al entrar a la funcion
print (f"El volumen que ocupa la unidad buscada es de "+ str(ejemplo3.volumen())+" cm^3");
print (f"La superficie que ocupa la unidad buscada es de "+ str(ejemplo3.base())+" cm^2");
#cada ejemplo es ina instancia u objeto. aqui instanciamos 3 objetos
print("--------------------------")

print ("ejemplo1.datos()",ejemplo1.datos())
print("--------------------------")
print ("ejemplo2.datos()",ejemplo2.datos())
print("--------------------------")
print ("ejemplo3.datos()",ejemplo3.datos())
print("--------------------------")
nuevo(7);
##################################################################################################################################
#Ejercicio_Clases_08
import datetime
class stock_general:
	def __init__(self,codigo,nombre,stock,descripcion):
		self.codigo = codigo
		self.nombre = nombre
		self.stock = stock
		self.descripcion = descripcion
	def __str__(self):
		return  f"LUGAR\t\t{self.__class__.__name__}\n" \
				f"REFERENCIA\t {self.codigo}\n" \
				f"NOMBRE\t\t {self.nombre}\n" \
				f"STOCK\t\t {self.stock}\n" \
				f"DESCRIPCIÓN\t {self.descripcion}\n"

class almacen_1(stock_general):#creo una clase que hereda de productos
	pass# como no la puedo dejar vaciá coloco la sentencia pass
class almacen_2(stock_general):#creo una clase que hereda de productos
	pass# como no la puedo dejar vaciá coloco la sentencia pass
item1 = almacen_2("xx2034yy", "Vaso",15, "Vaso de porcelana 50 cc, color blanco con dibujos")
item2 = almacen_2("25cc25cxc", "copa",50, "Copa cristal x 6 unidades, cristal")
item3 = almacen_2("sad122", "plato",25, "Plato  x 6 unidades, Blanco")
print(item1)
limpiar()
"""https://docs.hektorprofe.net/python/herencia-en-la-poo/herencia/"""
print("~~~~~~~~~~~~~~2da parte~~~~~~~~~~~~~~~~~~~~~~")
prod=[item1,item2]
prod.append(item3)#me olvide uno :(

item4 = almacen_1("ss123", "silla",600, "silla x 6 unidades, Negro")
prod.append(item4)
item5 = almacen_1("mm147", "mesa",500, "mesa  x 1 unidad, Negro")
prod.append(item5)
item6 = almacen_1("s258s", "sillon",250, "sillon  x 1 unidad, Negro")
prod.append(item6)
for productos in prod:
	print(productos )#ver def __str__ en class productos
	print("Item: ",productos.nombre)
	if( isinstance(productos, stock_general) ):
		print(f"En stock_general hay {productos.stock} unidades de { productos.nombre} con codigo {productos.codigo}")
	if( isinstance(productos, almacen_1) ):
		print(F"Ubicadas en {productos.__class__.__name__,} direccion xxx\n")
	elif( isinstance(productos, almacen_2) ):
		print(F"Ubicadas en {productos.__class__.__name__,} direcciom zzz\n")
	print("\n==========================")
#veremos este ejercicio mejorado con herencias
print("veremos este ejercicio mejorado con herencias")
nuevo(8);
##################################################################################################################################
#Ejercicio_Clases_09

from copy import copy
class Test:
    pass
print(" tener en cuenta que se cambia y que resultados dan estos cambios a la imagen")
test1 = Test()
test2 = test1#observar

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
except Exception as error_tipo:
    print(error_tipo)
print("\n------from copy import copy --------------------------------")
print(" tener en cuenta que se cambia y que resiltados dan estos cambios a la imagen")
test1 = Test()
test2 = copy(test1)#observar

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

nuevo(9,"fin");
##################################################################################################################################
print("""
aliasing
"Los objetos tienen individualidad, y múltiples nombres (en muchos ámbitos) pueden vincularse al mismo objeto. Esto se conoce como aliasing en otros lenguajes. Normalmente no se aprecia esto a primera vista en Python, y puede ignorarse sin problemas cuando se maneja tipos básicos inmutables (números, cadenas, tuplas). Sin embargo, el aliasing, o renombrado, tiene un efecto posiblemente sorpresivo sobre la semántica de código Python que involucra objetos mutables como listas, diccionarios, y la mayoría de otros tipos. Esto se usa normalmente para beneficio del programa, ya que los renombres funcionan como punteros en algunos aspectos. Por ejemplo, pasar un objeto es barato ya que la implementación solamente pasa el puntero; y si una función modifica el objeto que fue pasado, el que la llama verá el cambio; esto elimina la necesidad de tener dos formas diferentes de pasar argumentos, como en Pascal
.""")
