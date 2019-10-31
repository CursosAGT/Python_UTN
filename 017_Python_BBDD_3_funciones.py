from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
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
def Iniciar_practica():
	print ("Iniciamos")
	print ("Conectamos con MySQL")
	connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql)
	cursor = connection.cursor()
	print ("para iniciar el ejercicio si exista la base borrarla, sino crearla")
	try:
		print (f"Borramos la base de datos  {nombre_DDBB}")
		cursor.execute("DROP DATABASE "+str(nombre_DDBB))
	except Exception as error_borrado_base:
		print("Exeception occured:{}".format(error_borrado_base))
	finally:

		print (f"Creamos la base de datos  {nombre_DDBB}")
		cursor.execute("CREATE DATABASE "+str(nombre_DDBB))
		cursor.close
		connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql, database= nombre_DDBB )
		cursor = connection.cursor()
		cursor.execute("CREATE TABLE backup (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL)")
		cursor.execute("CREATE TABLE viejo (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL)")
		cursor.execute("CREATE TABLE "+str(nombre_tabla)+" (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255) NOT NULL , ALUMNO_NOMBRE VARCHAR(255) NOT NULL, ALUMNO_MAIL VARCHAR(255), ALUMNO_CELULAR VARCHAR(255), ALUMNO_EDAD INT , ALUMNO_GENERO enum('M','F') , ALUMNO_HOY date, ALUMNO_NACIMIENTO date, ALUMNO_INGRESO date )")
		columnas_mysql = "INSERT INTO "+str(nombre_tabla)+" (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_HOY, ALUMNO_NACIMIENTO, ALUMNO_INGRESO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		print("""
		cargo:
		Garcia Traba", "Ariel" , "cursos.agt@gmail.com","+5491144754637","46","M",hoy,nacimiento,ingreso))
		Primer Apellido 2", "Nombre_2" , "zzzzz@yahoo.com","+5491100000000","88","F",hoy,nacimiento,ingreso))
		Primer Apellido 3", "Nombre_3" , "xxxxx@hotgmail.com","+5491101234567","77","F",hoy,nacimiento,ingreso))
		Primer Apellido 4", "Nombre_4" , "yyyyy@gmail.com","+549110987654321","66","M",hoy,nacimiento,ingreso))
		Primer Apellido 5", "Nombre_5" , "wwwww2@gmail.com","+5491100000000","55","F",hoy,nacimiento,ingreso))
		""")



		nacimiento = datetime.datetime(1973,9,22)
		hoy = datetime.date.today()
		ingreso = datetime.datetime(2015,3,1)
		cursor.execute(columnas_mysql, ("Garcia Traba", "Ariel" , "cursos.agt@gmail.com","+5491144754637","46","M",hoy,nacimiento,ingreso))
		connection.commit()
		cursor.execute(columnas_mysql, ("Primer Apellido 2", "Nombre_2" , "zzzzz@yahoo.com","+5491100000000","88","F",hoy,nacimiento,ingreso))
		connection.commit()
		cursor.execute(columnas_mysql, ("Primer Apellido 3", "Nombre_3" , "xxxxx@hotgmail.com","+5491101234567","77","F",hoy,nacimiento,ingreso))
		connection.commit()
		cursor.execute(columnas_mysql, ("Primer Apellido 4", "Nombre_4" , "yyyyy@gmail.com","+549110987654321","66","M",hoy,nacimiento,ingreso))
		connection.commit()
		cursor.execute(columnas_mysql, ("Primer Apellido 5", "Nombre_5" , "wwwww2@gmail.com","+5491100000000","55","F",hoy,nacimiento,ingreso))
		connection.commit()
		propio = input("inicio carga de datos propios s/n ")
		if propio.upper()=="S":
			Apell=input("su Apellido :")
			Nombre=input("su Nombre :")
			email=input("su Email :")
			celular=input("su Celular :")
			edad=int(input("Su edad :"))
			sexo=input("su Sexo (F/M)")
			hoy = datetime.datetime.today()
			nac_d=int(input("su Fecha de nacimiento - Dia (dd)"))
			nac_m=int(input("su Fecha de nacimiento - Mes (mm)"))
			nac_a=int(input("su Fecha de nacimiento - Año (aaaa)"))
			fnacimiento = datetime.datetime(nac_a,nac_m,nac_d)
			ing_d=int(input("su Fecha de ingreso a utn - Dia (dd)"))
			ing_m=int(input("su Fecha de ingreso a utn - Mes (mm)"))
			ing_a=int(input("su Fecha de ingreso a utn - Año (aaaa)"))
			fingreso = datetime.datetime(ing_a,ing_m,ing_d)
			cursor.execute(columnas_mysql, (Apell, Nombre , email,celular,edad,sexo,hoy,fnacimiento,fingreso))
			connection.commit()
		print(cursor.rowcount, "record inserted.")
		cursor.close
def Recargar_practica():
	print ("Recargar_practica Conectamos con MySQL")
	connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
	cursor = connection.cursor()
	columnas_mysql = "INSERT INTO "+str(nombre_tabla)+" (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_HOY, ALUMNO_NACIMIENTO, ALUMNO_INGRESO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	nacimiento = datetime.datetime(1973,9,22)
	hoy = datetime.datetime.now()
	ingreso = datetime.datetime(2015,3,1)
	cursor.execute(columnas_mysql, ("Garcia traba", "Ariel" , "cursos.agt@gmail.com","+5491144754637","46","M",hoy,nacimiento,ingreso))
	connection.commit()
	cursor.execute(columnas_mysql, ("Primer Apellido 2", "Nombre_2" , "zzzzz@yahoo.com","+5491100000000","88","F",hoy,nacimiento,ingreso))
	connection.commit()
	cursor.execute(columnas_mysql, ("Primer Apellido 3", "Nombre_3" , "xxxxx@hotgmail.com","+5491101234567","77","F",hoy,nacimiento,ingreso))
	connection.commit()
	cursor.execute(columnas_mysql, ("Primer Apellido 4", "Nombre_4" , "yyyyy@gmail.com","+549110987654321","66","M",hoy,nacimiento,ingreso))
	connection.commit()
	cursor.execute(columnas_mysql, ("Primer Apellido 5", "Nombre_5" , "wwwww2@gmail.com","+5491100000000","55","F",hoy,nacimiento,ingreso))
	connection.commit()
	print(cursor.rowcount, "record inserted.")
	cursor.close
##########################################################################################################################
nombre_DDBB = "utn_2do_cuatrimestre"
nombre_tabla = "alumnos"
hoy = datetime.date.today()
print(hoy)
usuario = "root"
password_de_msql="utn"
host_local="localhost"
coneccion = str("mysql.connector.connect(host= '"+str(host_local)+"' ,user= '"+str(usuario)+"' , passwd= '"+str(password_de_msql)+"', database= '"+str(nombre_DDBB)+"' )")
print(coneccion)
Iniciar_practica()
pausa()
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  1_1) SELECIONO Y MUESTRO TODO LO QUE TENGA LA TABLA ");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()
print ('cursor.execute("SELECT * from "+str(nombre_tabla))');
cursor.execute("SELECT * from "+str(nombre_tabla))
resultados = cursor.fetchall()
print("SELECT * from "+str(nombre_tabla))
for cada_rec in resultados:
	print(cada_rec)
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  1_2) MUESTRO POR FILAS LAS COLUMNAS SELECCIONADAS TODO LO QUE TENGA LA TABLA ?");
cursor.execute("select ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_INGRESO from "+str(nombre_tabla))
print("ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_INGRESO")
for fila in cursor:
	print(fila)
	print("------------------------------\n")
cursor.close
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  2) SELECIONO POR COLUMNA ALUMNO_NOMBRE, ALUMNO_MAIL FROM "+str(nombre_tabla));
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()
print("""
Para leer los resultados de la consulta
<cursor.execute('select * from una_tabla')>
<resultados = cursor.fetchall()>
luego lo debemos llamar al método fetchone() , fetchall() o fetchmany() de cursor.
fetchone devuelve una de las filas de resultados y en sucesivas llamadas nos irá devolviendo el resto (none al final)
fetchall devuelve todas las filas juntas.
fetchmany(cant_filas) devuelve de a cant_filas de juntas.
<
while True:
	rows = cursor.fetchmany(50)
	if not rows:
		break
	for row in rows:
		yield row
>
""")
cursor.execute("SELECT ALUMNO_NOMBRE, ALUMNO_MAIL from "+str(nombre_tabla))
resultados = cursor.fetchall()
for cada_rec in resultados:
	print(cada_rec)
cursor.close
pausa()
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  3)SELECCIONO CON FILTROS `WHERE` ");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()
print(""" devuelve todo si corresponde a WHERE ALUMNO_MAIL ='cursos.agt@gmail.com'""")
string_de_busqueda = "SELECT * FROM "+str(nombre_tabla)+"  WHERE ALUMNO_MAIL ='cursos.agt@gmail.com'"
cursor.execute(string_de_busqueda)
resultados = cursor.fetchall()
print("Datos encontrados con Where")
for cada_rec in resultados:
	print(cada_rec)
pausa()
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  4 ) FILTRO CON CARACTERES % wildcard '%LIKE%' ");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()
string_de_busqueda = "SELECT * FROM "+str(nombre_tabla)+"  WHERE ALUMNO_MAIL LIKE '%zzzzz%'"
cursor.execute(string_de_busqueda)
resultados = cursor.fetchall()
print("Datos encontrados con like")
for cada_rec in resultados:
	print(cada_rec)
cursor.close

limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  5 ) FILTRO CON CARACTERES %s wildcard  SQL Injection ");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()
string_de_busqueda = "SELECT * FROM "+str(nombre_tabla)+"  WHERE ALUMNO_MAIL = %s"
dato_buscado = ("cursos.agt@gmail.com", )
cursor.execute(string_de_busqueda, dato_buscado)
resultados = cursor.fetchall()
for cada_rec in resultados:
	print(cada_rec)
cursor.close
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  6 ) SORT ");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()
string_de_busqueda = "SELECT * FROM "+str(nombre_tabla)+"  ORDER BY ALUMNO_NOMBRE"
cursor.execute(string_de_busqueda)
resultados = cursor.fetchall()
for cada_rec in resultados:
	print(cada_rec)
cursor.close
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  7 ) SORT INVERTIDO ");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()
string_de_busqueda = "SELECT * FROM "+str(nombre_tabla)+"  ORDER BY ALUMNO_NOMBRE DESC"
cursor.execute(string_de_busqueda)
resultados = cursor.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
cursor.close
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  8 ) BORRO UN RECORD ");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()

cursor.execute("SELECT * from "+str(nombre_tabla))
resultados = cursor.fetchall()
print ("\n\n  Listado original ");
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
cursor.close
pausa()
string_de_busqueda = "DELETE FROM "+str(nombre_tabla)+"  WHERE ALUMNO_Nombre = 'Nombre_4'"
cursor.execute(string_de_busqueda)
print ("borro - "+ str(string_de_busqueda));
connection.commit()
print(cursor.rowcount, "record(s) deleted")

cursor.execute("SELECT * from "+str(nombre_tabla))
resultados = cursor.fetchall()
print ("\n\n  Listado con un dato borrado Nombre_4");
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
cursor.close
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  9 ) BORRO UN RECORD - Prevent SQL Injection ");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()

cursor.execute("SELECT * from "+str(nombre_tabla))
resultados = cursor.fetchall()
print ("\n\n  Listado original ");
for cada_rec in resultados:
	print(cada_rec)

string_de_busqueda = "DELETE FROM "+str(nombre_tabla)+"  WHERE ALUMNO_NOMBRE = %s"
dato_buscado = ("Nombre_3", )
print ("borro - "+ str(string_de_busqueda) + str(dato_buscado) );
cursor.execute(string_de_busqueda, dato_buscado)
connection.commit()
print(cursor.rowcount, "record(s) deleted")

cursor.execute("SELECT * from "+str(nombre_tabla))
resultados = cursor.fetchall()
print ("\n\n  Listado con un dato borrado Nombre_3");
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
cursor.close
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  10 ) ACTUALIZAR UN DATO 'UPDATE'");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()

cursor.execute("SELECT * FROM "+str(nombre_tabla)+"  WHERE ALUMNO_NOMBRE LIKE '%Nombre_%'")
print ("\n\n  Listado original detodos los 'Nombres_' ");
resultados = cursor.fetchall()
for cada_rec in resultados:
	print(cada_rec)

string_de_busqueda = "UPDATE "+str(nombre_tabla)+"  SET ALUMNO_MAIL = 'zzzzz@yahoo.com' WHERE ALUMNO_MAIL = 'yyyyy@gmail.com' "
cursor.execute(string_de_busqueda)
connection.commit()
print(cursor.rowcount, "record(s) affected")

cursor.execute("SELECT * FROM "+str(nombre_tabla)+"  WHERE ALUMNO_MAIL LIKE '%yyyyy%'")
resultados = cursor.fetchall()
print ("\n\n  Listado modificado ");
for cada_rec in resultados:
	print(cada_rec)
cursor.close
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  11 ) ACTUALIZAR CON %s SQL Injection 'UPDATE' ?");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()

cursor.execute("SELECT * FROM "+str(nombre_tabla)+"  WHERE ALUMNO_MAIL LIKE '%zzzzz%'")
resultados = cursor.fetchall()
print("SELECT * FROM "+str(nombre_tabla)+"  WHERE ALUMNO_MAIL LIKE '%zzzzz%'")

for cada_rec in resultados:
	print("se reemplaza el sig resultado de LIKE '%zzzzz%':", cada_rec)
pausa()
string_de_busqueda = "UPDATE "+str(nombre_tabla)+"  SET ALUMNO_MAIL = %s WHERE ALUMNO_MAIL = %s"
print("Busco 'cursos.mithril@gmail.com' y reemplazo con 'zzzzz@yahoo.com' ")
dato_buscado = ("cursos.mithril@gmail.com", "zzzzz@yahoo.com")
cursor.execute(string_de_busqueda, dato_buscado)
connection.commit()
pausa()
print(cursor.rowcount, "record(s) affected")
cursor.execute("SELECT * FROM "+str(nombre_tabla)+"  WHERE ALUMNO_MAIL LIKE '%@%'")
resultados = cursor.fetchall()
print("SELECT * FROM "+str(nombre_tabla)+"  WHERE ALUMNO_MAIL LIKE '%@%'")
for cada_rec in resultados:
	print(cada_rec)
cursor.close
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  12 ) LIMITO LA CANTIDAD DE RESULTADOS 'LIMIT' ");
print ("You can limit the number of records returned from the query, by using the 'LIMIT' statement:");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()
cursor.execute("SELECT * FROM "+str(nombre_tabla)+"  LIMIT 5")
resultados = cursor.fetchall()
for cada_rec in resultados:
	print(cada_rec)
cursor.close
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  13 ) INICIO DESDE OTRA POSICION OFFSET ");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()
cursor.execute("SELECT * FROM "+str(nombre_tabla)+"  LIMIT 5 OFFSET 2")
resultados = cursor.fetchall()
for cada_rec in resultados:
	print(cada_rec)
Recargar_practica()
cursor.close
pausa()
limpiar();
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n\n  14 ) BORRO UNA TABLA 'Drop' ");
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)

print ("------------Estado Inicial-------------")
cursor = connection.cursor()
cursor.execute("SHOW TABLES")
for cada_rec in cursor:
	print(cada_rec)
print ("------------DROP-----------------------")

cursor = connection.cursor()
string_de_busqueda = "DROP TABLE "+str(nombre_tabla)
cursor.execute(string_de_busqueda)

print ("------------Estado Final---------------")
cursor = connection.cursor()
cursor.execute("SHOW TABLES")
for cada_rec in cursor:
	print(cada_rec)

Iniciar_practica()
cursor.close
pausa()
limpiar();
print (input("\n\n  15 ) BORRO UNA TABLA '2020_Marzo' (Drop) SI EXISTE "));
connection = mysql.connector.connect(host= host_local,user= usuario, passwd= password_de_msql, database=nombre_DDBB)
cursor = connection.cursor()

print ("------------Estado Inicial-------------")
cursor = connection.cursor()
cursor.execute("SHOW TABLES")
for cada_rec in cursor:
	print(cada_rec)
print ("------------DROP-----------------------")

cursor = connection.cursor()
string_de_busqueda = "DROP TABLE IF EXISTS 2020_Marzo"
print( "Tabla a borrar"+str(string_de_busqueda))
cursor.execute(string_de_busqueda)

print ("------------Estado Final---------------")
cursor = connection.cursor()
cursor.execute("SHOW TABLES")
for cada_rec in cursor:
	print(cada_rec)
cursor = connection.cursor()
string_de_busqueda = "DROP TABLE IF EXISTS "+str(nombre_tabla)
print( "Tabla a borrar"+str(string_de_busqueda))
cursor.execute(string_de_busqueda)

print ("------------Estado Final---------------")
cursor = connection.cursor()
cursor.execute("SHOW TABLES")
for cada_rec in cursor:
	print(cada_rec)

Iniciar_practica()
cursor.close
