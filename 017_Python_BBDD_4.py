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
Scripts>python -m pip install mysql-connector
https://www.w3schools.com/python/python_mysql_create_db.asp
""")
limpiar();
#################################################################
#Clase_BBDD_01 

import mysql.connector
def crear_base():
	try:
		nombre_DDBB = input("ingrese el nombre de la base de datos a crear : ")
		nombre_DDBB = nombre_DDBB.capitalize()
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn")#database='nombre',
		cursor = connection.cursor()
		cursor.execute("CREATE DATABASE "+str(nombre_DDBB))
		print ("Creamos la base de datos  "+str(nombre_DDBB))
		print ("cerramos coneccion")
		cursor.close
		print (input("		continuar?"));
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close
def listar_bases():
	try:
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn")
		cursor = connection.cursor()
		cursor.execute("SHOW DATABASES")
		print ("Mostramos las bases de datos  ")
		lista_de_bases=[]
		for lista_bases in (cursor):
			lista_nombres_bases=str(lista_bases)
			lista_nombres_bases_largo=len(lista_bases)-4
			lista_nombres_bases=lista_nombres_bases[2:lista_nombres_bases_largo]
			print ("*"+lista_nombres_bases+"*")
			lista_de_bases.append(lista_nombres_bases);
		print (lista_de_bases)
		print ("cerramos coneccion")
		cursor.close
		print (input("		continuar?"));
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close
def borrar_base():
	listar_bases()
	try:
		nombre_DDBB = input("ingrese el nombre de la BASE (QUE YA DEBE EXISTIR) de datos para insertar tablas  : ")
		nombre_DDBB = nombre_DDBB.capitalize()
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn")
		cursor = connection.cursor()
		accion = input ("Drop la DDBB (S/N)")
		if accion.upper() == "S":
			print ("Borramos la base de datos ", nombre_DDBB )
			cursor.execute("DROP DATABASE "+str(nombre_DDBB))
		cursor.close
		print (input("		continuar?"));
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close
def crear_tablas():
	try:
		nombre_DDBB = input("ingrese el nombre de la BASE (QUE YA DEBE EXISTIR) de datos para insertar tablas  : ")
		nombre_DDBB = nombre_DDBB.capitalize()
		nombre_tabla = input("ingrese el nombre de la nombre TABLA a crear : ")
		nombre_tabla = nombre_tabla.upper()
		nombre_columna_1 = input("ingrese el nombre de la nombre de la COLUMNA 1 a crear : ")
		nombre_columna_1 = nombre_columna_1.upper()
		nombre_columna_2 = input("ingrese el nombre de la nombre de la COLUMNA 2 a crear : ")
		nombre_columna_2 = nombre_columna_2.upper()
		nombre_columna_3 = input("ingrese el nombre de la nombre de la COLUMNA 3 a crear : ")
		nombre_columna_3 = nombre_columna_3.upper()
		
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn",database=str(nombre_DDBB))
		cursor = connection.cursor()
#		cursor.execute("CREATE TABLE "+str(nombre_tabla)+" (id INT AUTO_INCREMENT PRIMARY KEY, "+str(nombre_columna_1)+" VARCHAR(255), "+str(nombre_columna_2)+" INT, "+str(nombre_columna_3)+" VARCHAR(255))")
		cursor.execute("CREATE TABLE "+str(nombre_tabla)+" ( "+str(nombre_columna_1)+" VARCHAR(255), "+str(nombre_columna_2)+" INT, "+str(nombre_columna_3)+" VARCHAR(255))")
		cursor.execute("USE "+str(nombre_DDBB)); # select the database
		cursor.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)
		tablas = cursor.fetchall()       # return data from last query
		cursor.execute("SHOW columns FROM "+str(nombre_tabla))
		for column in cursor.fetchall():
			print (column[nombre_tabla]);
		print (tablas)
		print ("cerramos coneccion")
		cursor.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close
def agregar_id_tablas():
	try:
		nombre_DDBB = input("ingrese el nombre de la base(QUE YA DEBE EXISTIR) de datos para insertar ID  : ")
		nombre_DDBB = nombre_DDBB.capitalize()
		nombre_tabla = input("ingrese el nombre de la nombre TABLA (QUE  YA DEBE EXISTIR) para insertar ID  : ")
		nombre_tabla = nombre_tabla.upper()
		print ("Conectamos con MySQL ", nombre_DDBB )
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn",database=str(nombre_DDBB))
		cursor = connection.cursor()
		cursor.execute("ALTER TABLE "+str(nombre_tabla)+" ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 
		cursor.execute("SHOW TABLES")
		print ("Mostramos las tablas de la bases de datos UTN_practica1_2019")
		lista_de_tablas=[]
		for lista_tablas in (cursor):
			lista_nombres_tablas=str(lista_tablas)
			lista_nombres_tablas_largo=len(lista_tablas)-4
			lista_nombres_tablas=lista_nombres_tablas[2:lista_nombres_tablas_largo]
			print ("*"+lista_nombres_tablas+"*")
			
			lista_de_tablas.append(lista_nombres_tablas);
		print (lista_de_tablas)
		print("cerramos coneccion");
		cursor.close
		print (input("		continuar?"));
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close
def listar_tablas():
	try:
		nombre_DDBB = "UTN_practica1_2019";
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn",database=str(nombre_DDBB))
		cursor = connection.cursor()
		cursor.execute("SHOW TABLES")
		print ("Mostramos las tablas de la bases de datos "+str(nombre_DDBB))
		lista_de_tablas=[]
		for lista_tablas in (cursor):
			lista_nombres_tablas=str(lista_tablas)
			lista_nombres_tablas_largo=len(lista_tablas)-4
			lista_nombres_tablas=lista_nombres_tablas[2:lista_nombres_tablas_largo]
			print ("*"+lista_nombres_tablas+"*")
			lista_de_tablas.append(lista_nombres_tablas);
		print (lista_de_tablas)
		colunma_numero = int(input("Ingrese el numero de la tabla cuyas columnas desea listar : "));
		cursor.execute("SHOW columns FROM "+str(lista_de_tablas[colunma_numero]))
		for column in cursor.fetchall():
			print (column[colunma_numero]);
		print("cerramos coneccion");
		cursor.close
		print (input("		continuar?"));
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close
################################################            segunda parte del ejercicio
def Iniciar_practica():
	try:
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn")#database='nombre',
		cursor = connection.cursor()
		accion = input ("Drop la DDBB (S/N)")
		if accion.upper() == "S":
			cursor.execute("DROP DATABASE UTN_practica1_2019")
		cursor.execute("CREATE DATABASE UTN_practica1_2019")
		print ("Creamos la base de datos  UTN_practica1_2019")
		cursor.close
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica1_2019")
		cursor = connection.cursor()
		cursor.execute("CREATE TABLE UTN_cuatrimestre (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255), ALUMNO_NOMBRE VARCHAR(255), ALUMNO_MAIL VARCHAR(255), ALUMNO_CELULAR VARCHAR(255), ALUMNO_EDAD INT)")
		cursor.execute("SHOW TABLES")
		print ("Mostramos las tablas de la bases de datos UTN_practica1_2019")
		lista_de_tablas=[]
		for lista_tablas in (cursor):
			lista_nombres_tablas=str(lista_tablas)
			lista_nombres_tablas_largo=len(lista_tablas)-4
			lista_nombres_tablas=lista_nombres_tablas[2:lista_nombres_tablas_largo]
			print ("*"+lista_nombres_tablas+"*")
			lista_de_tablas.append(lista_nombres_tablas);
		print (lista_de_tablas)
		columnas_mysql = "INSERT INTO UTN_cuatrimestre (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD)  VALUES (%s, %s, %s, %s, %s)"
		datos = ("Primer Apellido Segundo Apellido", "Ariel" , "ariel.garcia.traba@gmail.com","+5491144754637","45")
		cursor.execute(columnas_mysql, datos)
		connection.commit()
		print(cursor.rowcount, "record inserted.")
		cursor.close
		print (input("		continuar?"));
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close
def agregar_datos_tabla():
	try:
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica1_2019")
		cursor = connection.cursor()
		cursor.execute("SHOW TABLES")
		print ("Mostramos las tablas de la bases de datos UTN_practica1_2019")
		lista_de_tablas=[]
		for lista_tablas in (cursor):
			lista_nombres_tablas=str(lista_tablas)
			lista_nombres_tablas_largo=len(lista_tablas)-4
			lista_nombres_tablas=lista_nombres_tablas[2:lista_nombres_tablas_largo]
			print ("*"+lista_nombres_tablas+"*")
			lista_de_tablas.append(lista_nombres_tablas);
		print (lista_de_tablas)
		columnas_mysql = "INSERT INTO UTN_cuatrimestre (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD)  VALUES (%s, %s, %s, %s, %s)"
		ALUMNO_APELLIDO = str(input("Ingrese su apellido : "));
		ALUMNO_NOMBRE = str(input("Ingrese su nombre : "));
		ALUMNO_MAIL = str(input("Ingrese su Email : "));
		ALUMNO_CELULAR = str(input("Ingrese su celular : "));
		ALUMNO_EDAD = str(input("Ingrese su edad : "));
		datos = (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD)
		cursor.execute(columnas_mysql, datos)
		connection.commit()
		print(cursor.rowcount, "record inserted.")
		cursor.close
		print (input("		continuar?"));
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close
def listar_datos_tabla():
	try:
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica1_2019")
		cursor = connection.cursor()
		cursor.execute("select ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD from UTN_cuatrimestre")
		for fila in cursor:
			print(fila)
			print("------------------------------\n")
		cursor.close
		print (input("		continuar?"));
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close

def modificar_datos_tabla():
	try:
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica1_2019")
		cursor = connection.cursor()
		cursor.execute("select ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD from UTN_cuatrimestre")
		print("--------Ante de borrar-----------\n")
		for fila in cursor:
			print(fila)
			print("------------------------------\n")
		cursor.execute("update UTN_cuatrimestre set ALUMNO_EDAD=99 where ALUMNO_NOMBRE='Ariel'")
		connection.commit()
		cursor.execute("select ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD from UTN_cuatrimestre")
		print("------Despues de borrar-----------\n")
		for fila in cursor:
			print(fila)
			print("------------------------------\n")
		cursor.close
		print (input("		continuar?"));
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close
def borrar_datos_tabla():
	try:
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica1_2019")
		cursor = connection.cursor()
		cursor.execute("select ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD from UTN_cuatrimestre")
		print("--------Ante de borrar-----------\n")
		for fila in cursor:
			print(fila)
			print("------------------------------\n")
		cursor.execute("delete from UTN_cuatrimestre where ALUMNO_NOMBRE='Ariel'")
		connection.commit()

		cursor.execute("select ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD from UTN_cuatrimestre")
		print("------Despues de borrar-----------\n")
		for fila in cursor:
			print(fila)
			print("------------------------------\n")
		cursor.close
		print (input("		continuar?"));
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		cursor.close	

accion = input ("Borramos base de datos (S/N)"); limpiar();
if accion.upper() =="S": borrar_base();
accion = input ("Creamos base de datos (S/N)"); limpiar();
if accion.upper() =="S": crear_base();
accion= input("Listamos base de datos existentes (S/N)"); limpiar();
if accion.upper() =="S": listar_bases();
accion = input ("Creamos Tablas en la base de datos (S/N)"); limpiar();
if accion.upper() =="S": crear_tablas();
accion= input("Agrego columna ID en tabla (S/N)"); limpiar();
if accion.upper() =="S": agregar_id_tablas();
################################################            segunda parte del ejercicio
print ("segunda parte del ejercicio")
accion= input("Inicio practica alumnos (S/N)"); 
if accion.upper() =="S": Iniciar_practica()
accion= input("Listamos Tablas en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": listar_tablas(); 
accion= input("Agregar dato 1 en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": agregar_datos_tabla(); 
accion= input("Agregar dato 2 en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": agregar_datos_tabla(); 
accion= input("Agregar dato 3 en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": agregar_datos_tabla(); 
accion= input("Agregar dato 4 en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": agregar_datos_tabla(); 
accion= input("Agregar dato 5 en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": agregar_datos_tabla(); 
accion= input("Agregar dato 6 en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": agregar_datos_tabla(); 
accion= input("Listar datos en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": listar_datos_tabla(); 
accion= input("Modificar datos en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": modificar_datos_tabla(); 
accion= input("Borrar datos en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": borrar_datos_tabla(); 








'''
import datetime
import mysql.connector
 
connection = mysql.connector.connect(user='user', password='password', database='database')
cursor =connection.cursor()
 
dni = 10
nombre = 'George'
apellido = 'Lopez'
fecha_nacimiento = datetime.date(1961, 4, 23)
lugar_nacimiento = 'Mission Hills, California, Estados Unidos'
domicilio = 'California'
e_mail = 'george@lopez.com'
 
sql = """
	INSERT INTO alumno
	(
		dni,
		nombre,
		apellido,
		fecha_nacimiento,
		lugar_nacimiento,
		domicilio,
		e-mail
	)
	VALUES (
		%s,
		%s,
		%s,
		%s,
		%s,
		%s,
		%s,
		)
	"""
datos = (dni, nombre, apellido, fecha_nacimiento, lugar_nacimiento, domicilio, e_mail)
cursor.execute(sql, datos)
cursor.commit()
 
cursor.close()
connection.close()
'''
