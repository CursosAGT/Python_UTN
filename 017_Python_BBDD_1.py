from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                   Bases de Datos                            ║
║                                                                             ║
║                              libreria mysql.connector                       ║
║              https://dev.mysql.com/downloads/connector/python/              ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              Create Database                                ║
║                              Create Table                                   ║
║                              Insert                                         ║
║                              Select                                         ║
║                              Where                                          ║
║                              Order By                                       ║
║                              Delete                                         ║
║                              Drop Table                                     ║
║                              Update                                         ║
║                              Limit                                          ║
║                              Join                                           ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                     MySQL has 3 main categories of data types namely        ║
║                                                                             ║
║                                    Numeric,                                 ║
║                                    Text                                     ║
║                                    Date/time.                               ║
║                                                                             ║
║       Numeric Data types                                                    ║
║       Numeric data types are used to store numeric values. It is very       ║
║         important to make sure range of your data is between lower and upper║
║         boundaries of numeric data types.                                   ║
║                    TINYINT( )    -128 to 127 normal 0 to 255                ║
║                    SMALLINT( )   -32768 to 32767 normal                     ║
║                    MEDIUMINT( )  -8388608 to 8388607 normal                 ║
║                    INT( )        -2147483648 to 2147483647 normal           ║
║                    BIGINT( )     -9223372036854775808 to                    ║
║                                9223372036854775807 normal                   ║
║                    FLOAT         A small approximate number with a floating ║
║                        decimal point.                                       ║
║                    DOUBLE( , )   A large number with a floating decimal     ║
║                        point.                                               ║
║                    DECIMAL( , )  A DOUBLE stored as a string , allowing     ║
║                        for a fixed decimal point. Choice for storing        ║
║                        currency values.                                     ║
║                                                                             ║
║       Text Data Types                                                       ║
║       As data type category name implies these are used to store text values║
║       Always make sure you length of your textual data do not exceed        ║ 
║       maximum lengths.                                                      ║
║                    CHAR( )       A fixed section from 0 to 255 characters   ║
║                    VARCHAR( )    A variable section from 0 to 255 chrs      ║
║                    TINYTEXT      A string with a max. length of 255 chrs.   ║
║                    TEXT          A string with a max. length of 65535       ║
║                    BLOB          A string with a max. length of 65535       ║
║                    MEDIUMTEXT    A string with a max. length of 16777215    ║
║                    MEDIUMBLOB    A string with a max. length of 16777215    ║
║                    LONGTEXT      A string with a max. length of 4294967295  ║
║                    LONGBLOB      A string with a max. length of 4294967295  ║
║                                                                             ║
║       Date / Time                                                           ║
║                    DATE          YYYY-MM-DD                                 ║
║                    DATETIME      YYYY-MM-DD HH:MM:SS                        ║
║                    TIMESTAMP     YYYYMMDDHHMMSS                             ║
║                    TIME          HH:MM:SS                                   ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║       Apart from above there are some other data types in MySQL.            ║
║                                                                             ║
║       ENUM     To store text value chosen from a list of predefined text    ║
║                values                                                       ║
║       SET      This is also used for storing text values chosen from a list ║
║                predefined text values. It can have multiple values.         ║
║       BOOL     Synonym for TINYINT(1), used to store Boolean values         ║
║       BINARY   Similar to CHAR, difference is texts are stored in binary    ║
║                format.                                                      ║
║       VARBINARY   Similar to VARCHAR, difference is texts are stored        ║
║                   in binary format.                                         ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
	python -m pip install mysql-connector 
              pip install mysql-connector-python
https://www.w3schools.com/python/python_mysql_create_db.asp");
http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc36272.1550/html/commands/X72692.htm
""")
limpiar();

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="utn"
)

print(mydb) 

limpiar();
#################################################################
#Clase_BBDD_01 
import mysql.connector
import json

def crear_base(nombre_base_MySQL):
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn")#database='AGT',
	puntero = conectarse.cursor()
	puntero.execute("CREATE DATABASE "+str(nombre_base_MySQL))
	print ("Creamos la base de datos "+str(nombre_base_MySQL))
	print ("cerramos coneccion")
	puntero.close
def listar_bases():
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn")
	puntero = conectarse.cursor()
	puntero.execute("SHOW DATABASES")
	lista_de_bases=[]
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (puntero):
		lista_nombres_bases=str(lista_bases)
		lista_nombres_bases_largo=len(lista_bases)-4
		lista_nombres_bases=lista_nombres_bases[2:lista_nombres_bases_largo]
		print ("*"+lista_nombres_bases+"*")
		lista_de_bases.append(lista_nombres_bases);
	print (lista_de_bases)
	print ("cerramos coneccion")
	puntero.close
	return (lista_de_bases)

def chequear_base_existe(nombre_base_MySQL_input):
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn")
	puntero = conectarse.cursor()
	puntero.execute("SHOW DATABASES")
	lista_de_bases=[]
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (puntero):
		nombre_base_MySQL_para_chequear=str(lista_bases)
		nombre_largo=len(lista_bases)-4
		nombre_base_MySQL_para_chequear=nombre_base_MySQL_para_chequear[2:nombre_largo]
		lista_de_bases.append(nombre_base_MySQL_para_chequear);
	puntero.close
	print ("cerramos coneccion")
	print (lista_de_bases)
	lista_bases_2=json.loads(lista_bases);
	lista_de_bases_2.append(lista_bases_2);
	print(lista_de_bases);
	print(lista_de_bases_2);
	base_nueva=False
	while base_nueva==False:
		for nombre_base_MySQL in (lista_de_bases):
			if nombre_base_MySQL_input == nombre_base_MySQL:
				nombre_base_MySQL_input= input("Ingrese un nuevo nombre de la base de datos MySQL "+str(nombre_base_MySQL_input)+" ya existe :")
				break
			else:
				if len(nombre_base_MySQL) == len(lista_de_bases):
					print (f"Genial '{nombre_base_MySQL_input}' no existe. pasamos a crear la base de datos en MySQL")
					base_nueva=True
	return (nombre_base_MySQL_input)
	
def listar_tablas(nombre_base_MySQL_input):
	print ("Conectamos con MySQL")
	print (nombre_base_MySQL_input)
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database=nombre_base_MySQL_input,)
	puntero = conectarse.cursor()
	puntero.execute("SHOW TABLES")
	lista_de_tablas=[]
	print ("cargamos el listado de tabla de la base"+str(nombre_base_MySQL_input))
	for lista_tablas in (puntero):
		print(lista_tablas)
		lista_nombres_tablas=str(lista_tablas)
		print ("*"+str(lista_nombres_tablas)+"*")
		lista_de_tablas.append(lista_nombres_tablas);
	puntero.close
	return (lista_de_tablas)

def borrar_base(nombre_base_MySQL_input):
	limpiar();
	listar_bases()
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn")
	puntero = conectarse.cursor()
	puntero.execute("DROP DATABASE "+str(nombre_base_MySQL_input))
	puntero.close

limpiar()
#################################################################
 
while True:
	print ("\n\n\n");	
	print ("L) listar Base");
	print ("C) Crear Base");
	print ("A) Abrir Base");
	print ("B) Borrar Base");	
	print ("Z) Salir del programa")
	opcion= input("Opcion : ")
	opcion=opcion.upper()
	if opcion =="C":
		limpiar();
		nombre_base_MySQL= input("Ingrese el nombre de la base de datos a CREAR : ")
		crear_base(nombre_base_MySQL)
	elif opcion =="L":
		limpiar();
		listar_bases()
	elif opcion =="A":
		limpiar();
		nombre_base_MySQL= input("Ingrese el nombre de la base de datos a ABRIR : ")
		listar_tablas(nombre_base_MySQL)
	elif opcion =="B":
		limpiar();
		nombre_base_MySQL= input("Ingrese el nombre de la base de datos a BORRAR : ")
		borrar_base(nombre_base_MySQL)
	elif opcion =="Z":
		limpiar();
		break
		
		

"""

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 
#print(f"Hola {nombre_base_MySQL} se que tenes {edad} años.")

#func_crear(nuevo_nombre_base_MySQL)
"""
"""
def check_base_existe(nombre_base_MySQL_input):
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn")
	puntero = conectarse.cursor()
	puntero.execute("SHOW DATABASES")
	lista_de_bases=[]
	
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (puntero):
		nombre_base_MySQL_para_chequear=str(lista_bases)
		nombre_largo=len(lista_bases)-4
		nombre_base_MySQL_para_chequear=nombre_base_MySQL_para_chequear[2:nombre_largo]
#		print ("*"+nombre_base_MySQL_para_chequear+"*", "*"+nombre_base_MySQL_input+"*")
		lista_de_bases.append(nombre_base_MySQL_para_chequear);
	puntero.close
	print ("cerramos coneccion")
	print (lista_de_bases)
	c=0
	base_nueva=False
	while base_nueva==False:
		input("while"+str(base_nueva))
		c +=1
		print (c)
		for nombre_base_MySQL in (lista_de_bases):
			if nombre_base_MySQL_input == nombre_base_MySQL:
				print ("*"+nombre_base_MySQL_input+"*", "*"+nombre_base_MySQL+"*         ==")
				input("=="+str(base_nueva))
				nombre_base_MySQL_input= input("Ingrese un nuevo nombre de la base de datos MySQL "+str(nombre_base_MySQL_input)+" ya existe :")
				break
			else:
				if len(nombre_base_MySQL) == len(lista_de_bases):
					print (f"Genial '{nombre_base_MySQL_input}' no existe. pasamos a crear la base de datos en MySQL")
					base_nueva=True
				else:
					print ("*"+nombre_base_MySQL_input+"*", "*"+nombre_base_MySQL+"*         =/=")
					input("=/="+str(base_nueva))
		input("Fin"+str(base_nueva))
	print (lista_de_bases)
	print (nombre_base_MySQL_input)
	return (nombre_base_MySQL_input)
nombre_base_MySQL= "mysql"#input("Ingrese el nombre de la base de datos MySQL : ")
print(check_base_existe(nombre_base_MySQL))
"""
