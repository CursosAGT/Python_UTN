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
║                 Listas                                                      ║
║                      * Índices                                              ║
║                      * Recorrer listas                                      ║
║                   Tuplas                                                    ║
║                      * Índices                                              ║
║                      * Recorrer Tuplas                                      ║
║                   Diccionarios                                              ║
║                      * Funcionamiento de diccionarios                       ║
║                      * Estructuras tipo JSON                                ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                Python List/Array Methods                    ║
║                               ---------------------------                   ║
║                                                                             ║
║         Method    Description                                               ║
║                                                                             ║
║         clear()   Removes all the elements from the dictionary              ║
║         copy()    Returns a copy of the dictionary                          ║
║         fromkeys()Returns a dictionary with the specified keys and values   ║
║         get()     Returns the value of the specified key                    ║
║         items()   Returns a list containing a tuple for each key value pair ║
║         keys()    Returns a list containing the dictionary's keys           ║
║         pop()     Removes the element at the specified position             ║
║         popitem() Removes the last inserted key-value pair                  ║
║         reverse() Reverses the order of the dictionary                      ║
║         setdefault() Returns the value of the specified key. If the key     ║
║                   does not exist: insert the key, with the specified value  ║
║         update()  Updates the dictionary with the specified key-value pairs ║
║         values()  Returns a list of all the values in the dictionary        ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                      Diccionarios                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://www.w3schools.com/python/python_ref_dictionary.asp
https://www.w3schools.com/python/python_dictionaries.asp
https://python-para-impacientes.blogspot.com/2014/01/cadenas-listas-tuplas-diccionarios-y.html


Diccionarios o matrices asociativas
Los diccionarios son objetos que contienen una lista de parejas de elementos.
De cada pareja un elemento es la clave, que no puede repetirse, y, el otro, un valor asociado.
La clave que se utiliza para acceder al valor tiene que ser un dato inmutable como una cadena,
El valor puede ser un número, una cadena, un valor lógico (True/False), una lista o una tupla.
Los pares clave-valor están separados por dos puntos, las parejas por comas y todo el conjunto se encierra entre llaves.
""");
limpiar();
#################################################################
#Clase_Diccionarios_Ej_01 

Nombre_diccionario_1 = {"clave 1":"dato_asociado 1","clave 2":"dato_asociado 2","clave 3":"dato_asociado 3","clave 4":"dato_asociado 4","clave 5":"dato_asociado 5","clave 6":"dato_asociado 6","clave 7":"dato_asociado 7","clave 8":"dato_asociado 8","clave 9":"dato_asociado 9","clave 10":"dato_asociado 10"}
Nombre_tupla_1 = ["linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 1"]
Nombre_tupla_2 = ["columna 1","columna 2","columna 3","columna 4","columna 5","columna 6","columna 7","columna 8","columna 9","columna 10"]


print (Nombre_diccionario_1)
print ("clave 2  "+Nombre_diccionario_1["clave 2"])
print ("clave 6  "+Nombre_diccionario_1["clave 6"])
print ("clave 5  "+Nombre_diccionario_1["clave 5"])
print ("clave 9  "+Nombre_diccionario_1["clave 9"])
print ("clave 1  "+Nombre_diccionario_1["clave 1"])
nuevo(2);
#################################################################
#Clase_Diccionarios_Ej_03
print("Agregar")
print (Nombre_diccionario_1)
print ("Agrego un conjunto en la posicion FINAL")
Nombre_diccionario_1["clave 11"]="dato_asociado 11"
print (Nombre_diccionario_1)
nuevo(3);
#################################################################
#Clase_Diccionarios_Ej_04
print("Borrar")
print (Nombre_diccionario_1)
print ("delEteo o borro el dato 'clave 8'")
del Nombre_diccionario_1["clave 8"]
print (Nombre_diccionario_1)
nuevo(4);
#################################################################
#Clase_Diccionarios_Ej_05
print("Reemplazar")
print (Nombre_diccionario_1)
print ("cambio el dato asociado a la clave 9")
Nombre_diccionario_1["clave 9"]="dato_asociado 999"
print (Nombre_diccionario_1)
nuevo(5);
#################################################################
#Clase_Diccionarios_Ej_06
print("de tuplas a diccionrios")
print ("valores tupla 1"+str(Nombre_tupla_1))
print ("valores tupla 2"+str(Nombre_tupla_2))
Nombre_diccionario_3 = {}
Nombre_diccionario_2 = {Nombre_tupla_1[0]:Nombre_tupla_2[0],Nombre_tupla_1[1]:Nombre_tupla_2[1],Nombre_tupla_1[2]:Nombre_tupla_2[2],Nombre_tupla_1[3]:Nombre_tupla_2[3],Nombre_tupla_1[4]:Nombre_tupla_2[4],Nombre_tupla_1[5]:Nombre_tupla_2[5],Nombre_tupla_1[6]:Nombre_tupla_2[6],Nombre_tupla_1[7]:Nombre_tupla_2[7],Nombre_tupla_1[8]:Nombre_tupla_2[8],Nombre_tupla_1[9]:Nombre_tupla_2[9]}
print (Nombre_diccionario_2)
for contador in range (0,9):
	Nombre_diccionario_3[Nombre_tupla_1[contador]] = Nombre_tupla_2[contador]
print (Nombre_diccionario_3)
nuevo(6);
#################################################################
#Clase_Diccionarios_Ej_07
print("separo claves de  datos asociados ")
print ("pares de valores del diccionario 1 : "+str(Nombre_diccionario_1))
print ("Claves del diccionario 1 : "+str(Nombre_diccionario_1.keys()))
print ("Datos asociados del diccionario 1 : "+str(Nombre_diccionario_1.values()))
print ("Longitud de pares de datos del diccionario 1 : "+str(len(Nombre_diccionario_1)))
nuevo(7);
#################################################################
#Clase_Diccionarios_Ej_08
# input stored in variable a. 
diccionario = {"nombre":"Juan", "apellido":"Perez"} 
# Use of format_map() function 
print("el apellido de  {nombre} es {apellido}".format_map(diccionario)) 
# input stored in variable a. 
a = {"x":"alfa", "y":"beta"} 
# Use of format_map() function 
print("{x} {y}".format_map(a)) 
# Input dictionary 
profession = { "nombres":["Juan", "Pedro"], 
               "profesion":["Astronauta", "Biologo"], 
               "edad":[33, 55] } 
# Use of format_map() function  
print("{nombres[0]} Segundo Apellidoja de {profesion[0]} y tiene {edad[0]} años.".format_map(profession)) 
print("{nombres[1]} Segundo Apellidoja de {profesion[1]} y tiene {edad[1]} años.".format_map(profession)) 
nuevo(8);
#################################################################
#Clase_Diccionarios_Ej_09
dic1 = {'Lorca':'Escritor', 'Goya':'Pintor'}		# declara diccionario 
print(dic1) 										# imprime dic1{'Goya': 'Pintor', 'Lorca': 'Escritor'}
dic2 = dict((('mesa',5), ('silla',10)))				# declara a partir de tupla
dic3 = dict(ALM=5, CAD=10)							# declara a partir de cadenas simples 
dic4 = dict([(z, z**2) for z in (1, 2, 3)])			# declara a partir patrón
print(dic4)											# muestra {1: 1, 2: 4, 3: 9}
print(dic1['Lorca'])								# escritor, acceso a un valor por clave
print(dic1.get('Gala', 'no existe'))				# acceso a un valor por clave
if 'Lorca' in dic1: print('está')					# comprueba si existe una clave
print(dic1.items())									# obtiene una lista de tuplas clave:valor
print(dic1.keys())									# obtiene una lista de las claves
print(dic1.values())								# obtiene una lista de los valores
dic1['Lorca'] = 'Poeta'								# añade un nuevo par clave:valor
dic1['Amenabar'] = 'Cineasta'						# añade un nuevo par clave:valor
dic1.update({'Carreras' : 'Tenor'})					# añadir con update()
del dic1['Amenabar']								# borra un par clave:valor 
print(dic1.pop('Amenabar', 'Amenabar ya no está'))	# borra par clave:valor
nuevo(9);
#################################################################
#Clase_Diccionarios_Ej_10
artistas = {'Lorca':'Escritor', 'Goya':'Pintor'}	# diccionario
paises = ['Chile','España','Francia','Portugal']	# declara lista
capitales = ['Santiago','Madrid','París','Lisboa']	# declara lista
for c, v in artistas.items():
	print(c,':',v)									# recorre diccionario
for i, c in enumerate(paises):
	print(i,':',c)									# recorre lista 
for p, c in zip(paises, capitales):
	print(c,' ',p)									# recorre listas
for p in reversed(paises):
	print(p,)										# recorre en orden inverso
for c in sorted(paises):
	print(c,)  										# recorre secuencia ordenada
nuevo(10);
#################################################################
