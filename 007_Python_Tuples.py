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
║                          Python tuples/Array Methods                        ║
║                          ---------------------------                        ║
║                                                                             ║
║          Method    Description                                              ║
║                                                                             ║
║          count()   Returns the number of elements with the specified value  ║
║                                                                             ║
║          index()   Returns the index of the first element with the specified║
║                    value.Searches the tuple for a specified value and       ║
║                    returns the position of where it was found               ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                    Tuplas                                   ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://www.w3schools.com/python/python_ref_tuple.asp
\nhttps://www.w3schools.com/python/python_tuples.asp
""");
nuevo(0,"inicio");
Nombre_tupla_1 = ("linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 1")
Nombre_lista_1 = [" "]
Nombre_tupla_2 = (" ")
#################################################################
#Clase_Tupples_Ej_001
print("tupla a listas con tuple")
print ("valores tupla 1"+str(Nombre_tupla_1))
print ("valores lista 1"+str(Nombre_lista_1))
print ("paso los datos de mi tupla a mi lista")
Nombre_lista_1=tuple(Nombre_tupla_1)
print ("Nuevos valores lista 1"+str(Nombre_lista_1))
nuevo(1);
#################################################################
#Clase_Tupples_Ej_002
print("lista a tuple con list")
print ("valores tupla 2"+str(Nombre_tupla_2))
print ("paso los datos de mi lista a mi tupla 2")
Nombre_tupla_2=list(Nombre_lista_1)
print ("Nuevos valores tupla 2"+str(Nombre_tupla_2))
nuevo(2);
#################################################################
#Clase_Tupples_Ej_003
print("posiciones") 
print (Nombre_tupla_1)
print ("posicion [1]  "+Nombre_tupla_1[1])
print ("posicion [5]  "+Nombre_tupla_1[5])
print ("posicion [7]  "+Nombre_tupla_1[7])
print ("posicion [0]  "+Nombre_tupla_1[0])
print ("posicion [9]  "+Nombre_tupla_1[9])
nuevo(3);
#################################################################
#Clase_Tupples_Ej_004
print("posiciones negativas") 
print (Nombre_tupla_1)
print ("posicion [-1]  "+Nombre_tupla_1[-1])
print ("posicion [-2]  "+Nombre_tupla_1[-2])
print ("posicion [-3]  "+Nombre_tupla_1[-9])
nuevo(5);
#################################################################
#Clase_Tupples_Ej_006
print("sectores o porsiones") 
print (Nombre_tupla_1)
print ("posicion [4 al 8]  "+str(Nombre_tupla_1[4:8]))
print ("posicion [0 al -2]  "+str(Nombre_tupla_1[0:-2]))
print ("posicion [-3 al 5]  "+str(Nombre_tupla_1[-3:5])+"error")
nuevo(6);
#################################################################
#Clase_Tupples_Ej_007
print("operadores varios") 
print (Nombre_tupla_1)
print ("cantidad de datos totales "+str(len(Nombre_tupla_1)))
print ("cantidad de datos 'ĺinea 1' es " +str(Nombre_tupla_1.count("linea 1")))
nuevo(7);
#################################################################
#Clase_Tupples_Ej_008
print("busco (si existe) un dato en la tupla")
print (Nombre_tupla_1)
print ("Busco si el dato 'linea 3' esta en mi tupla??")
print ("linea 3" in  Nombre_tupla_1)
nuevo(8);
#################################################################
#Clase_Tupples_Ej_009
print("busco (si existe) un dato en la tupla")
print ("Busco si el dato 'columna 3' esta en mi tupla??")
print ("viejo" in  Nombre_tupla_1)
nuevo(9);
#################################################################
#Clase_Tupples_Ej_010
print("Ubicar la posicion un dato en el index" )
print (Nombre_tupla_1)
print ("Ubicar la posicion de 'linea 3' en el index y es : ")
print (Nombre_tupla_1.index("linea 3"))
nuevo(10,"fin");
#################################################################
