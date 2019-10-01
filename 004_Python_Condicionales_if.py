from Estructura import *
nuevo(0,"inicio");
#################################################################
#Condicional_Ej_01;
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                Condicionales                                ║
║                                                                             ║
║                                    "if"                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
dato = [99, 25, 50, 5];
print (dato)
print("Ejemplo de operador de comparación Igual:");

if (dato[0] == dato[1]):
	print ("'dato[0]' y 'dato[1]' son iguales.");
else:
	print ("'dato[0]' y 'dato[1]' no son iguales.");

print("Ejemplo de operador de comparación Distinto:");

if (dato[0] != dato[1]):
	print ("'dato[0]' y 'dato[1]' son distintas.");
else:
	print ("'dato[0]' y 'dato[1]' no son distintas.");

print("Ejemplo de operador de comparación Menor que:");

if (dato[0] < dato[1]):
	print ("'dato[0]' es menor que 'dato[1]'.");
else:
	print ("'dato[0]' no es menor que 'dato[1]'.");

print("Ejemplo de operador de comparación Mayor que:");

if (dato[0] > dato[1]):
	print ("'dato[0]' es mayor que 'dato[1]'.");
else:
	print ("'dato[0]' no es mayor que 'dato[1]'.");

print("Ejemplo de operador de comparación Menor o igual que:");

if (dato[2] <= dato[3]):
	print ("'dato[2]' es menor o igual que 'dato[3]'.");
else:
	print ("'dato[2]' no es menor o igual que 'dato[3]'.");

print("Ejemplo de operador de comparación Mayor o igual que:");

if (dato[3] >= dato[2]):
	print ("'dato[3]' es mayor o igual que 'dato[2]'.");
else:
	print ("'dato[3]' no es mayor o igual que 'dato[2]'.");


if ((dato[0] >= dato[1])) or ((dato[2] >= dato[3])):
	print ("(dato[0] >= dato[1])) or ((dato[2] >= dato[3]).");

if ((dato[0] >= dato[1])) and ((dato[2] >= dato[3])):
	print ("(dato[0] >= dato[1])) and ((dato[2] >= dato[3]).");

if ((dato[0] >= dato[1])) != ((dato[2] >= dato[3])):
	print ("(dato[0] >= dato[1])) != ((dato[2] >= dato[3]).");
else:
	print ("NO  (dato[0] >= dato[1])) != ((dato[2] >= dato[3]).");

if not ((dato[0] <= dato[1])):
	print ("NOT (dato[0] <= dato[1])).");
else:
	print ("(dato[0] <= dato[1]))") 


var = int(input ("ingrese un numero : "))
if var not in dato:
	print (f" {var} No esta en la lista de datos :{dato}")
else:
	print (f" {var} Si esta en la lista de datos :{dato}")
nuevo(1);
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
	print ("la raiz cuadrada de :"+str(valor)+" son los nomeros Reales: + -"+str(resultado));
elif valor<0:
	resultado = math.sqrt(abs(valor));
	print ("la raiz cuadrada de :"+str(valor)+" es un numero Imaginario : + -"+str(resultado)+" i donde i");
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
texto_a=texto_a.upper
texto_a=texto_a.lower
nuevo(9);
#################################################################
#Condicional_Ej_10;
print("Condicionales string");
nombre = " "
nombre = str(input("Cual es su gracia? :) "));
if nombre==("Ariel","Segundo Nombre","Andrea","Primer Nombre"):
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
nuevo(13,"fin");
#################################################################
