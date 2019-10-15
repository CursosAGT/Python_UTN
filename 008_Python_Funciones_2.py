from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
	print("""
	╔═════════════════════════════════════════════════════════════════════════════╗
	║                                                                             ║
	║                              Funciones y Metodos                            ║
	║                              -------------------                            ║
	║                                                                             ║
	║          Funciones    Description                                           ║
	║                   lambda                                                    ║
	║                                                                             ║
	║                                                                             ║
	║          Metodos son finciones dentro de clases donde se deberia instanciar ║
	║                   a la clase con self nombre_objeto                         ║
	║                                                                             ║
	╠═════════════════════════════════════════════════════════════════════════════╣
	║                                                                             ║
	║                              Funciones,  Metodos                            ║
	║                                  y Generadores                              ║
	║                                                                             ║
	╚═════════════════════════════════════════════════════════════════════════════╝

	https://www.w3schools.com/python/python_ref_list.asp
	https://www.w3schools.com/python/python_lists.asp
	https://python-para-impacientes.blogspot.com/2014/02/programacion-funcional-funciones-de.html
	https://python-para-impacientes.blogspot.com/2014/02/funciones.html
	""")
	nuevo(0,"inicio");
	#################################################################
	#Ejercicio_Funciones_Ej_001
	print("""
	╔═════════════════════════════════════════════════════════════════════════════╗
	║                                                                             ║
	║                              Funciones,  Metodos                            ║
	║                                                                             ║
	╚═════════════════════════════════════════════════════════════════════════════╝
	""")
	#                          como función
	def funcion (var_1, var_2):
		return  (var_1 * var_2)
	print ("Función directa :",funcion (3,6))
	mi_array=(3,6)
	print ("Función con array :",funcion (*mi_array))# ver el "*"
	#                          como Método
	class Clase1:# ver el nombre con mayúscula en su primer carácter que no debe ser numérico
		resultado= 0
		def metodo(self,var_1,var_2):
			self.var_1=  var_1
			self.var_2=  var_2
			self.resultado= (var_1 *var_2)
	ej=Clase1()
	ej.metodo(3,6)
	print ("Método de clase:",ej.resultado)
	nuevo(1);
	#################################################################
	#Ejercicio_Funciones_Ej_002
	print("""
	╔═════════════════════════════════════════════════════════════════════════════╗
	║                                                                             ║
	║                                     Métodos                                 ║
	║                                                                             ║
	╚═════════════════════════════════════════════════════════════════════════════╝
	""")
	class Clase2:# ver el nombre con mayúscula en su primer carácter que no debe ser numérico
		resultado= 0
		def __init__(self):#construye los objetos
			self.var_1=  0
			self.var_2=  0
		def meto2(self,var_1,var_2):
			self.var_1=  var_1
			self.var_2=  var_2
			self.resultado= (var_1 *var_2)

	ej=Clase2()
	print ("al inicio con valores 'self'",ej.resultado)
	ej.meto2(3,6)
	print ("al final con datos modificado por método",ej.resultado)
	nuevo(2);
	#################################################################
	#Ejercicio_Funciones_Ej_003
	def varios(param1, param2, **diccionario):
		for dato in diccionario.items():
			print ("Datos en el diccionario",dato)
	varios(1, 2, tercero = 3, cuarto = 4, quinto = 5)


	def saludar(lenguaje_elejido):
		def saludar_es():
			print ("Hola")
		def saludar_en():
			print ("Hi")
		def saludar_fr():
			print ("Salut")
		def saludar_it():
			print ("Ciao")
		def saludar_ge():
			print ("Hallo")
		Saludar_en_su_leng = {"es": saludar_es,"en": saludar_en,"fr": saludar_fr,"it": saludar_it,"ge": saludar_ge}
		return Saludar_en_su_leng[lenguaje_elejido]
	saludar("es")()
	saludar("it")()
	saludar("fr")()

	nuevo(3);
#################################################################
#Ejercicio_Funciones_Ej_004
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                   Generadores                               ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
Las expresiones generadoras funcionan de forma muy similar a la comprensión de listas. De hecho su sintaxis es exactamente igual, a
excepción de que se utilizan paréntesis en lugar de corchetes:


Un generador es una clase especial de función que genera valores sobre los que iterar. Para devolver el siguiente valor sobre el que iterar se
utiliza la palabra clave yield en lugar de return .
def mi_generador(n, m, s):
	while(n <= m):
		yield n
		n += s
lista = list( mi_generador(0, 5, 1))
print(lista)
El generador se puede utilizar en cualquier lugar donde se necesite un objeto iterable.

No generamos un solo valor cada vez que se necesita, en situaciones en las que no sea necesario tener la lista completa el uso de generadores puede
suponer una gran diferencia de memoria. En todo caso siempre es posible crear una lista a partir de un generador mediante la función list :
lista = list(mi_generador)
""")
def mi_generador(n, m, s):
	while(n <= m):
		yield n
		n += s
lista = list( mi_generador(0, 5, 1))
print(lista)
limpiar()
print("\n# Fibonacci version 1")
# Fibonacci version 1
def fibonacci():
	Limit = 10
	count = 0
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a+b
		if (count == Limit):
			break
		count += 1
for n in fibonacci():
	print(n, end=' ')
print("\n# Fibonacci version 2")
# Fibonacci version 2
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
for n in fibonacci(500):
	print(n, end=' ')
nuevo(4);
#################################################################
#Ejercicio_Funciones_Ej_005
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                       Lambda                                ║
║                 lambda <parámetro> :expresión                               ║
╚═════════════════════════════════════════════════════════════════════════════╝
http://conocepython.blogspot.com/2017/08/t2-las-funciones-lambda-elogio-de-la.html
https://programacionpython80889555.wordpress.com/2018/10/30/funciones-lambda-en-python/

Operador lambda:
El operador lambda que no es función lambda, es una forma de crear funciones anónimas, es decir, funciones sin nombre. Estas funciones son desechable, es decir, solo se necesitan donde se han creado. Las funciones lambda se utilizan principalmente en combinación con las funciones Map, Filter y Reduce.

lambda no es una función es keyword o palabra reservada del lenguaje que introduce en el punto de la declaración una expresión: una expresión lambda. El resultado de dicha expresión es a todos los efectos un callable equivalente a uno generado con la sentencia def.

La sintaxis general de una función lambda es bastante simple:
lambda argument_list : expression

El operador lambda o función lambda, es una forma de crear funciones anónimas, es decir, funciones sin nombre. Estas funciones son desechables, es decir, solo se nesecitan donde se han creado. Las funciones lambda se utilizan principalmente en combinatorio con las funciones Map, Filter y Reduce.
""")

area_triangulo =lambda base,altura:(base*altura)/2
while True:
	try:
		base = float(input("Ingrese la base :"))
		altura = float(input("Ingrese la altura :"))
		break
	except ValueError:
		print ("Error de entrada/salida.")
print(area_triangulo(base,altura))
nuevo(5);
#################################################################
#Ejercicio_Funciones_Ej_006
#Función lambda que devuelve la suma de sus dos argumentos:
func_lambda = lambda x, y : x + y
print("func_lambda(2 , 6)",func_lambda(2 , 6))

#Segundo ejemplo de lambda
#Función lambda que devuelve la raíz cuadrada de su argumento
func_lambda = lambda x : x**1/2
print("func_lambda(233)",func_lambda(233))


func_lambda = lambda x: x < 5
print(func_lambda(3))  # Devuelve 'True'
print(func_lambda(8))  # Devuelve 'False'

func_lambda =  lambda x, y, z=1: (x+y) * z
print("func_lambda(5, 6) :",func_lambda(5, 6))
print("func_lambda(5, 6, 7) :",func_lambda(5, 6, 7))

nuevo(6);
#################################################################
#Ejercicio_Funciones_Ej_007

print("Con strings")
revertir = lambda cadena: cadena[::-1]
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ:",revertir("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print("BUEN DIA, ¿COMO VA LA VIDA?:",revertir("BUEN DIA, ¿COMO VA LA VIDA?"))
print("Neuquen:",revertir("Neuquen"));print("Es un palíndromo")
limpiar()
array = ['a','b','c']
num = range(1,4)
for contador in map(lambda x, y: x*y, array, num):
	print(contador)
#sin lambda con zip
for contador in (x*y for x,y in zip(array, num)):
    print(contador)
nuevo(7);
#################################################################
#Ejercicio_Funciones_Ej_008
print ("Ver \nhttps://es.quora.com/Qu%C3%A9-hace-realmente-la-funci%C3%B3n-lambda-de-Python-Quiero-dominarle-pero-no-la-entiendo")

resultado = lambda s: s.strip().upper()

print(resultado("  hOlA CoMo EsTaS   "))

print("Con funciones")
def imprimir_si(lista, fn):
	for elemento in lista:
		if fn(elemento):
			print(elemento)

lista1=[9, 20, 70, 60, 19]
print("Valores pares de la lista")
imprimir_si(lista1, lambda x: x%2==0)
print("Valores múltiplos de 3 o de 5")
imprimir_si(lista1, lambda x: x%3==0 or x%5==0)
print("Imprimir valores mayores o iguales a 50")
imprimir_si(lista1, lambda x: x>=50)
print("Imprimir los valores comprendidos entre 10 y 50 o 70 y 100")
imprimir_si(lista1, lambda x: x>=10 and x<=50 or x>=70 and x<=100)
print("Imprimir la lista completa")
imprimir_si(lista1, lambda x: True )

nuevo(8);
#################################################################
#Ejercicio_Funciones_Ej_009
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Lambda + map                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
Operador Map:
El operador Map, toma una función y un iterable como argumentos, y devuelve un nuevo iterable con la función aplicada a cada argumento . Ejemplo:
Como pueden ver, "map" nos a devuelto una lista con todo los elementos de la lista "array", vemos que a cada elemento le sumo 5.
""")

#Ejemplo del operador Map
def add_five(x):
	return x + 5
print("array = [11, 25, 34, 100, 23]")
array = [11, 25, 34, 100, 23]
resultado = list(map(add_five, array))
print("función normal + 5",resultado)
#        lo mismo pero en lambda


resultado = list(map(lambda x:x+5, array))
print("función lambda + 5",resultado)

resultado = list(map(lambda x: x**2, array))
print(resultado)



nuevo(9);
#################################################################
#Ejercicio_Funciones_Ej_010

print("""Vamos a hacer una función
def doblar(num):
	resultado = num*2
	return resultado
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num):
	resultado = num*2
	return resultado
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))

print("""Vamos a hacerlo mas simple
def doblar(num):
	return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num):
	return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))

print(""" mas simple
def doblar(num): return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num): return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))

print(""" y ahora......
Esta notación simple es la que una función lambda intenta replicar, fijaros, vamos a convertir la función en una función anónima:
doblar = (lambda num: num*2)
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")


doblar = lambda num: num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
print(""" Ejemplo""")

impar = lambda num: num%2 != 0
valor = int(input("Valor : "))
print("es impar :",impar(valor))

nuevo(10);
#################################################################
#Ejercicio_Funciones_Ej_011
print ("""
Función lambda
--------------
La función lambda se utiliza para declarar funciones que sólo ocupan una línea. Son objetos que se pueden asignar a variables para usar con posterioridad.
""")
cuadrado = lambda x: x*x

lista = [1,2,3,5,8,13]
for elemento in lista:
	print(cuadrado(elemento))

print (""" Lambda, con 2 argumentos:""")

area_triangulo = (lambda b,h: b*h/2)
medidas = [(34, 8), (26, 8), (44, 18)]
for datos in medidas:
	base = datos[0]
	altura = datos[1]
	print(area_triangulo(base, altura))
nuevo(11);
#################################################################
#Ejercicio_Funciones_Ej_012

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Lambda + filter (true / false)                 ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

Operador Filter:

El operado filter (función, lista) ofrece una forma elegante de filtrar todos los elementos de una lista, para los que la función de función devuelve True.
El operador filter(f, l) necesita una función f como primer argumento. f devuelve un valor booleano, es decir, verdadero o falso. Esta función se aplicará a cada elemento de la lista. Solo si f devuelve True, el elemento de la lista se incluirá en la lista de resultados.
""")

#Usando el operador Filter
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
print("array",array)
resultado = list(filter(lambda x: x % 2 == 0, array))
print("x % 2 == 0, :",resultado)

resultado = list(filter(lambda x: x > 0, array))
print("x > 0 :",resultado)

resultado = list(filter(lambda x: x % 3 != 0, array))
print("x % 3 != 0 :",resultado)

resultado = list(filter(lambda x: x % 3 <= 5, array)) # list()' convierte el iterable
print("x % 3 <= 5 :",resultado)

nuevo(12);
#################################################################
#Ejercicio_Funciones_Ej_013
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                     Clases                                  ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
class Funcion_Contador:#
	Valor = 0   # This represents the Valor of objects of this class
	def __init__(self, nombre_objeto):
		self.nombre_objeto = nombre_objeto
		print (nombre_objeto, 'creado')
		Funcion_Contador.Valor += 1
	def __del__(self):
		print (self.nombre_objeto, 'borrado')
		Funcion_Contador.Valor -= 1
		if Funcion_Contador.Valor == 0:
			print ('Se borro el ultimo objeto')
		else:
			print (Funcion_Contador.Valor, 'Objetos remanentes')
objerto_1 = Funcion_Contador("Primer objeto")
objerto_2 = Funcion_Contador("Segundo objeto")
objerto_3 = Funcion_Contador("Tercer objeto")
del objerto_2

print("""
Without the final del, you get an exception. Shouldn’t the normal cleanup process take care of this?

From the Python docs regarding __del__:

	Warning: Due to the precarious circumstances under which __del__() methods are invoked, exceptions that occur during their execution are ignored, and a warning is printed to sys.stderr instead. Also, when __del__() is invoked in response to a module being deleted (e.g., when execution of the program is done), other globals referenced by the __del__() method may already have been deleted. For this reason, __del__() methods should do the absolute minimum needed to maintain external invariants.

Without the explicit call to del, __del__ is only called at the end of the program, Counter and/or Count may have already been GC-ed by the time __del__ is called (the order in which objects are collected is not deterministic). The exception means that Counter has already been collectd. You can’t do anything particularly fancy with __del__.

There are two possible solutions here.

	1. Use an explicit finalizer method, such as close() for file objects.

		Use weak references.
""")
nuevo(13,"fin");
#################################################################
