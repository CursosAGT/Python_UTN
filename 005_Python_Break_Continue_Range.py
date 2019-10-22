from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aquí las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                For       break  // continue // range                        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
nuevo(0,"inicio");
Nombre_lista_1 = ["linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 10"]
print ("lista original :",Nombre_lista_1);
#################################################################
#Clase_break/continue/range_Ej_01
for dato_1 in Nombre_lista_1:
	print(dato_1)#<---------------------print
	if dato_1 == "linea 5":
		break#    <---------------------Break

print('Exit the loop when dato_1 is "linea 5", but this time the break comes before the print:');

for dato_1 in Nombre_lista_1:
	if dato_1 == "linea 5":
		break#    <---------------------Break
	print(dato_1)#<---------------------print
nuevo(1);
#################################################################
#Clase_break/continue/range_Ej_02
print('The continue Statement');
print('With the continue statement we can stop the current iteration of the loop, and continue with the next:');
print('Do not print linea 5:');
for dato_1 in Nombre_lista_1:
	if dato_1 == "linea 5":
		print("\t\t<------------------hey UTN's aquí esta");
		continue
	print(dato_1)
nuevo(2);
#################################################################
#Clase_break/continue/range_Ej_03
print('The continue Statement');
print('With the continue statement we can stop the current iteration of the loop, and continue with the next:');
print('Do not print linea 5:');
for dato_1 in Nombre_lista_1:
	if dato_1 == "linea 5":
		print("\t\t<------------------hey UTN's aquí esta");
		continue
	elif dato_1 == "linea 7":
		break;#	exit()				probar con exit
	print(dato_1)
nuevo(3);
#################################################################
#Clase_break/continue/range_Ej_04
print("for continue / break /else ");
cadena_de_caracteres=" "
cont_de_a =0
cont_de_b =0
cont_de_c =0
otras_letras =0
contador_de_letras = 0
cadena_de_caracteres=str(input("Ingrese strings y tipee  '#' para finalizar "));
for letra in cadena_de_caracteres:
	if letra==" ":
		continue
	contador_de_letras = contador_de_letras + 1
	if letra=="#":
		print ("break");
		fin=True
		break
	if letra=="a":
		cont_de_a +=1
	elif letra=="b":
		cont_de_b +=1
	elif letra=="c":
		cont_de_c +=1
	else:
		otras_letras +=1
else:
	fin=False
print (str("hay "+str(contador_de_letras)+" letras en el string ingresado" + str(cadena_de_caracteres)));
print (str("hay "+str(cont_de_a)+"letras 'A' en el string ingresado " + str(cadena_de_caracteres)));
print (str("hay "+str(cont_de_b)+"letras 'B' en el string ingresado " + str(cadena_de_caracteres)));
print (str("hay "+str(cont_de_c)+"letras 'C' en el string ingresado " + str(cadena_de_caracteres)));
print (str("hay "+str(otras_letras)+" 'otras letras' en el string ingresado" + str(cadena_de_caracteres)));
if fin:
	print("el programa se bloqueo con #");
else:
	print("el programa llego al fin");
nuevo(4);

for letra in "Python-UTN":
    if letra == "-":
        break
    print ("Letra actual : " + letra)

# Segundo ejemplo
for var in range(11,0,-1):
    if var == 5:
        break
    print ("Valor actual de la variable : " + str(var))
print ("fin del script")


var = 10
while var > 0:
    var = var -1
    if var == 5:
        break
    print ("Valor actual de la variable : " + str(var))

print ("fin del script")
