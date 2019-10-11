from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Ingreso de datos por teclado                   ║
║                              salida de datos por consola                    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://www.w3schools.in/python-tutorial/gui-programming/
""");
nota_alumno_1 = input("Ingreso la nota del 1er parcial :");
nota_alumno_1 = int(nota_alumno_1);
nota_alumno_2 = int(input("Ingreso la nota del 2d0 parcial :"));
print ("1er parcial : "+str(nota_alumno_1));
print ("2do parcial : "+str(nota_alumno_2));
print ("promedio : "+str((nota_alumno_1+nota_alumno_2)/2));
nuevo(1);
#################################################################
#IO Ej_02
valor1=0.1;

valor2=0.1;
valor1=float(input("valor de la mercaderia 1 : "));
valor2=float(input("valor de la mercaderia 2 : "));

resultado_suma= valor1+valor2
resultado_resta=valor1-valor2
resultado_multiplica=valor1*valor2
resultado_divide=valor1/valor2

print ("la suma de los valores es "+str(resultado_suma)+" pesos");
print ("la devolucion genera una resta cuyo saldo es de "+str(resultado_resta)+" pesos");
print ("la multiplicacion de ambos valores es de " +str(resultado_multiplica)+" pesos", end=" ");
print (" y la deivion es de "+str(resultado_divide)+" aunque esto no sirve para nada");
nuevo(2);
#################################################################
#IO Ej_03
edad=int(input("Ingere su edad : "));
if edad<0:
	print("error");
if edad<=2:
	print("bebe");
if edad<=10:
	print("Chico");
if edad<=15:
	print("pavo");
if edad<=20:
	print("Ni ni");
if edad<=30:
	print("A laburar");
if edad>=40:
	print("te crece la panza y se cae todo, hasta el pelo");
nuevo(3);
#################################################################
#IO Ej_04
print ("rehacer IO Ej_03  con  'elif y else>'");
print ("rehacer IO Ej_03  con parametros de '>'");
nuevo(4);
#################################################################
#IO Ej_05
valoracion="aprobado"
print("multiples condiciones en multiples lineas");
nota_alumno_1 = int(input("Ingreso la nota del 1er parcial :"));
nota_alumno_2 = int(input("Ingreso la nota del 2d0 parcial :"));
def evaluacion(nota1,nota2):
	valoracion="aprobado"
	if nota1<5 and nota2<5:
		valoracion="final obligatorio"
	elif nota1<5 and nota2>=5:
		valoracion="RECUPREA 1er parcial"
	elif nota1>=5 and nota2<5:
		valoracion="RECUPREA 2do parcial"
	elif nota1>=7 and nota2>=7:
		valoracion="Aprobado sin final"
	return valoracion
print(evaluacion((nota_alumno_1),(nota_alumno_2)));
print("promedio : "+str((nota_alumno_1+nota_alumno_2)/2));
nuevo(5);
#################################################################
#IO Ej_06
Edad_alumno = 0
valoracion="ok"
print("condicion maximos y minimos en una linea (concatenados)");
Edad_alumno = int(input("Ingreso la edad del alumno :"));
print (Edad_alumno);
if 0<Edad_alumno<100:
	valoracion="ok"
else:
	valoracion="Error"
print (valoracion);
nuevo(6);
#################################################################
#IO Ej_07
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
nuevo(7);
#################################################################
#IO Ej_08
print("multiples condiciones en una linea (concatenados)");
print (" el ej anterior con arreglos por notas");
print ("					<0 - out");
print ("				entre	0  y <4  - ");
print ("				entre	4  y <6  - ");
print ("				entre	6  y <8  - ");
print ("				entre	8  y <10  - ");
print ("					>10 - out");
nuevo(8);
#################################################################
#IO Ej_09
print("isalnum()	Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.");
print("isalpha()	Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.");
print("isdigit()	Returns true if string contains only digits and false otherwise.");
print("islower()	Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.");
print("isnumeric()	Returns true if a unicode string contains only numeric characters and false otherwise.");
print("leer\nhttp://pyspanishdoc.sourceforge.net/lib/string-methods.html");
texto_en_memoria="1973"
print("texto_en_memoria : "+str(texto_en_memoria));
print("isalnum : "+str(texto_en_memoria.isalnum()));
print("---------------------------------------------------------------------");
print("isalpha : "+str(texto_en_memoria.isalpha()));
print("---------------------------------------------------------------------");
print("isdigit : "+str(texto_en_memoria.isdigit()));
print("---------------------------------------------------------------------");
texto_en_memoria="arribaUTN"
print("texto_en_memoria : "+str(texto_en_memoria));
print("isalnum : "+str(texto_en_memoria.isalnum()));
print("---------------------------------------------------------------------");
print("isalpha : "+str(texto_en_memoria.isalpha()));
print("---------------------------------------------------------------------");
print("isdigit : "+str(texto_en_memoria.isdigit()));
print("---------------------------------------------------------------------");
texto_en_memoria="Arielnacioen1973"
print("texto_en_memoria : "+str(texto_en_memoria));
print("isalnum : "+str(texto_en_memoria.isalnum()));
print("---------------------------------------------------------------------");
print("isalpha : "+str(texto_en_memoria.isalpha()));
print("---------------------------------------------------------------------");
print("isdigit : "+str(texto_en_memoria.isdigit()));
print("---------------------------------------------------------------------");
nuevo(9,"fin");
#################################################################
#IO Ej_07

