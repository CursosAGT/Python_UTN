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
║                               Bucles // Do while                            ║
║                                                                             ║
║                             "NO EXISTE EN Python"                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
limpiar();
#################################################################
#Clase_While_Ej_01
edad=0
print ("venta de alcohol en boliches");
x = True

while x :
	edad=int(input("ingrese su edad :"));
	if edad <= 18:
		print ("Cometió un error al ingresar la edad o es menor y debe retirarse");
		x = True
	else:
		print("que desea beber.......fin....");
		x = False
nuevo(1);
