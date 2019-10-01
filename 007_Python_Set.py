from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                  Python Set /Array Methods                  ║
║                          ---------------------------                        ║
║                                                                             ║
║          Method    Description                                              ║
║                                                                             ║
║          add()     Adds an element to the set                               ║
║          clear()   Removes all the elements from the set                    ║
║          copy()    Returns a copy of the set                                ║
║          difference()	Returns a set containing the difference between two   ║
║                    or more sets                                             ║
║          difference_update()	Removes the items in this set that are also   ║
║                     included in another, specified set                      ║
║          discard()	Remove the specified item                             ║
║          intersection()	Returns a set, that is the intersection of two    ║
║                     other sets                                              ║
║          intersection_update()	Removes the items in this set that are not║
║                    present in other, specified set(s)                       ║
║          isdisjoint()	Returns whether two sets have a intersection or       ║
║                     not                                                     ║
║          issubset()	Returns whether another set contains this set or      ║
║                     not                                                     ║
║          issuperset()	Returns whether this set contains another set or      ║
║                     not                                                     ║
║          pop()	Removes an element from the set                           ║
║          remove()	Removes the specified element                             ║
║          symmetric_difference()	Returns a set with the symmetric          ║
║                     differences of two sets                                 ║
║          symmetric_difference_update()	inserts the symmetric differences ║
║                     from this set and another                               ║
║          union()	Return a set containing the union of sets                 ║
║          update()	Update the set with the union of this set and others      ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                       SET                                   ║
║                                                                             ║
║       Un conjunto es una lista de elementos donde ninguno de ellos está     ║
║       repetido. A partir de una lista, en la que pueden haber elementos     ║
║       repetidos, con set es posible crear otra lista con todos los          ║
║       elementos pero sin repetir ninguno. Además, si tenemos varias         ║
║       listas podemos realizar operaciones de conjuntos de unión,            ║
║       diferencia, intersección y diferencia simétrica                       ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

https://www.w3schools.com/python/python_sets.asp
""");
nuevo(0,"inicio");
#################################################################
#Clase_Set_Ej_001
Nombre_set_1 = {"linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 1"}

print("SET_1")
print("Access Items\nYou cannot access items in a set by referring to an indedato_set, since sets are unordered the items has no indedato_set.");
print("But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.");
print("Loop through the set, and print the values:")
for dato_set in Nombre_set_1:  print(dato_set)
nuevo(1);
#################################################################
#Clase_Set_Ej_002
print("Check");
print("----------");
print("Check if 'linea 5' is present in the set:")
print("linea 2" in Nombre_set_1)
if ("linea 2" in Nombre_set_1):  print("Si, esta en lista!")
nuevo(2);
#################################################################
#Clase_Set_Ej_003
print("Change Items");
print("Once a set is created, you cannot change its items, but you can add new items.");
print("Add Items");
print("---------");
print("Add an item to a set, using the add() method:");
print(Nombre_set_1)
Nombre_set_1.add("linea 0")
print(Nombre_set_1)
nuevo(3);
#################################################################
#Clase_Set_Ej_004
print("Add multiple items to a set, using the update() method:");
print(Nombre_set_1)
Nombre_set_1.update(["linea 11", "linea 12", "linea 13"])
print(Nombre_set_1)
nuevo(4);
#################################################################
#Clase_Set_Ej_005
print("Get the Length of a Set");
print("-----------------------");
print("To determine how many items a set has, use the len() method.");
print("Get the number of items in a set:");
print(len(Nombre_set_1))
nuevo(5);
#################################################################
#Clase_Set_Ej_006
print("Remove Item");
print("-----------");
print("To remove an item in a set, use the remove(), or the discard() method.");
print("Remove 'linea 4' by using the remove() method:");
print(Nombre_set_1)
Nombre_set_1.remove("linea 4")
print(Nombre_set_1)
print("Note: If the item to remove does not erase all list, remove() will raise an error.");
nuevo(6);
#################################################################
#Clase_Set_Ej_007
print("Remove 'linea 3' by using the discard() method:");
print(Nombre_set_1)
Nombre_set_1.discard("linea 3")
print(Nombre_set_1)
print("Note: If the item to remove does erase all list, discard() will NOT raise an error.");
nuevo(7);
#################################################################
#Clase_Set_Ej_008
print("You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.");
print("The return value of the pop() method is the removed item.");
print("Remove the last item by using the pop() method:");
dato_set = Nombre_set_1.pop()
print(dato_set)
print(Nombre_set_1)
print("Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.");
nuevo(8);
#################################################################
#Clase_Set_Ej_009
print("Clear Item");
print("----------");
print("The clear() method empties the set:");
Nombre_set_1.clear()
print(Nombre_set_1)
print("The del keyword will delete the set completely:");
nuevo(9);
#################################################################
#Clase_Set_Ej_010
lista = ['vino', 'cerveza', 'agua', 'vino']					# define lista
bebidas = set(lista)										# define conjunto a partir de una lista
print('vino' in bebidas)									# True, 'vino' está en el conjunto
print('anis' in bebidas)									# False, 'anis' no está en el conjunto
print(bebidas)												# imprime {'agua', 'cerveza', 'vino'}
bebidas2 = bebidas.copy()									# crea nuevo conjunto a partir de copia
print(bebidas2)												# imprime {'agua', 'cerveza', 'vino'}
bebidas2.add('anis')										# añade un nuevo elemento 
print(bebidas2.issuperset(bebidas)) 						# True, bebidas es subconjunto
bebidas.remove('agua')										# borra elemento
print(bebidas & bebidas2)									# imprime elementos comunes
tapas = ['croquetas', 'solomillo', 'croquetas']				# define lista
conjunto = set(tapas)										# crea conjunto (sólo una de croquetas)
if 'croquetas' in conjunto:	pass							# evalúa si croquetas está
conjunto1 = set('Python');									# define conj: P,y,t,h,o,n 
conjunto2 = set('Pitonisa');								# define conj: P,i,t,o,n,s,a
print(conjunto2 - conjunto1)								# aplica diferencia: s, i, a
print(conjunto1 | conjunto2)								# aplica unión: P,y,t,h,o,n,i,s,a 
print(conjunto1 & conjunto2)								# intersección: P,t,o,n
print(conjunto1 ^ conjunto2)								# diferencia simétrica: y,h,i,s,a
nuevo(10);
#################################################################
#Clase_Set_Ej_011
from collections import Counter

datos = [10,20,30,40,10,20,30,10,20,10]
c_datos = Counter(datos)

print(c_datos.items())        # Registros del contador por clave-valor
print(c_datos.keys())         # Registros del contador por clave
print(c_datos.values())       # Registros del contador por valor

print(sum(c_datos.values()))  # Suma total de elementos del contador

print(list(c_datos))          # Conversión a lista
print(dict(c_datos))          # Conversión a conjunto
print(set(c_datos))           # Conversión a conjunto
nuevo(11,"fin");
#################################################################
