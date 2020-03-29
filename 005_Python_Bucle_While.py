from Estructura import *
nuevo(0,"inicio");
#################################################################
import math
def Ej_ya_hechos():
	#Con tab colocaremos aquí las prácticas hechas
	pass

	print("""
	╔═════════════════════════════════════════════════════════════════════════════╗
	║                                                                             ║
	║                               Bucles // while                               ║
	║                                                                             ║
	╚═════════════════════════════════════════════════════════════════════════════╝
	""");
	nuevo(0,"inicio");
	#################################################################
	#Clase_While_Ej_01
	contador = 0
	while contador<=100:
		print (contador);
		contador +=10
	print ("FIN");
	nuevo(1);
	#################################################################
	#Clase_While_Ej_02
	edad=0
	print ("venta de alcohol en boliches");
	edad=int(input("ingrese su edad :"));
	while edad<18:
		print ("Cometió un error al ingresar la edad o es menor y debe retirarse");
		edad=int(input("ingrese su edad :"));
	else:
		print("que desea beber.......fin....");
	nuevo(2);
	#################################################################
	#Clase_While_Ej_03
	print(" break" );
	print ("venta de alcohol en boliches");
	edad=int(input("ingrese su edad :"));
	while edad<18:
		print ("Cometió un error al ingresar la edad o es menor debe ingresar un valor'<10' y retirarse");
		edad=int(input("ingrese su edad :"));
		if edad<=10:
			print ("toma una cindor y Adios");
			break
	else:
		print("que desea beber.......fin....");
	nuevo(3);
	#################################################################
	#Clase_While_Ej_04
	print(" break" );
	print ("venta de alcohol en boliches");
	edad=int(input("ingrese su edad :"));
	while edad<18:
		print ("Cometió un error al ingresar la edad o es menor debe ingresar un valor'<10' y retirarse");
		edad=int(input("ingrese su edad :"));
		if edad<=10:
			print ("toma una cindor y Adios");
			break
	else:
		print("que desea beber.......fin....");
	nuevo(4);
		#################################################################
	#Clase_While_Ej_05
	valor=0
	print("librería math");
	valor=int(input("Ingrese numero para sacar raíz cuadrada:"));
	while valor<0:
		valor=int(input("Ingreso un numero negativo. Ingrese un numero para sacar raíz cuadrada:"));
	resultado = math.sqrt(valor);
	print ("la raiz cuadrada de :"+str(valor));
	print ("son : + -"+str(resultado));
	nuevo(5);

	#################################################################
	#Clase_While_Ej_06

	print("""
	╔═════════════════════════════════════════════════════════════════════════════╗
	║                                                                             ║
	║                                   while                                     ║
	║                                                                             ║
	║                               or , and , not                                ║
	╚═════════════════════════════════════════════════════════════════════════════╝
	""");
	salir = False
	while salir!=True:# not  salir==True:#  salir==False
		entrada = input("ingrese un string o zz para salir :")
		if entrada.lower() == "zz":
			salir = True
			print("Chau")

		else:
			print ("Ud.ingreso :",entrada)
	nuevo(6);

	#################################################################
	#Clase_While_Ej_07
	#pandemia
Asia=False
Europa=False
Americadelnorte=False
Americadelsur=False
Africa=False
Oceania=False
mayortres=0
contador=0
while mayortres<3 and contador<6:
	contador+=1
	print("contador de anios:",contador)
	mayortres=0
	dato1=input("esta africa afectada? V/F")
	if dato1.upper()=="V":
		print ("Africa Afectada")
		mayortres+=1
	else : print ("Africa no Afectada")
	dato2=input("esta europa afectada? V/F")
	if dato2.upper()=="V":
		print ("europa Afectada")
		mayortres+=1
	else : print ("europa no Afectada")
	dato3=input("esta asia afectada? V/F")
	if dato3.upper()=="V":
		print ("asia Afectada")
		mayortres+=1
	else : print ("asia no Afectada")
	dato4=input("esta americadelnorte afectada? V/F")
	if dato4.upper()=="V":
		print ("America del norte Afectada")
		mayortres+=1
	else : print ("America del norte no Afectada")
	dato5=input("esta oceania afectada? V/F")
	if dato5.upper()=="V":
		print ("oceania Afectada")
		mayortres+=1
	else : print ("oceania no Afectada")
	dato6=input("esta merica del sur afectada? V/F")
	if dato6.upper()=="V":
		print ("America del sur Afectada")
		mayortres+=1
	else : print ("America del sur no Afectada")
if contador<6:
	print("estamos en pandemia")
else:
	print("no hay pandemia")
	
