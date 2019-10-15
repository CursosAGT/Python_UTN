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
║                                 "swich case"                                ║
║                                                                             ║
║                             "NO EXISTE EN Python"                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");

def switch_mes(dato):
	switcher = {
				1: "Enero",
				2: "Febrero",
				3: "Marzo",
				4: "Abril",
				5: "Mayo",
				6: "Junio",
				7: "Julio",
				8: "Agosto",
				9: "Septiembre",
				10: "Octubre",
				11: "Noviembre",
				12: "Diciembre"
	}
	return switcher.get(dato,"Mes Invalido")
dato=int(input("Ingrese el mes entre 1 y 12 :"))
print(switch_mes(dato))
nuevo(1);
#################################################################
#Condicional_Ej_02;

def primero():
	return "Enero"
def segundo():
	return "Febrero"
def tercero():
	return "Marzo"
def cuarto():
	return "Abril"
def quinto():
	return "Mayo"
def sexto():
	return "Junio"
def septimo():
	return "Julio"
def octavo():
	return "Agosto"
def noveno():
	return "Septiembre"
def decimo():
	return "Octubre"
def decimoprimero():
	return "Noviembre"
def decimosegundo():
	return "Diciembre"
def meses(argumento):
	switcher = {
		1: primero,
		2: segundo,
		3: tercero,
		4: cuarto,
		5: quinto,
		6: sexto,
		7: septimo,
		8: octavo,
		9: noveno,
		10: decimo,
		11: decimoprimero,
		12: decimosegundo
	}
	func = switcher.get(argumento, lambda: "Mes Invalido")
	print (func())
dato=int(input("Ingrese el mes entre 1 y 12 :"))
meses(dato)
nuevo(2);
#################################################################
#Condicional_Ej_03;
def sal():
	return "salir";
salir = "jugar";
print (salir)
switch_case = {
	8 : "El jugador sube la  la cuesta",
	2 : "El jugador sube la cuesta",
	4 : "El jugador gira a la izquierda",
	6 : "El jugador gira a la derecha",
	}

print(switch_case.get(int(input("usa el pad numérico del teclado (valores 8,2,4,6-5 para salir:)"))))
nuevo(3);
#################################################################
#Condicional_Ej_04;
def east(): return "Este"
def west(): return "Oeste"
def north(): return "Norte"
def south(): return "Sur"
# map the inputs to the function blocks
switch_case = {
          1 : east,
          2 : west,
          3 : north,
          4 : south
         }
dato=int(input("opciones 1234:"))
print(switch_case[dato]())
nuevo(4);
#################################################################
