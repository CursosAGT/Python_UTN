
from Estructura import *
nuevo(0,"inicio");
#################################################################
#Condicional_Ej_01;
def Ej_ya_hechos():
	#Con tab colocaremos aquí las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                Condicionales                                ║
║                                                                             ║
║                               "if else elif"                                ║
║                                 <,>,==,!=                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
dato = [99, 25, 50, 5];
print (dato)
#################################################################
print("Ejemplo de operador de comparación Igual: ==");
if (dato[0] == dato[1]):
	print ("'dato[0]' y 'dato[1]' son iguales.");
else:
	print ("'dato[0]' y 'dato[1]' no son iguales.");
#################################################################
print("Ejemplo de operador de comparación Distinto: !=");
if (dato[0] != dato[1]):
	print ("'dato[0]' y 'dato[1]' son distintas.");
else:
	print ("'dato[0]' y 'dato[1]' no son distintas.");
#################################################################
print("Ejemplo de operador de comparación Menor que: <");
if (dato[0] < dato[1]):
	print ("'dato[0]' es menor que 'dato[1]'.");
else:
	print ("'dato[0]' no es menor que 'dato[1]'.");
#################################################################
print("Ejemplo de operador de comparación Mayor que: >");
if (dato[0] > dato[1]):
	print ("'dato[0]' es mayor que 'dato[1]'.");
else:
	print ("'dato[0]' no es mayor que 'dato[1]'.");
#################################################################
print("Ejemplo de operador de comparación Menor o igual que: <=");
if (dato[2] <= dato[3]):
	print ("'dato[2]' es menor o igual que 'dato[3]'.");
else:
	print ("'dato[2]' no es menor o igual que 'dato[3]'.");
#################################################################
print("Ejemplo de operador de comparación Mayor o igual que: >=");
if (dato[3] >= dato[2]):
	print ("'dato[3]' es mayor o igual que 'dato[2]'.");
else:
	print ("'dato[3]' no es mayor o igual que 'dato[2]'.");
#################################################################
print("Ejemplo de dos operadoradores de dos comparaciones");
if ((dato[0] >= dato[1]) != (dato[2] >= dato[3])):
	print ("(dato[0] >= dato[1])) != ((dato[2] >= dato[3]).");
else:
	print ("NO  (dato[0] >= dato[1])) != ((dato[2] >= dato[3]).");

nuevo(1);
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                Condicionales                                ║
║                                                                             ║
║                                    "if"                                     ║
║                                  or , and ,                                 ║
║                                 not, is, in                                 ║
╔═════════════════════════════════════════════════════════════════════════════╗
║                               TABLAS DE VERDAD                              ║
║         AND                                              OR                 ║
║     ===========                                      ==========             ║
║      V  V  | Verdadero                                V V  | V              ║
║      F  V  | Falso                                    F V  | V              ║
║      V  F  | Falso                                    V F  | V              ║
║      F  F  | Falso                                    F F  | F              ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");



#################################################################

print("Ejemplo de operadores OR y AND de comparaciones");
if (dato[0] >= dato[1]) or (dato[2] >= dato[3]):
	
	print ("VERDADERO: ((dato[0] >= dato[1]) or (dato[2] >= dato[3])).");

if (dato[0] >= dato[1]) and (dato[2] >= dato[3]):
	print ("VERDADERO: ((dato[0] >= dato[1]) and (dato[2] >= dato[3])).");

if not ((dato[0] == dato[1]) or (dato[2] == dato[3])):
	print ("VERDADERO: not ((dato[0] == dato[1]) or (dato[2] == dato[3])).");
pausa();limpiar()
#################################################################

print("Ejemplo de operador NOT de comparación");
if not ((dato[0] <= dato[1])):
	print ("NOT (dato[0] <= dato[1])).");
else:
	print ("(dato[0] <= dato[1]))")

#################################################################
x = 10
if not x > 10:
	print("not es True")
else:
	print("not es False")
nuevo(2);

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                Condicionales                                ║
║                                                                             ║
║                                    "if"                                     ║
║                                  is , not is                                ║
╚═════════════════════════════════════════════════════════════════════════════╝

What's the difference between is and ==?
== and is are different comparison! As others already said:
	== compares the values of the objects.
	is compares the references of the objects.
In Python names refer to objects, for example in this case value1 and value2 refer to an int instance storing the value 1000:
value1 = 1000
value2 = value1
value2 refers to the same object is and == will give True:

>>> value1 == value2
True
>>> value1 is value2
True

In the following example the names value1 and value2 refer to different int instances, even if both store the same integer:
>>> value1 = 1000
>>> value2 = 1000

the same value (integer) is stored == will be True, that's why it's often called "value comparison". However is will return False because these are different objects:
>>> value1 == value2
True
>>> value1 is value2
False

When to use which?
Generally is is a much faster comparison. That's why CPython caches (or maybe reuses would be the better term) certain objects like small integers, some strings, etc. But this should be treated as implementation detail that could (even if unlikely) change at any point without warning.

You should only use is if you:
	want to check if two objects are really the same object (not just the same "value"). One example can be if you use a singleton object as constant.
	want to compare a value to a Python constant. The constants in Python are:
		None
		True1
		False1
		NotImplemented
		Ellipsis
		__debug__
		classes (for example int is int or int is float)
		there could be additional constants in built-in modules or 3rd party modules. For example np.ma.masked from the NumPy module)



'==' is an equality test. It checks whether the right hand side and the left hand side are equal objects (according to their __eq__ or __cmp__ methods.)
'is' is an identity test. It checks whether the right hand side and the left hand side are the very same object. No methodcalls are done, objects can't influence the is operation.
You use is (and is not) for singletons, like None, where you don't care about objects that might want to pretend to be None or where you want to protect against objects breaking when being compared against None.

""");
pausa()
#################################################################
print("Ejemplo de operador IN de comparación");
print("array :", dato)
for item in dato:
	if not item in (150,5):
		print ("Items del Array 'not' en mi lista:(25 y 5) " ,item," en ",dato)


#################################################################
print("Ejemplo de operador IS de comparación");

print(dato)

if 5 in dato:
	print("5 SI esta en el array")
else:
	print("5 NO esta en el array")


if 66 not in dato:
	print("66 NO esta en el array")
else:
	print("66 SI esta en el array")
nuevo(3);

#################################################################
print("Ejemplo de comparación sin IF");
#################################################################
print("""
x1 = 5
y1 = 5
x2 = 'Hola'
y2 = 'Hola'
x3 = [1,2,3]
y3 = [1,2,3]
""")
x1 = 5
y1 = 5
x2 = 'Hola'
y2 = 'Hola'
x3 = [1,2,3]
y3 = [1,2,3]
# Output:
print("x1 is not y1:",x1 is y1)#False
print("x1 is not y1:",x1 is not y1)#False
print("x2 is y2:",x2 is y2)#true
print("x3 is y3:",x3 is y3)#False
#################################################################
print("""
x = 'HOLA CURSO'
y = {1:'a',2:'b'}
""")
x = 'HOLA CURSO'
y = {1:'a',2:'b'}
print("'H' in x:",'H' in x)#true
print("'HOLA' not in x :",'HOLA' not in x)#true
print(" 1 in y: ",1 in y)#true
print("'a' in y: ",'a' in y)#false

#################################################################
nuevo(4);
#################################################################
print("\tEjemplos de condicionales varios")
#################################################################
print("El array contiene :"+ str(dato))
var = int(input ("\n\tingrese un numero : "))
if var not in dato:
	print (f" {var} No esta en la lista de datos :{dato}")
else:
	print (f" {var} Si esta en la lista de datos :{dato}")
#################################################################
pausa()
limpiar()
lista_mails =["cursos.agt@gmail.com","cursos.agt_gmail.com","cursos.agt//gmail.com"]
for mail in lista_mails:
	if "@" not in mail:
		#raise ValueError("Reemplace el mail")
		print(f"Seguro que {mail} No es mail xq @ no esta en el array.")
	else:
		print(f"Probablemente {mail} sea un mail xq @ esta en el array.")
#################################################################
pausa()
limpiar()
mail=input("Ingrese su email: ")

if mail is not None and "@" not in mail:
	print(f"Seguro que {mail} No es mail xq @ no esta en el array.")
else:
	print(f"Probablemente {mail} sea un mail xq @ esta en el array.")
pausa()
limpiar()

print("""
list1 = []
list2 = []
list3=list1
""")
list1 = []
list2 = []
list3=list1
print("if (list1 == list2):")
if (list1 == list2):#True
	print("True")
else:
	print("False")


print("if (list1 is list2):")
if (list1 is list2):#false
	print("True")
else:
	print("False")

print("if (list1 == list3):")
if (list1 is list3):#True
	print("True")
else:
	print("False")
pausa()
limpiar()
#################################################################
print("rehacer con par impar")
for i in range(250, 260): a = i; print ("%i: %s" % (i, a is int(str(i))));

#################################################################

pausa()
limpiar()
dato2 = "Ariel"
print("rehacer con input y upper")
if dato2 is "Ariel":
	print ('Si dato2 is "Ariel"')
#################################################################
pausa()
limpiar()

print("""
a = "algo_asi"
b = "algo" + "_" + "asi"
""")
a = "some_string"
b = "some" + "_" + "string"
print("a is b:",a is b)
pausa()
limpiar()
#################################################################

print("""
a = "Ariel"
b = "Ariel"
""")
a = "Ariel"
b = "Ariel"
print("a is b:",a is b)
pausa()
limpiar()
#################################################################

print("""
a = "Ariel!"
b = "Ariel!"
""")
a = "Ariel!"
b = "Ariel!"
print("a is b:",a is b)

print("""
a, b = "Ariel!", "Ariel!"
""")
a, b = "Ariel!", "Ariel!"
print("a is b:",a is b)
pausa()
limpiar()
#################################################################
#Condicional_Ej_02;
print("Multiples condiciones en multiples lineas");
nota_alumno = int(input("Ingreso la nota :"));
if nota_alumno<1:
	valoracion="ir a particular - obligatorio"
elif nota_alumno<=5:
	valoracion="mucha ayuda"
elif nota_alumno<=7:
	valoracion="va bien"
elif nota_alumno<=9:
	valoracion="Muy bien"
elif nota_alumno<=10:
	valoracion="Exelente"
else:
	valoracion="Error al ingresar datos"
print(valoracion);
nuevo(2);
#################################################################
#Condicional_Ej_03;
Edad_alumno=0
print("Condicion maximos y minimos en una linea (concatenados)");
Edad_alumno=int(input("Ingreso la edad del alumno entre 0 y 18 :"));
print (Edad_alumno);
if 0<Edad_alumno<18:
	valoracion="ok es real"
else:
	valoracion="viejo"
print (valoracion);
nuevo(3);
#################################################################
#Condicional_Ej_04;
print("Multiples condiciones en una linea (concatenados)");
nota_1 = int(input("Ingreso la nota del 1er bimestre :"));
nota_2 = int(input("Ingreso la nota del 2er bimestre :"));
nota_3 = int(input("Ingreso la nota del 3er bimestre :"));
nota_4 = int(input("Ingreso la nota del 4er bimestre :"));
if nota_1<nota_2<nota_3<nota_4:
	valoracion="MEJORANDO"
elif nota_1>nota_2>nota_3>nota_4:
	valoracion="DE MAL EN PEOR"
else:
	valoracion="Maso"
print (valoracion);
nuevo(4);
#################################################################
#Condicional_Ej_05;
import math
print("Raiz cuadrada ");
valor=0
valor=int(input("Ingrese numero para sacar raiz cuadrada:"));
if valor>0:
	resultado = math.sqrt(valor);
	print ("la raiz cuadrada de :"+str(valor)+" son los numeros Reales: + -"+str(resultado));
elif valor<0:
	resultado = math.sqrt(abs(valor));
	print ("la raiz cuadrada de :"+str(valor)+" es un numero Imaginario : + -"+str(resultado)+" i ");
	nuevo(5);
#################################################################
#Condicional_Ej_06;
print("cambia el ejercicio anterior para  ");
print("solicionar el ingreso con valor '0'");
nuevo(6);
#################################################################
#Condicional_Ej_07;
print("Multiples condiciones en multiples lineas");
nota_alumno_1 = int(input("Ingreso la nota del 1er parcial :"));
nota_alumno_2 = int(input("Ingreso la nota del 2d0 parcial :"));
def evaluacion(nota1,nota2):#          metodo(clase) o funcion
	print (nota1);
	print (nota2);
	valoracion="aprobado"
	if nota1<5 and nota2<5:
		valoracion="final obligatorio"
	elif nota1<5 and nota2>=5:
		valoracion="RECUPREA 1er parcial"
	elif nota1>=5 and nota2<5:
		valoracion="RECUPREA 2do parcial"
	elif 10>=nota1>=7 and 10>=nota2>=7:
		valoracion="Aprobado sin final"
	elif nota1>10 or nota2>10:
		valoracion="error al cargar los datos"
	return valoracion
print(evaluacion(nota_alumno_1,nota_alumno_2));
print("promedio : "+str((nota_alumno_1+nota_alumno_2)/2));
nuevo(7);
#################################################################
#Condicional_Ej_08;
text_a=" "
text_b=" "
print("condicionales string");
texto_a = input("escriba 2 veces la letra 'A'");
texto_b = input("escriba 4 veces la letra 'b'");
if texto_a=="AA":
	print ("Ok primera parte ");
else:
	print ("NO primera parte escribiste ");
if texto_b=="bbbb":
	print ("Ok segunda parte", texto_b);
else:
	print ("NO segunda parte escribiste ", texto_b);
nuevo(8);
#################################################################
#Condicional_Ej_09;
print("rehacer ej anterior Condicionales string");
texto_a=texto_a.upper()
texto_a=texto_a.lower()
nuevo(9);
#################################################################
#Condicional_Ej_10;
print("Condicionales string")
nombre = (input("Cual es su gracia? :) "));
conocidos=["ARIEL","FACUNDO","ANDREA","JOAQUIN"]
if nombre.upper() in conocidos:#camba por nombres de su entorno
	print("yo te conozco "+str(nombre));
print("Un placer " + nombre + "!");
Edad = input("Tu edad? ");
print("Datos " + str(Edad) + " Años, " + nombre + "!");
nuevo(10);
#################################################################
#Condicional_Ej_11;
print("Lista");
jugadores = ['Batalla', 'Driussi', 'Casco', 'Alario', 'Pity', 'Rojas', 'Ponzio', 'Alonso']
print(jugadores)

print("""
 Para evitar un error con el método remove()
 chequeamos la existencia del ítem antes de
 intentar eliminarlo de la lista.
 """);
if 'Maidana' in jugadores:
	jugadores.remove('Maidana')
else:
	print('Maidana no está en la lista de jugadores.')

if 'Driussi' in jugadores:
	jugadores.remove('Driussi')
else:
	print('Driussi no está en la lista de jugadores.')

print(jugadores)
jugadores.reverse()
print(jugadores)
jugadores.clear()

print(jugadores)
nuevo(11);
#################################################################
#Condicional_Ej_12;

cadena = 'Python'											# asigna cadena a variable
lista = [1, 2, 3, 4, 5]										# declara lista
print("cadena = 'Python'")
print("lista = [1, 2, 3, 4, 5]")
if 'y' in cadena: print('“y” está en “Python”') 			# contiene
if 6 not in lista: print('6 no está en la lista')			# no contiene
print("'abcabc' <---> 'abc' * 2:")
if 'abcabc' is 'abc' * 2: print('Son iguales')				# son iguales
nuevo(12);
#################################################################
#Condicional_Ej_13;
num = int(input("Ingrese un valor :"))
var = "par" if (num % 2 == 0) else "impar"
print (var)
nuevo(13,"fin");
#################################################################
#Condicional_Ej_14;

