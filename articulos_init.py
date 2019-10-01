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
print("############################################################################");
print("##                                                                        ##");
print("##      Unidad 1 -¿Qué es Python?                                         ##");
print("##            * Instalación y configuración                               ##");
print("##            * Errores sintácticos y lógicos                             ##");
print("##            * Programación secuencial                                   ##");
print("##            * Estructuras condicionales simples, compuestas y anidadas  ##");
print("##            * Estructuras repetitivas                                   ##");
print("##                                                                        ##");
print("##      Unidad 2 - Variables, Listas                                      ##");
print("##            * Tipos de variables                                        ##");
print("##            * Procesamiento de cadenas                                  ##");
print("##            * Listas                                                    ##");
print("##            * Diccionarios                                              ##");
print("##                                                                        ##");
print("##      Unidad 3 - Funciones                                              ##");
print("##            * Parámetros                                                ##");
print("##            * Retorno de datos                                          ##");
print("##            * Return de listas                                          ##");
print("##            * Parámetros con valor por defecto                          ##");
print("##                                                                        ##");
print("##      Unidad 4 - Listas, Tuplas y Diccionarios                          ##");
print("##         Listas                                                         ##");
print("##            * Índices                                                   ##");
print("##            * Recorrer listas                                           ##");
print("##         Tuplas                                                         ##");
print("##            * Índices                                                   ##");
print("##            * Recorrer Tuplas                                           ##");
print("##         Diccionarios                                                   ##");
print("##            * Funcionamiento de diccionarios                            ##");
print("##            * Estructuras tipo JSON                                     ##");
print("##                                                                        ##");
print("##         Unidad 5 - MySQL, Parte 1                                      ##");
print("##            * INSERT, UPDATE, DELETE, SELECT                            ##");
print("##            * FECHAS Y HORAS                                            ##");
print("##            * %LIKE%                                                    ##");
print("##            * JOIN                                                      ##");
print("##                                                                        ##");
print("##         Unidad 6 - MySQL, Parte 2                                      ##");
print("##            * MySQL en Python                                           ##");
print("##            * puntero y verificación de consultas                        ##");
print("##            * Manejo de errores                                         ##");
print("##                                                                        ##");
print("##         Unidad 7 - Fechas, Horas, Archivos                             ##");
print("##            * Modulo time, datetime                                     ##");
print("##            * Manejo de fechas y horas                                  ##");
print("##            * Operaciones con archivos                                  ##");
print("##                                                                        ##");
print("##         Unidad 8 - OPEN CV                                             ##");
print("##            * Procesamiento de imágenes en OpenCV                       ##");
print("##            * Detección y descripción de imágenes                       ##");
print("##            * Detección de objetos                                      ##");
print("##                                                                        ##");
print("##         Unidad 9 - Programación de eventos                             ##");
print("##            * Módulo sched                                              ##");
print("##            * Declaración de programadores                              ##");
print("##            * Programar eventos y poner en marcha el programador        ##");
print("##            * Programación de eventos considerando prioridades          ##");
print("##            * Cancelación de eventos                                    ##");
print("##                                                                        ##");
print("##         Unidad 10 - GIT Colaborativo -Pair Programming                 ##");
print("##            * Introducción a CVS y comparativa con SVN                  ##");
print("##            * Creando un repositorio con GIT, clonar, crear branches    ##");
print("##            * Borrar, guardar (stash), recuperar (pop)                  ##");
print("##            * Configuración de remote                                   ##");
print("##            * Configuración de Git avanzada                             ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##         Unidad 5 - MySQL, Parte 1                                      ##");
print("##            * INSERT, UPDATE, DELETE, SELECT                            ##");
print("##            * FECHAS Y HORAS                                            ##");
print("##            * %LIKE%                                                    ##");
print("##            * JOIN                                                      ##");
print("##                                                                        ##");
print("##         Unidad 6 - MySQL, Parte 2                                      ##");
print("##            * MySQL en Python                                           ##");
print("##            * puntero y verificación de consultas                        ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                              Bases de Datos                            ##");
print("##                                                                        ##");
print("##                         libreria mysql.connector                       ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                         Create Database                                ##");
print("##                         Create Table                                   ##");
print("##                         Insert                                         ##");
print("##                         Select                                         ##");
print("##                         Where                                          ##");
print("##                         Order By                                       ##");
print("##                         Delete                                         ##");
print("##                         Drop Table                                     ##");
print("##                         Update                                         ##");
print("##                         Limit                                          ##");
print("##                         Join                                           ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                MySQL has 3 main categories of data types namely        ##");
print("##                                                                        ##");
print("##                               Numeric,                                 ##");
print("##                               Text                                     ##");
print("##                               Date/time.                               ##");
print("##                                                                        ##");
print("##  Numeric Data types                                                    ##");
print("##  Numeric data types are used to store numeric values. It is very       ##");
print("##    important to make sure range of your data is between lower and upper##");
print("##    boundaries of numeric data types.                                   ##");
print("##               TINYINT( )    -128 to 127 normal 0 to 255                ##");
print("##               SMALLINT( )   -32768 to 32767 normal                     ##");
print("##               MEDIUMINT( )  -8388608 to 8388607 normal                 ##");
print("##               INT( )        -2147483648 to 2147483647 normal           ##");
print("##               BIGINT( )     -9223372036854775808 to                    ##");
print("##                           9223372036854775807 normal                   ##");
print("##               FLOAT         A small approximate number with a floating ##");
print("##                   decimal point.                                       ##");
print("##               DOUBLE( , )   A large number with a floating decimal     ##");
print("##                   point.                                               ##");
print("##               DECIMAL( , )  A DOUBLE stored as a string , allowing     ##");
print("##                   for a fixed decimal point. Choice for storing        ##");
print("##                   currency values.                                     ##");
print("##                                                                        ##");
print("##  Text Data Types                                                       ##");
print("##  As data type category name implies these are used to store text values##");
print("##  Always make sure you length of your textual data do not exceed        ##"); 
print("##  maximum lengths.                                                      ##");
print("##               CHAR( )       A fixed section from 0 to 255 characters   ##");
print("##               VARCHAR( )    A variable section from 0 to 255 chrs      ##");
print("##               TINYTEXT      A string with a max. length of 255 chrs.   ##");
print("##               TEXT          A string with a max. length of 65535       ##");
print("##               BLOB          A string with a max. length of 65535       ##");
print("##               MEDIUMTEXT    A string with a max. length of 16777215    ##");
print("##               MEDIUMBLOB    A string with a max. length of 16777215    ##");
print("##               LONGTEXT      A string with a max. length of 4294967295  ##");
print("##               LONGBLOB      A string with a max. length of 4294967295  ##");
print("##                                                                        ##");
print("##  Date / Time                                                           ##");
print("##               DATE          YYYY-MM-DD                                 ##");
print("##               DATETIME      YYYY-MM-DD HH:MM:SS                        ##");
print("##               TIMESTAMP     YYYYMMDDHHMMSS                             ##");
print("##               TIME          HH:MM:SS                                   ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##  Apart from above there are some other data types in MySQL.            ##");
print("##                                                                        ##");
print("##  ENUM     To store text value chosen from a list of predefined text    ##");
print("##           values                                                       ##");
print("##  SET      This is also used for storing text values chosen from a list ##");
print("##           predefined text values. It can have multiple values.         ##");
print("##  BOOL     Synonym for TINYINT(1), used to store Boolean values         ##");
print("##  BINARY   Similar to CHAR, difference is texts are stored in binary    ##");
print("##           format.                                                      ##");
print("##  VARBINARY   Similar to VARCHAR, difference is texts are stored        ##");
print("##              in binary format.                                         ##");
print("##                                                                        ##");
print("############################################################################");
import mysql.connector
       
def borrar_base():
	try:
		nombre_DDBB = "bd1"
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

#import mysql.connector
#conexion1=mysql.connector.connect(host="localhost",user="root", passwd="utn" ,  database="bd1")
#cursor1=conexion1.cursor()
#sql="insert into articulos(descripcion, precio,codigo) values (%s,%s,%s)"
#filas=[ ("naranjas", 23.50,"nra"), ("bananas", 34,"banana"),("peras", 21,"pera"),("sandía", 19.60,"sandia") ]
#cursor1.executemany(sql, filas)
#conexion1.commit()
#conexion1.close()
	try:
		nombre_DDBB = "bd1"
		nombre_tabla = "articulos"
		nombre_columna_1 = "descripcion"
		nombre_columna_2 = "precio"
		nombre_columna_3 = "codigo"
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

borrar_base();
crear_base();

