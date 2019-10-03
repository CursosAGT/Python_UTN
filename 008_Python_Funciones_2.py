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
#Clase_Funciones_Ej_001
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Funciones,  Metodos                            ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
#                          como funcion
def funcion (var_1, var_2):
	return (var_1 *var_2)
print (funcion (2,4))
mi_array=(3,6)
print (funcion (*mi_array))# ver el "*"
#                          como Metodo
class Clase1:# ver el nombre con mayuscula en su primer caracter que no debe ser numerico
	resultado= 0
	def metodo(self,var_1,var_2):
		self.var_1=  var_1
		self.var_2=  var_2
		self.resultado= (var_1 *var_2)
ej=Clase1()
ej.metodo(6,5)
print (ej.resultado)

nuevo(2);
#################################################################
#Clase_Funciones_Ej_003
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                     Metodos                                 ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
class Clase2:# ver el nombre con mayuscula en su primer caracter que no debe ser numerico
	resultado= 0
	def __init__(self):#construye los objetos
		self.var_1=  0
		self.var_2=  0
	def metodo(self,var_1,var_2):
		self.var_1=  var_1
		self.var_2=  var_2
		self.resultado= (var_1 *var_2)

ej=Clase2()
print ("al inicio con valores 'self'",ej.resultado)
ej.metodo(6,5)
print ("al final con datos modificado por metodo",ej.resultado)
nuevo(2);
#################################################################

#Clase_Funciones_Ej_004
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                       Lambda                                ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
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
nuevo(4);
#################################################################
#Clase_Funciones_Ej_005

class Contador:#
	Valor = 0   # This represents the Valor of objects of this class
	def __init__(self, nombre_objeto):
		self.nombre_objeto = nombre_objeto
		print (nombre_objeto, 'creado')
		Contador.Valor += 1
	def __del__(self):
		print (self.nombre_objeto, 'borrado')
		Contador.Valor -= 1
		if Contador.Valor == 0:
			print ('Se borro el ultimo objeto')
		else:
			print (Contador.Valor, 'Objetos remanentes')
objerto_x = Contador("First")
objerto_y = Contador("second")
del objerto_x

"""
Without the final del, you get an exception. Shouldn’t the normal cleanup process take care of this?

From the Python docs regarding __del__:

	Warning: Due to the precarious circumstances under which __del__() methods are invoked, exceptions that occur during their execution are ignored, and a warning is printed to sys.stderr instead. Also, when __del__() is invoked in response to a module being deleted (e.g., when execution of the program is done), other globals referenced by the __del__() method may already have been deleted. For this reason, __del__() methods should do the absolute minimum needed to maintain external invariants.

Without the explicit call to del, __del__ is only called at the end of the program, Counter and/or Count may have already been GC-ed by the time __del__ is called (the order in which objects are collected is not deterministic). The exception means that Counter has already been collectd. You can’t do anything particularly fancy with __del__.

There are two possible solutions here.

	1. Use an explicit finalizer method, such as close() for file objects.

		Use weak references.
"""
nuevo(5);
#################################################################
#Clase_Funciones_Ej_006

print("""Vamos a hacer una funcion
def doblar(num):
    resultado = num*2
    return resultado
valor = int(input("Valor : "))
print(doblar(valor))

""")

def doblar(num):
    resultado = num*2
    return resultado
valor = int(input("Valor : "))
print(doblar(valor))

print("""Vamos a hacerlo mas simple
def doblar(num):
    return num*2
valor = int(input("Valor : "))
print(doblar(valor))
""")

def doblar(num):
    return num*2
valor = int(input("Valor : "))
print(doblar(valor))

print(""" mas simple
def doblar(num): return num*2
valor = int(input("Valor : "))
print(doblar(valor))
""")

def doblar(num): return num*2
valor = int(input("Valor : "))
print(doblar(valor))


print(""" y ahora......
Esta notación simple es la que una función lambda intenta replicar, fijaros, vamos a convertir la función en una función anónima:
doblar = (lambda num: num*2)
valor = int(input("Valor : "))
print(doblar(valor))
""")


doblar = lambda num: num*2
valor = int(input("Valor : "))
print(doblar(valor))
print(""" Ejemplo
""")


impar = lambda num: num%2 != 0
valor = int(input("Valor : "))
print(impar(valor))

nuevo(6);
#################################################################
#Clase_Funciones_Ej_07
print ("""
Función lambda
--------------
La función lambda se utiliza para declarar funciones que sólo ocupan una línea. Son objetos que se pueden asignar a variables para usar con posterioridad.
""")
cuadrado = lambda x: x*x

lista = [1,2,3,5,8,13]
for elemento in lista:
    print(cuadrado(elemento))

# Lambda, con 2 argumentos:

area_triangulo = (lambda b,h: b*h/2)
medidas = [(34, 8), (26, 8), (44, 18)]
for datos in medidas:
    base = datos[0]
    altura = datos[1]
    print(area_triangulo(base, altura))
nuevo(7,"fin");
#################################################################





