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

https://www.w3schools.com/python/python_mysql_create_db.asp
https://www.w3schools.com/python/python_mysql_create_table.asp
https://www.w3schools.com/python/python_mysql_insert.asp
https://www.w3schools.com/python/python_mysql_select.asp
https://www.w3schools.com/python/python_mysql_where.asp
https://www.w3schools.com/python/python_mysql_orderby.asp
https://www.w3schools.com/python/python_mysql_delete.asp
https://www.w3schools.com/python/python_mysql_drop_table.asp
https://www.w3schools.com/python/python_mysql_update.asp
https://www.w3schools.com/python/python_mysql_limit.asp
https://www.w3schools.com/python/python_mysql_join.asp
https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
https://www.guru99.com/how-to-create-a-database.html
http://www.mysqltutorial.org/mysql-datetime/
""")
limpiar();
#################################################################
#Clase_BBDD_01 
import mysql.connector
import datetime
#from datetime import date
#from datetime import datetime
def Iniciar_practica():
#	try:
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn")
	puntero = conectarse.cursor()
	accion = input ("Drop la DDBB (S/N)")
	if accion.upper() == "S":
		print ("Borramos la base de datos  UTN_practica_2_2019")
		puntero.execute("DROP DATABASE UTN_practica_2_2019")
	puntero.execute("CREATE DATABASE UTN_practica_2_2019")
	print ("Creamos la base de datos  UTN_practica_2_2019")
	puntero.close
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
	puntero = conectarse.cursor()
	puntero.execute("CREATE TABLE 2017_Marzo (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL)")
	puntero.execute("CREATE TABLE 2018_Marzo (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL)")	
	puntero.execute("CREATE TABLE UTN_cuatrimestre (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL , ALUMNO_NOMBRE VARCHAR(255) NOT NULL, ALUMNO_MAIL VARCHAR(255), ALUMNO_CELULAR VARCHAR(255), ALUMNO_EDAD INT , ALUMNO_GENERO enum('M','F') , ALUMNO_HOY date, ALUMNO_NACIMIENTO date, ALUMNO_INGRESO date )")
	columnas_mysql = "INSERT INTO UTN_cuatrimestre (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_HOY, ALUMNO_NACIMIENTO, ALUMNO_INGRESO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

	nacimiento = datetime.datetime(1973,9,22)
	hoy = datetime.datetime.now()
	ingreso = datetime.datetime(2015,3,1)
	puntero.execute(columnas_mysql, ("Garcia traba", "Ariel" , "cursos.agt@gmail.com","+5491144754637","46","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Primer Apellido 2", "Nombre 2" , "zzzzz@yahoo.com","+5491100000000","88","F",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Primer Apellido 3", "Nombre 3" , "xxxxx@hotgmail.com","+5491101234567","77","F",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Primer Apellido 4", "Nombre 4" , "yyyyy@gmail.com","+549110987654321","66","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Primer Apellido 5", "Nombre 5" , "wwwww2@gmail.com","+5491100000000","55","F",hoy,nacimiento,ingreso))
	conectarse.commit()

	print(puntero.rowcount, "record inserted.")
	puntero.close
def Recargar_practica():
	print ("Recargar_practica Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
	puntero = conectarse.cursor()
	columnas_mysql = "INSERT INTO UTN_cuatrimestre (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_HOY, ALUMNO_NACIMIENTO, ALUMNO_INGRESO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	nacimiento = datetime.datetime(1973,9,22)
	hoy = datetime.datetime.now()
	ingreso = datetime.datetime(2015,3,1)
	puntero.execute(columnas_mysql, ("Garcia traba", "Ariel" , "cursos.agt@gmail.com","+5491144754637","46","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Primer Apellido 2", "Nombre 2" , "zzzzz@yahoo.com","+5491100000000","88","F",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Primer Apellido 3", "Nombre 3" , "xxxxx@hotgmail.com","+5491101234567","77","F",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Primer Apellido 4", "Nombre 4" , "yyyyy@gmail.com","+549110987654321","66","M",hoy,nacimiento,ingreso))
	conectarse.commit()
	puntero.execute(columnas_mysql, ("Primer Apellido 5", "Nombre 5" , "wwwww2@gmail.com","+5491100000000","55","F",hoy,nacimiento,ingreso))
	conectarse.commit()
	print(puntero.rowcount, "record inserted.")
	puntero.close

Iniciar_practica()
print(input("continuo????"))
limpiar();
print (input("\n\n  1_1) SELECIONO Y MUESTRO TODO LO QUE TENGA LA TABLA ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
print ('puntero.execute("SELECT * FROM UTN_cuatrimestre")');
puntero.execute("SELECT * FROM UTN_cuatrimestre")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
print (input("\n\n  1_2) MUESTRO POR FILAS LAS COLUMNAS SELECCIONADAS TODO LO QUE TENGA LA TABLA ?"));
puntero.execute("select ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_INGRESO from UTN_cuatrimestre")
print("ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_INGRESO")
for fila in puntero:
	print(fila)
	print("------------------------------\n")
puntero.close
print (input("\n\n  2) SELECIONO POR COLUMNA ALUMNO_NOMBRE, ALUMNO_MAIL FROM UTN_cuatrimestre ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
puntero.execute("SELECT ALUMNO_NOMBRE, ALUMNO_MAIL FROM UTN_cuatrimestre")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  3)SELECCIONO CON FILTROS `WHERE` ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
sql = "SELECT * FROM UTN_cuatrimestre WHERE ALUMNO_MAIL ='ariel.Primer Apellido.Segundo Apellido@gmail.com'"
puntero.execute(sql)
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
print(input("continuo????"))
limpiar();
print (input("\n\n  4 ) * FILTRO CON CARACTERES % wildcard '%LIKE%' ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
sql = "SELECT * FROM UTN_cuatrimestre WHERE ALUMNO_MAIL LIKE '%Primer Apellido%'"
puntero.execute(sql)
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec) 
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  5 ) FILTRO CON CARACTERES %s wildcard  SQL Injection ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
sql = "SELECT * FROM UTN_cuatrimestre WHERE ALUMNO_MAIL = %s"
adr = ("ariel.Primer Apellido.Segundo Apellido@gmail.com", )
puntero.execute(sql, adr)
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec) 
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  6 ) SORT ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
sql = "SELECT * FROM UTN_cuatrimestre ORDER BY ALUMNO_NOMBRE"
puntero.execute(sql)
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  7 ) SORT INVERTIDO ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
sql = "SELECT * FROM UTN_cuatrimestre ORDER BY ALUMNO_NOMBRE DESC"
puntero.execute(sql)
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  8 ) BORRO UN RECORD ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()

puntero.execute("SELECT * FROM UTN_cuatrimestre")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
puntero.close

sql = "DELETE FROM UTN_cuatrimestre WHERE ALUMNO_MAIL = 'ariel.Primer Apellido.Segundo Apellido@gmail.com'"
puntero.execute(sql)
print ("borro - "+ str(sql));
conectarse.commit()
print(puntero.rowcount, "record(s) deleted")

puntero.execute("SELECT * FROM UTN_cuatrimestre")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  9 ) BORRO UN RECORD - Prevent SQL Injection ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()

puntero.execute("SELECT * FROM UTN_cuatrimestre")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)

sql = "DELETE FROM UTN_cuatrimestre WHERE ALUMNO_NOMBRE = %s"
adr = ("Segundo Nombre", )
print ("borro - "+ str(sql) + str(adr) );
puntero.execute(sql, adr)
conectarse.commit()
print(puntero.rowcount, "record(s) deleted")

puntero.execute("SELECT * FROM UTN_cuatrimestre")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  10 ) ACTUALIZAR UN DATO 'UPDATE' ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()

puntero.execute("SELECT * FROM UTN_cuatrimestre WHERE ALUMNO_MAIL LIKE '%Primer Apellido%'")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec) 

sql = "UPDATE UTN_cuatrimestre SET ALUMNO_MAIL = 'ariel.Primer Apellido.Segundo Apellido@ariel.Primer Apellido.Segundo Apellido@hotmail.com.com' WHERE ALUMNO_MAIL = 'ariel.Primer Apellido.Segundo Apellido@hotmail.com'"
puntero.execute(sql)
conectarse.commit()
print(puntero.rowcount, "record(s) affected")

puntero.execute("SELECT * FROM UTN_cuatrimestre WHERE ALUMNO_MAIL LIKE '%Primer Apellido%'")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec) 
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  11 ) ACTUALIZAR CON %s SQL Injection 'UPDATE' ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()

puntero.execute("SELECT * FROM UTN_cuatrimestre WHERE ALUMNO_MAIL LIKE '%Primer Apellido%'")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)

sql = "UPDATE UTN_cuatrimestre SET ALUMNO_MAIL = %s WHERE ALUMNO_MAIL = %s"
val = ("ariel.Primer Apellido.Segundo Apellido@hotmail.com", "ariel.Primer Apellido.Segundo Apellido@Gmail.com")
puntero.execute(sql, val)
conectarse.commit()
print(puntero.rowcount, "record(s) affected")

puntero.execute("SELECT * FROM UTN_cuatrimestre WHERE ALUMNO_MAIL LIKE '%Primer Apellido%'")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  12 ) LIMITO LA CANTIDAD DE RESULTADOS 'LIMIT' ?"));
print ("You can limit the number of records returned from the query, by using the 'LIMIT' statement:");
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
puntero.execute("SELECT * FROM UTN_cuatrimestre LIMIT 5")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec) 
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  13 ) INICIO DESDE OTRA POSICION OFFSET ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()
puntero.execute("SELECT * FROM UTN_cuatrimestre LIMIT 5 OFFSET 2")
resultados = puntero.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()  
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  14 ) BORRO UNA TABLA 'Drop' ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")

print ("------------Estado Inicial-------------")
puntero = conectarse.cursor()
puntero.execute("SHOW TABLES")
for cada_rec in puntero:
	print(cada_rec)
print ("------------DROP-----------------------")

puntero = conectarse.cursor()
sql = "DROP TABLE UTN_cuatrimestre"
puntero.execute(sql) 

print ("------------Estado Final---------------")
puntero = conectarse.cursor()
puntero.execute("SHOW TABLES")
for cada_rec in puntero:
	print(cada_rec)

Iniciar_practica()
puntero.close
print(input("continuo????"))
limpiar();
print (input("\n\n  15 ) BORRO UNA TABLA 'Drop' SI EXISTE ?"));
conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn", database="UTN_practica_2_2019")
puntero = conectarse.cursor()

print ("------------Estado Inicial-------------")
puntero = conectarse.cursor()
puntero.execute("SHOW TABLES")
for cada_rec in puntero:
	print(cada_rec)
print ("------------DROP-----------------------")

puntero = conectarse.cursor()
sql = "DROP TABLE IF EXISTS 2020_Marzo"
print( "Tabla a borrar"+str(sql))
puntero.execute(sql) 

print ("------------Estado Final---------------")
puntero = conectarse.cursor()
puntero.execute("SHOW TABLES")
for cada_rec in puntero:
	print(cada_rec)
puntero = conectarse.cursor()
sql = "DROP TABLE IF EXISTS UTN_cuatrimestre"
print( "Tabla a borrar"+str(sql))
puntero.execute(sql) 

print ("------------Estado Final---------------")
puntero = conectarse.cursor()
puntero.execute("SHOW TABLES")
for cada_rec in puntero:
	print(cada_rec)
	
Iniciar_practica()
puntero.close
