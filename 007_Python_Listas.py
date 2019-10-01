from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                  Unidad 4 - Listas, Tuplas y Diccionarios   ║
║              Listas                                                         ║
║                 * Índices                                                   ║
║                 * Recorrer listas                                           ║
║              Tuplas                                                         ║
║                 * Índices                                                   ║
║                 * Recorrer Tuplas                                           ║
║              Diccionarios                                                   ║
║                 * Funcionamiento de diccionarios                            ║
║                 * Estructuras tipo JSON                                     ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                           Python List/Array Methods                         ║
║                          ---------------------------                        ║
║                                                                             ║
║          Method    Description                                              ║
║                                                                             ║
║          append()  Adds an element at the end of the list                   ║
║          clear()   Removes all the elements from the list                   ║
║          copy()    Returns a copy of the list                               ║
║          count()   Returns the number of elements with the specified value  ║
║          extend()  Add the elements of a list (or any iterable), to the end ║
║                    of the current list                                      ║
║          index()   Returns the index of the first element with the specified║
║                    value                                                    ║
║          insert()  Adds an element at the specified position                ║
║          pop()     Removes the element at the specified position            ║
║          remove()  Removes the first item with the specified value          ║
║          reverse() Reverses the order of the list                           ║
║          sort()    Sorts the list                                           ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                    Listas                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

https://www.w3schools.com/python/python_ref_list.asp
\nhttps://www.w3schools.com/python/python_lists.asp
""");
limpiar();
#################################################################
print("""
list.append(x)
    Agrega un ítem al final de la lista. Equivale a a[len(a):] = [x].

list.extend(iterable)
    Extiende la lista agregándole todos los ítems del iterable. Equivale a a[len(a):] = iterable.

list.insert(i, x)
    Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se insertará, por lo tanto a.insert(0, x) inserta al principio de la lista, y a.insert(len(a), x) equivale a a.append(x).

list.remove(x)
    Quita el primer ítem de la lista cuyo valor sea x. Es un error si no existe tal ítem.

list.pop([i])
    Quita el ítem en la posición dada de la lista, y lo devuelve. Si no se especifica un índice, a.pop() quita y devuelve el último ítem de la lista. (Los corchetes que encierran a i en la firma del método denotan que el parámetro es opcional, no que deberías escribir corchetes en esa posición. Verás esta notación con frecuencia en la Referencia de la Biblioteca de Python.)

list.clear()
    Quita todos los elementos de la lista. Equivalente a del a[:].

list.index(x[, start[, end]])
	Devuelve un índice basado en cero en la lista del primer ítem cuyo valor sea x. Levanta una excepción ValueError si no existe tal ítem.
    Los argumentos opcionales start y end son interpetados como la notación de rebanadas y se usan para limitar la búsqueda a una subsecuencia particular de la lista. El index retornado se calcula de manera relativa al inicio de la secuencia completa en lugar de con respecto al argumento start.

list.count(x)
    Devuelve el número de veces que x aparece en la lista.

list.sort(key=None, reverse=False)
    Ordena los ítems de la lista in situ (los argumentos pueden ser usados para personalizar el orden de la lista, ve sorted() para su explicación).

list.reverse()
    Invierte los elementos de la lista in situ.

list.copy()
	Devuelve una copia superficial de la lista. Equivalente a a[:].
""");
limpiar();
#################################################################
#Clase_listas_Ej_001
Nombre_lista_1 = ["linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 10"]
Nombre_lista_2 = ["columna 1","columna 2","columna 3","columna 4","columna 5","columna 6","columna 7","columna 8","columna 9","columna 10"]
print("Inicio ej005_1 - posiciones")
print (Nombre_lista_1)
print ("posicion [1]  "+Nombre_lista_1[1])
print ("posicion [5]  "+Nombre_lista_1[5])
print ("posicion [7]  "+Nombre_lista_1[7])
print ("posicion [0]  "+Nombre_lista_1[0])
print ("posicion [9]  "+Nombre_lista_1[9])
nuevo(1);
#################################################################
#Clase_listas_Ej_002
print("posiciones negativas") 
print (Nombre_lista_1)
print ("posicion [-1]  "+Nombre_lista_1[-1])
print ("posicion [-2]  "+Nombre_lista_1[-2])
print ("posicion [-3]  "+Nombre_lista_1[-9])
nuevo(2);
#################################################################
#Clase_listas_Ej_003
print("sectores o porsiones") 
print (Nombre_lista_1)
print ("posicion [4 al 8]  "+str(Nombre_lista_1[4:8]))
print ("posicion [0 al -2]  "+str(Nombre_lista_1[0:-2]))
print ("posicion [-3 al 5]  "+str(Nombre_lista_1[-3:5])+"error")
nuevo(3);
#################################################################
#Clase_listas_Ej_004
print("amplio la lista con un dato al final")
print (Nombre_lista_1)
print ("Agrego un dato en la posicion FINAL")
Nombre_lista_1.append ("Nuevo")
print (Nombre_lista_1)
nuevo(4);
#################################################################
#Clase_listas_Ej_005
print("amplio la lista con un dato en una posicion elejida")
print (Nombre_lista_1)
print ("Agrego un dato en la posicion 5")
Nombre_lista_1.insert(5,"AQUI_Nuevo_5")
print (Nombre_lista_1)
nuevo(5);
#################################################################
#Clase_listas_Ej_006
print("amplio mucho la lista ")
print (Nombre_lista_1)
print ("Agrego o adiciono un conjunto de datos u otra lista a la original")
Nombre_lista_1.extend(["linea 11","linea 12","linea 13","linea 14","linea 15","linea 16","linea 17","linea 18","linea 19","linea 20"])
print (Nombre_lista_1)
nuevo(6);
#################################################################
#Clase_listas_Ej_007
print("busco (si existe) un dato en la lista")
print (Nombre_lista_1)
print ("Busco si el dato 'AQUI_Nuevo_5' esta en mi lista??")
print ("AQUI_Nuevo_5" in  Nombre_lista_1)
nuevo(7);
#################################################################
#Clase_listas_Ej_008
print("busco (si existe) un dato en la lista")
print ("Busco si el dato 'viejo' esta en mi lista??")
print ("viejo" in  Nombre_lista_1)
nuevo(8);
#################################################################
#Clase_listas_Ej_009
print("Ubicar la posicion un dato en el index" )
print (Nombre_lista_1)
print ("Ubicar la posicion de 'AQUI_Nuevo_5' en el index y es : ")
print (Nombre_lista_1.index("AQUI_Nuevo_5"))
nuevo(9);
#################################################################
#Clase_listas_Ej_010
posicion = 0 
print("remuevo el dato especifico")
print (Nombre_lista_1)
print ("remuevo de la lista 'AQUI_Nuevo_5'")
Nombre_lista_1.remove("AQUI_Nuevo_5")
print (Nombre_lista_1)
nuevo(10);
#################################################################
#Clase_listas_Ej_011
posicion = 0 
print (Nombre_lista_1)
print ("remuevo el dato en la posicion FINAL")
Nombre_lista_1.pop()
print (Nombre_lista_1)
nuevo(11);
#################################################################
#Clase_listas_Ej_012
print("suma de 2 listas")
print ("Lista original")
print (Nombre_lista_1)
print ("Lista nueva")
print (Nombre_lista_2)
print ("junto las listas")
Nombre_lista_3=Nombre_lista_1+Nombre_lista_2
print (Nombre_lista_3)
nuevo(12);
#################################################################
#Clase_listas_Ej_013
print("multiplicacion de listas") 
print ("Lista original")
print (Nombre_lista_2)
print ("repetir datos 3 veces")
Nombre_lista_2=Nombre_lista_2 * 3
print (Nombre_lista_2)
nuevo(13);
#################################################################
#Clase_listas_Ej_014
print("remuevo el dato en la posicion buscada por index")
print (Nombre_lista_1)
posicion = Nombre_lista_1.index("linea 4")
print ("Ubicar la posicion de 'linea 4' con .index y es : "+str(posicion))
print ("delETEO borro la posicion : "+str(posicion))
del Nombre_lista_1[posicion]
print (Nombre_lista_1)
nuevo(14);
#################################################################
#Clase_listas_Ej_015
print("remuevo el dato en la posicion buscada por index")
print("https://python-para-impacientes.blogspot.com/2014/02/programacion-funcional-funciones-de.html")
print ("""
Función map()
-------------
La función de orden superior map() aplica una función a una lista de datos y devuelve un iterador que contiene todos los resultados para los elementos de la lista.
En el siguiente ejemplo la función cuadrado calcula el cuadrado de un número. 
La lista_VALORES contiene una lista de datos numéricos. Con map(cuadrado, lista_VALORES) se aplica la función cuadrado a cada elemento de la lista. 
""")
def cuadrado(numero):       
	return numero ** 2
lista_VALORES = [-2, 4, -6, 8]
lista_CUADRADOS = list(map(cuadrado, lista_VALORES))# Convierte a lista el iterador obtenido
print(lista_CUADRADOS)  # Muestra elementos de la lista
limpiar();
print ("""
Función filter()
----------------
La función filter() aplica un filtro a una lista de datos y devuelve un iterador con los elementos que superan el filtro.
""")

def esneg(numero):# La función verifica si un número es negativo
    return (numero < 0)# Devuelve True/False según sea o no nº negativo
lista5 = [-3, -2, 0, 1, 9, -5]
print(list(filter(esneg, lista5)))
# Muestra los números negativos de la lista
# La función esneg() es llamada para comprobar, 
# uno a uno, todos los números de la lista
limpiar();
print ("""
Función reduce()
----------------
La función reduce() aplica una función a una lista de datos evaluando los elementos por pares. La primera vez se aplica al primer y segundo elemento, la siguiente, se aplicará al valor devuelto por la función junto al tercer elemento y así, sucesivamente, reduciendo la lista hasta que quede un sólo elemento.
A partir de Python 3 si queremos utilizar reduce() debemos importar el módulo functools:
""")
import functools

def multiplicar(x, y):
    print(x * y)  # muestra el resultado parcial
    return x * y

lista = [1, 2, 3, 4]
valor = functools.reduce(multiplicar, lista)
print(valor)  # muestra el resultado final
limpiar();
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
limpiar();
print ("""
Comprensión de listas
----------------------
Es un tipo de construcción que consta de una expresión que determina cómo modificar los elementos de una lista, seguida de una o varias clausulas for y, opcionalmente, una o varias clausulas if. El resultado que se obtiene es una lista.
""")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cada elemento de la lista se eleva al cubo
cubos = [valor ** 3 for valor in lista]
print('Cubos de 1 a 10:', cubos)


numeros = [135, 154, 180, 193, 210]
divisiblespor3 = [valor for valor in numeros if valor % 3.0 == 0] 

# Muestra lista con los números divisibles por 3
print(divisiblespor3)  


# Define función devuelve el inverso de un número
def funcion(x):
    return 1/x

L = [1, 2, 3]  # declara lista

# Muestra lista con inversos de cada número
print([funcion(i) for i in L])
limpiar();
print ("""
Generadores
-----------
Los generadores funcionan de forma parecida a la comprensión de listas pero no devuelven listas sino generadores. Un generador es una clase especial de función que genera valores sobre los que iterar. La sintaxis usada es como la usada en la comprensión de listas pero en vez de usar corchetes se utilizan paréntesis. Para devolver los valores se utiliza yield en vez de return.
""")
# Define generador
def generador(inicio, fin, incremento):
    while(inicio <= fin):
        yield inicio  # devuelve valor
        inicio += incremento

# Recorre los valores del generador
for valor in generador(0, 6, 1):
    # Muestra valores, uno a uno:
    print(valor)  # 0 1 2 3 4 5 6

# Obtiene una lista del generador
lista = list(generador(0, 8, 2))

# Muestra lista
print(lista)  # [0,2,4,6,8]
limpiar();
print ("""
Función Decorador
-----------------
Es una función que recibe una función como parámetro y devuelve otra función como valor de retorno. Se utiliza cuando es necesario definir varias funciones que son muy parecidas. La función devuelta actúa como un envoltorio (wrapper) resolviendo lo que sería común a todas las funciones. También se aplica a clases.
""")
# Define decorador
def decorador1(funcion):
    # Define función decorada
    def funciondecorada(*param1, **param2):
        print('Inicio', funcion.__name__)
        funcion(*param1, **param2)
        print('Fin', funcion.__name__)
    return funciondecorada
    
def suma(a, b):
    print(a + b)

suma2 = decorador1(suma)
suma2(1,2)
suma3 = decorador1(suma)
suma3(2,2)

# Otra forma más elegante, usando @:

@decorador1
def producto(arg1, arg2):
    print(arg1 * arg2)

producto(5,5)


# El siguiente decorador genera tablas de sumas
# y multiplicaciones. El código que es común a todas 
# las funciones se declara en la función 'envoltura':

def tablas(funcion):
    def envoltura(tabla=1):
        print('Tabla del %i:' %tabla)
        print('-' * 15)
        for numero in range(0, 11):            
            funcion(numero, tabla)
        print('-' * 15)
    return envoltura

@tablas
def suma(numero, tabla=1):
    print('%2i + %2i = %3i' %(tabla, numero, tabla+numero))

@tablas
def multiplicar(numero, tabla=1):
    print('%2i X %2i = %3i' %(tabla, numero, tabla*numero))

# Muestra la tabla de sumar del 1
suma()

# Muestra la tabla de sumar del 4 
suma(4)

# Muestra la tabla de multiplicar del 1
multiplicar()

# Muestra la tabla de multiplicar del 10
multiplicar(10)  
"""
lista = ['larry', 'curly', 'moe']
lista.append('shemp')         ## append elem at end
lista.insert(0, 'xxx')        ## insert elem at index 0
lista.extend(['yyy', 'zzz'])  ## add list of elems at end
  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print lista
print lista.index('curly')    ## 2

lista.remove('curly')         ## search and remove that element
lista.pop(1)                  ## removes and returns 'larry'
print lista  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
"""
