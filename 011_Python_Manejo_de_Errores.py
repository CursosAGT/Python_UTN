from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                Manejo de errores                            ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

https://www.w3schools.in/python-tutorial/gui-programming/


try:
     cociente = dividendo / divisor");
 except:
     print ("No se permite la división por cero");
#################################################################
try:
     aquí ponemos el código que puede lanzar excepciones
except:
     ERROR de sintaxis, esta sentencia no puede estar aquí,
     sino que debería estar luego del except IOError.
except IOError:
     Manejo de la excepción de entrada/salida
#################################################################
try:
    archivo = open("miarchivo.txt")
     procesar el archivo
except IOError:
    print "Error de entrada/salida."
     realizar procesamiento adicional
except:
     procesar la excepción
finally:
 	si el archivo no está cerrado hay que cerrarlo
   if not(archivo.closed):
	archivo.close()
""")
nuevo(0,"inicio");
#################################################################
#Clase_Errores_Ej_001
print("Ingresa los datos con errores Ej números en string")
try:
	maximo = int(input("ingrese la cantidad de numeros :"));
except:
	print ("ha ocurrido un Error. pero sigo con un valor = 10");
	maximo = 10
if maximo>0:
	def numeros_pares(maximo):
		contador = 1
		lista_de_pares=[]
		while contador<=maximo:
			lista_de_pares.append(contador*2);
			contador+=1
		return lista_de_pares
	print (numeros_pares(maximo));
nuevo(1);
#################################################################
#Clase_Errores_Ej_002
try:
	print("""
	x = 10
	y = 0
	print(x/y)##nunca dividirás por cero
	""")
	x = 10
	y = 0
	print(x/y)##nunca dividirás por cero
except Exception as dato_error:
	print("Ocurrió un error o excepción // Exeception occured:{}".format(dato_error))
finally:
	x = 10
	y = 2
	print(x/y)
print ("continuo")
nuevo(2);
#################################################################
#Clase_Errores_Ej_003
import math
print("Ingrese valores numéricos para funcionar y no numéricos par generar un error");
while True:
	try:
		print("""
		valor1=float(input("valor 1 : "));
		valor2=float(input("valor 2 : "));
		""")
		valor1=float(input("valor 1 : "));
		valor2=float(input("valor 2 : "));
		break
	except ValueError:
		print("Error. solo nomeros");
def resultado_suma(valor_1,valor_2):
	return valor_1+valor_2
def resultado_resta(valor_1,valor_2):
	return  valor_1-valor_2
def resultado_multiplica(valor_1,valor_2):
	return valor_1*valor_2
def resultado_divide(valor_1,valor_2):
	try:
		return valor_1/valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
def resultado_portenciacion(valor_1,valor_2):
	return valor_1**valor_2
def resultado_radicacion2(valor_1,valor_2):
	return  math.sqrt(valor_2);
def resultado_porcentage(valor_1,valor_2):
	try:
		return valor_1/valor_2*100
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
def resultado_cociente(valor_1,valor_2):
	try:
		return valor_1//valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
def resultado_resto(valor_1,valor_2):
	try:
		return valor_1%valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
print ("resultado suma : "+str(resultado_suma(valor1,valor2)));
print ("resultado resta : "+str(resultado_resta(valor1,valor2)));
print ("resultado multiplicacion : "+str(resultado_multiplica(valor1,valor2)));
print ("resultado divicion : "+str(resultado_divide(valor1,valor2)));
print ("resultado portenciacion : "+str(resultado_portenciacion(valor1,valor2)));
print ("resultado radicacion2 : "+str(resultado_radicacion2(valor1,valor2)));
print ("resultado porcentage : "+str(resultado_porcentage(valor1,valor2)));
print ("resultado cociente : "+str(resultado_cociente(valor1,valor2)));
print ("resultado resto : "+str(resultado_resto(valor1,valor2)));
nuevo(3);
#################################################################
#Clase_Errores_Ej_004
from Python_Metodos_propia import *#<-------------------------------------------------------------via archivo externo

nuevo(4);
#################################################################
#Clase_Errores_Ej_004
lista = [1, 2, 3, 4, 5, 6, 7, 8]
iterador = iter(lista)
try:
    while True:
        print("DATO DEL ITERADOR",iterador.__next__())
except StopIteration:
    print("Se ha alcanzado el final de la lista")
nuevo(4);
#################################################################
#Clase_Errores_Ej_005

area_triangulo =lambda base,altura:(base*altura)/2
while True:
	try:
		base = float(input("Ingrese la base :"))
		altura = float(input("Ingrese la altura :"))
		break
	except ValueError:
		print("Error. solo nomeros");
print(area_triangulo(base,altura))
nuevo(5);
#################################################################
#Clase_Errores_Ej_006
import calendar
while True:
	try:
		año=int(input("Año :"))
		mes=int(input("Mes (en numeros):"))
		break
	except ValueError:
		print("Error. solo nomeros");
calendario = calendar.month(año, mes)
print(f"Verifique por favor:\n {calendario}")
nuevo(7);
#################################################################
#Clase_Errores_Ej_007
print("Diferencia de dos fechas en días, introducidas por teclado")

from datetime import datetime

def main():
# Establecer formato de las fechas a introducir: dd/mm/aaaa
	formato = "%d/%m/%Y"
# Bucle 'sin fin'
	while True:
		try:
	# Introducir fecha inicial utilizando el formato definido
			fecha_desde = input('Introducir fecha inicial en formato (dd/mm/aaaa): ')
	# Si no se introduce ningún valor se fuerza el final del bucle
			if fecha_desde == "":
				break
	# Introducir fecha final utilizando el formato definido
			fecha_hasta = input('Introducir fecha final en formato  (dd/mm/aaaa): ')
	# Si no se introduce ningún valor se fuerza el final del bucle
			if fecha_hasta == "":
				break
	# Se evaluan las fechas según el formato dd/mm/aaaa
	# En caso de introducirse fechas incorrectas se capturará la excepción o error
			fecha_desde = datetime.strptime(fecha_desde, formato)
			fecha_hasta = datetime.strptime(fecha_hasta, formato)
	# Se comprueba que fecha_hasta sea mayor o igual que fecha_desde
			if fecha_hasta >= fecha_desde:
		# Se cálcula diferencia en día y se muestra el resultado
				diferencia = fecha_hasta - fecha_desde
				print("Diferencia:", diferencia.days, "días")
			else:
				print("La fecha fecha final debe ser mayor o igual que la inicial")
		except:
			print('Error en la/s fecha/s. ¡Inténtalo de nuevo!')
			return 0

if __name__ == '__main__':
	main()
nuevo(8);
#################################################################
#Clase_Errores_Ej_009
""""""
nuevo(9);
#################################################################
#Clase_Errores_Ej_010
"""inventa un ejercicio donde ingreses una fecha y chequees el contenido para validarlo """
nuevo(10);
#################################################################
#Clase_Errores_Ej_011
import mysql.connector#<------------------------------------------------debe estar disponible
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='utn_2019',
                                         user='root',
                                         password='utn')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
nuevo(11,"fin");
#################################################################
