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

try:
   connection = mysql.connector.connect(host='localhost', database='UTN_practica_2_2019', user='root',password='utn')
#ALUMNO_APELLIDO VARCHAR(255) NOT NULL , ALUMNO_NOMBRE VARCHAR(255) NOT NULL, ALUMNO_MAIL VARCHAR(255), ALUMNO_CELULAR VARCHAR(255), ALUMNO_EDAD INT , ALUMNO_GENERO enum('M','F') , ALUMNO_HOY date, ALUMNO_NACIMIENTO date, ALUMNO_INGRESO date
    mySql_insert_query = """INSERT INTO cuatrimestre_2 (Name, Price, Purchase_date) 
                           VALUES 
                           (1, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """

    cursor =connection.cursor()
	result = cursor.execute(mySql_insert_query)
	connection.commit()
    print("Datos ingresados en la tabla {}".format(error))
    cursor.close()

except mysql.connector.Error as error:
    print("Error en ingresar un dato en la tabla {}".format(error))

finally:
    if (connection.is_connected()):
       connection.close()
        print("Ante un problema MySQLconnection se cierra")

def listar_bases():
	print ("Conectamos con MySQL")
	connection = mysql.connector.connect(host="localhost",user="root", passwd="utn")
	cursor = connection.cursor()
	cursor.execute("SHOW DATABASES")
	lista_de_bases=[]
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (cursor):
		lista_nombres_bases=str(lista_bases)
		lista_nombres_bases_largo=len(lista_bases)-4
		lista_nombres_bases=lista_nombres_bases[2:lista_nombres_bases_largo]
		print ("*"+lista_nombres_bases+"*")
		lista_de_bases.append(lista_nombres_bases);
	print (lista_de_bases)
	print ("cerramos coneccion")
	cursor.close
	return (lista_de_bases)

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
	connection = mysql.connector.connect(host="localhost",user="root", passwd="utn")
	cursor = connection.cursor()
	cursor.execute("SHOW DATABASES")
	lista_de_bases=[]
	
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (cursor):
		nombre_base_MySQL_para_chequear=str(lista_bases)
		nombre_largo=len(lista_bases)-4
		nombre_base_MySQL_para_chequear=nombre_base_MySQL_para_chequear[2:nombre_largo]
#		print ("*"+nombre_base_MySQL_para_chequear+"*", "*"+nombre_base_MySQL_input+"*")
		lista_de_bases.append(nombre_base_MySQL_para_chequear);
	cursor.close
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
