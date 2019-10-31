#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>

def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print("""
############################################################################
##                                                                        ##
##                              Bases de Datos                            ##
##                                                                        ##
##                         libreria mysql.connector                       ##
##                                                                        ##
############################################################################
##                                                                        ##
##                         Create Database                                ##
##                         Create Table                                   ##
##                         Insert                                         ##
##                         Select                                         ##
##                         Where                                          ##
##                         Order By                                       ##
##                         Delete                                         ##
##                         Drop Table                                     ##
##                         Update                                         ##
##                         Limit                                          ##
##                         Join                                           ##
##                                                                        ##
############################################################################
##                                                                        ##
##                MySQL has 3 main categories of data types namely        ##
##                                                                        ##
##                               Numeric,                                 ##
##                               Text                                     ##
##                               Date/time.                               ##
##                                                                        ##
##  Numeric Data types                                                    ##
##  Numeric data types are used to store numeric values. It is very       ##
##    important to make sure range of your data is between lower and upper##
##    boundaries of numeric data types.                                   ##
##               TINYINT( )    -128 to 127 normal 0 to 255                ##
##               SMALLINT( )   -32768 to 32767 normal                     ##
##               MEDIUMINT( )  -8388608 to 8388607 normal                 ##
##               INT( )        -2147483648 to 2147483647 normal           ##
##               BIGINT( )     -9223372036854775808 to                    ##
##                           9223372036854775807 normal                   ##
##               FLOAT         A small approximate number with a floating ##
##                   decimal point.                                       ##
##               DOUBLE( , )   A large number with a floating decimal     ##
##                   point.                                               ##
##               DECIMAL( , )  A DOUBLE stored as a string , allowing     ##
##                   for a fixed decimal point. Choice for storing        ##
##                   currency values.                                     ##
##                                                                        ##
##  Text Data Types                                                       ##
##  As data type category name implies these are used to store text values##
##  Always make sure you length of your textual data do not exceed        ##
##  maximum lengths.                                                      ##
##               CHAR( )       A fixed section from 0 to 255 characters   ##
##               VARCHAR( )    A variable section from 0 to 255 chrs      ##
##               TINYTEXT      A string with a max. length of 255 chrs.   ##
##               TEXT          A string with a max. length of 65535       ##
##               BLOB          A string with a max. length of 65535       ##
##               MEDIUMTEXT    A string with a max. length of 16777215    ##
##               MEDIUMBLOB    A string with a max. length of 16777215    ##
##               LONGTEXT      A string with a max. length of 4294967295  ##
##               LONGBLOB      A string with a max. length of 4294967295  ##
##                                                                        ##
##  Date / Time                                                           ##
##               DATE          YYYY-MM-DD                                 ##
##               DATETIME      YYYY-MM-DD HH:MM:SS                        ##
##               TIMESTAMP     YYYYMMDDHHMMSS                             ##
##               TIME          HH:MM:SS                                   ##
##                                                                        ##
############################################################################
##                                                                        ##
##  Apart from above there are some other data types in MySQL.            ##
##                                                                        ##
##  ENUM     To store text value chosen from a list of predefined text    ##
##           values                                                       ##
##  SET      This is also used for storing text values chosen from a list ##
##           predefined text values. It can have multiple values.         ##
##  BOOL     Synonym for TINYINT(1), used to store Boolean values         ##
##  BINARY   Similar to CHAR, difference is texts are stored in binary    ##
##           format.                                                      ##
##  VARBINARY   Similar to VARCHAR, difference is texts are stored        ##
##              in binary format.                                         ##
##                                                                        ##
############################################################################""");
import mysql.connector

def borrar_base():
	try:
		print ("Conectamos con MySQL")
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn")
		puntero = conectarse.cursor()
		puntero.execute("DROP DATABASE "+str(nombre_DDBB))
		puntero.close
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		puntero.close
def crear_base():

	try:

		print ("Conectamos con MySQL")
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="utn")
		puntero = conectarse.cursor()

		print ("CREATE DATABASE")
		puntero.execute("CREATE DATABASE "+str(nombre_DDBB))
		conectarse.commit()
		puntero = conectarse.cursor()
		print(puntero.rowcount, "record inserted.")
		print ("USE DATABASE")
		puntero.execute("USE "+str(nombre_DDBB))
		puntero = conectarse.cursor()
		print ("CREATE TABLE")
		print ("CREATE COLUMN")
		puntero.execute("CREATE TABLE "+str(nombre_tabla) + "(id INT AUTO_INCREMENT PRIMARY KEY, "+str(nombre_columna_1)+" VARCHAR(255), "+str(nombre_columna_2)+" FLOAT, "+str(nombre_columna_3)+" VARCHAR(255))")
		puntero = conectarse.cursor()
		print ("RECORD INSERT")
		columnas_mysql = "INSERT INTO  "+str(nombre_tabla) + " ("+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+") VALUES(%s,%s,%s)"
#		columnas_mysql = "INSERT INTO 2019_Marzo (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD, ALUMNO_GENERO, ALUMNO_HOY, ALUMNO_NACIMIENTO, ALUMNO_INGRESO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		puntero.execute(columnas_mysql, ("Fideos", 30 , "f1"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("Arroz", 25 , "A1"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("Agua", 20 , "H2O"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("Tomates", 15 , "T1"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("Sal", 10, "S1"))
		conectarse.commit()
		print(puntero.rowcount, "record inserted.")
		print("cerramos coneccion");
		puntero.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		puntero.close
nombre_DDBB = "utn_2do_cuatrimestre"
nombre_tabla = "articulos"
nombre_columna_1 = "descripcion"
nombre_columna_2 = "precio"
nombre_columna_3 = "codigo"
borrar_base();
crear_base();

