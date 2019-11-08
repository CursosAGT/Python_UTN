#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia T <cursos.agt@gmail.com>
from Estructura import *
#################################################################
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                               Trabajo Final Python                          ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                             Python_BBDD_articulos_init                      ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");

import mysql.connector
import datetime
import mysql.connector
hoy = datetime.date.today()
print(hoy)
host_local="localhost"
usuario = "root"
password_de_msql="utn"
nombre_DDBB = "Supermercado"
nombre_tabla = "articulos"
nombre_columna_1 = "descripcion"
nombre_columna_2 = "precio"
nombre_columna_3 = "codigo"
nombre_columna_4 = "stock"
nombre_columna_5 = "Vencimiento"

def borrar_base():
	try:
		connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql )
		print ("Conectamos con MySQL 	connection = ",connection)
		cursor = connection.cursor()
		cursor.execute("DROP DATABASE IF EXISTS "+str(nombre_DDBB))
		cursor.close
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		print("finally")
def crear_base():
	try:
		print ("Conectamos con MySQL")
		connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql )
		cursor = connection.cursor()

		print ("CREATE DATABASE")
		cursor.execute("CREATE DATABASE "+str(nombre_DDBB))
		connection.commit()
		cursor = connection.cursor()
		print(cursor.rowcount, "record inserted.")
		print ("USE DATABASE")
		cursor.execute("USE "+str(nombre_DDBB))
		cursor = connection.cursor()
		print ("CREATE TABLE")
		print ("CREATE COLUMN")
		cursor.execute("CREATE TABLE "+str(nombre_tabla) + "(id INT AUTO_INCREMENT PRIMARY KEY, "+str(nombre_columna_1)+" VARCHAR(255), "+str(nombre_columna_2)+" FLOAT, "+str(nombre_columna_3)+" VARCHAR(255),  "+str(nombre_columna_4)+"  INT,  "+str(nombre_columna_5)+"  date )")
		cursor = connection.cursor()
		print ("RECORD INSERT")
		columnas_mysql = "INSERT INTO  "+str(nombre_tabla) + " ("+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+", "+str(nombre_columna_4)+", "+str(nombre_columna_5)+") VALUES(%s,%s,%s,%s,%s)"
		cursor.execute(columnas_mysql, ("Fideos", 30 , "f1",8,hoy))
		connection.commit()
		cursor.execute(columnas_mysql, ("Arroz", 25 , "A1",78,hoy))
		connection.commit()
		cursor.execute(columnas_mysql, ("Agua", 20 , "H2O",81,hoy))
		connection.commit()
		cursor.execute(columnas_mysql, ("Tomates", 15 , "T1",28,hoy))
		connection.commit()
		cursor.execute(columnas_mysql, ("Sal", 10, "S1",18,hoy))
		connection.commit()
		print(cursor.rowcount, "record inserted.")
		print("cerramos coneccion");
		cursor.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		#cursor.close
		pass
borrar_base();
crear_base();
