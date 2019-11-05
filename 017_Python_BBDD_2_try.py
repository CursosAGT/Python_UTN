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
#################################################################
#Clase_BBDD_01
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime

hoy = datetime.date.today()
print(hoy)
host_local="localhost"
usuario = "root"
password_de_msql="utn"
nombre_DDBB = "utn2doCuatrimestre"
nombre_tabla = "alumnos"

try:
	print ("Iniciamos")
	print ("Conectamos con MySQL")
	connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql, database= nombre_DDBB )
	cursor = connection.cursor()
	datos_mysql = "INSERT INTO "+str(nombre_tabla)+" (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_HOY, ALUMNO_NACIMIENTO, ALUMNO_INGRESO) VALUES('Garcia Traba', 'Ariel' , 'cursos.agt@gmail.com','+5491144754637','46','M','2020-01-01','1973-09-22','2010-08-14') "
	cursor =connection.cursor()
	result = cursor.execute(datos_mysql)
	connection.commit()
	print(f"Datos ingresados en la tabla ")
	cursor.close()

except mysql.connector.Error as error:
	print("Error en ingresar un dato en la tabla {}".format(error))
	print ("Conectamos con MySQL")
	connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql)
	cursor = connection.cursor()
	print ("Conectamos con MySQL")
	cursor.execute("CREATE DATABASE "+str(nombre_DDBB))
	cursor.close
	connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql, database= nombre_DDBB )
	cursor = connection.cursor()
	print("CREATE TABLE backup (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL)------------------una tabla vaciá para guardad la copia de seguridad de lo que valla a cambiar")
	cursor.execute("CREATE TABLE backup (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL)")
	print("CREATE TABLE viejo (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL)------------------una tabla vaciá para guardad las cosas viejas")
	cursor.execute("CREATE TABLE viejo (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL)")
	print("CREATE TABLE "+str(nombre_tabla)+" (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL , ALUMNO_NOMBRE VARCHAR(255) NOT NULL, ALUMNO_MAIL VARCHAR(255), ALUMNO_CELULAR VARCHAR(255), ALUMNO_EDAD INT , ALUMNO_GENERO enum('M','F') , ALUMNO_HOY date, ALUMNO_NACIMIENTO date, ALUMNO_INGRESO date )")
	cursor.execute("CREATE TABLE "+str(nombre_tabla)+" (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL , ALUMNO_NOMBRE VARCHAR(255) NOT NULL, ALUMNO_MAIL VARCHAR(255), ALUMNO_CELULAR VARCHAR(255), ALUMNO_EDAD INT , ALUMNO_GENERO enum('M','F') , ALUMNO_HOY date, ALUMNO_NACIMIENTO date, ALUMNO_INGRESO date )")
	print("INSERT INTO "+str(nombre_tabla)+" (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_HOY, ALUMNO_NACIMIENTO, ALUMNO_INGRESO) VALUES('Garcia Traba', 'Ariel' , 'cursos.agt@gmail.com','+5491144754637','46','M','2020-01-01','1973-09-22','2010-08-14') ")
	datos_mysql = "INSERT INTO "+str(nombre_tabla)+" (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_HOY, ALUMNO_NACIMIENTO, ALUMNO_INGRESO) VALUES('Garcia Traba', 'Ariel' , 'cursos.agt@gmail.com','+5491144754637','46','M','2020-01-01','1973-09-22','2010-08-14') "
	cursor =connection.cursor()
	result = cursor.execute(datos_mysql)
	connection.commit()
	cursor.close
finally:
	if (connection.is_connected()):
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print ("SELECCIONO Y MUESTRO TODO LO QUE TENGA LA TABLA ");
		connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
		cursor = connection.cursor()
		print ('cursor.execute("SELECT * from "+str(nombre_tabla))');
		cursor.execute("SELECT * from "+str(nombre_tabla))
		resultados = cursor.fetchall()
		print("SELECT * from "+str(nombre_tabla))
		for cada_rec in resultados:
			print(cada_rec)
		connection.close()
		print("Ante un problema MySQLconnection se cierra")
