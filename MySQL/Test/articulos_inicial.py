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
limpiar()
print("############################################################################");
print("##                                                                        ##");
print("##                         Test  - UTN 2019                               ##");
print("##                                                                        ##");
print("##                           Marzo - Abril                                ##");
print("##                                                                        ##");
print("##      A partir del el ejemplo adjunto se necesita                       ##");
print("##          1 * Se ampliara la base para las siguientes columnas.(ordenar)##");
print("##               A ) Cantidad en stock                                    ##");
print("##               B ) Unidad en stock                                      ##");
print("##               C ) Vencimiento de la mercaderia                         ##");
print("##               D ) Costo                                                ##");
print("##               E ) Area                                                 ##");
print("##               F ) Marca                                                ##");
print("##                                                                        ##");
print("##          1.2 Iniciar la base con 10 articulos para una nueva sucursal  ##");
print("##                 q se cargaran en una funcion de inicializacion de base ##");
print("##             (Las cantidades a ingresar seran de 10 productos por art.) ##");
print("##                                                                        ##");
print("##          1.3 Se cargaran 2 productos ya existentes con fecha de        ##");
print("##                  10 dias posterior a la original.)                     ##");
print("##                                                                        ##");
print("##          1.4 Se comentaran los pasos con print enconsola para su       ##");
print("##                 seguimiento                                            ##");
print("##                                                                        ##");
print("##      Pasar a clases y metodos                                          ##");
print("##                                                                        ##");
print("##          2 * Se modificaran las pantallas graficas 'articulos.py'      ##");
print("##               para agregar Stock, Fecha de vencimiento y costo.        ##");
print("##                                                                        ##");
print("##          3 * Se creara una pantallas graficas para ventas 'ventas.py'. ##");
print("##               A ) Venta del producto por cod/descripcion y cantidad    ##");
print("##                    Presentacion de la descripcion, precio y stock      ##");
print("##               B ) Generar la venta descripcion, precio y TOTAL.        ##");
print("##               C ) Descuento de la cant vendida al stock bajo el        ##");
print("##                    sistema first in first out en la bas de datos.      ##");
print("##               D )  Enviar la compra a una nueva tabla                  ##");
print("##             (Ejemplificar con ventas de 2 * con mas de 10 productos.)  ##");
print("##                                                                        ##");
print("##          4 * A las 21 horas se generaran archivos tipo texto con       ##");
print("##               A ) Listado de mercaderia con stock menor de 10 unidades ##");
print("##                    para su reposicion                                  ##");
print("##               B ) Total de costos , Ventas y utilidad bruta            ##");
print("##                                                                        ##");
print("############################################################################");
print("https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=82&codigo=82&inicio=75")

#	https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=82&codigo=82&inicio=75

import mysql.connector
import datetime 

def borrar_base():
	try:
		nombre_DDBB = "Supermercado"
		print ("Conectamos con MySQL")
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="")
		puntero = conectarse.cursor()
		puntero.execute("DROP DATABASE "+str(nombre_DDBB))
		puntero.close
		limpiar();
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		puntero.close
def crear_base():
#          1 * Se ampliara la base para las siguientes columnas.(ordenar)
#               A ) Cantidad en stock
#               B ) Unidad en stock
#               C ) Vencimiento de la mercaderia
#               D ) Costo
#               E ) Area
#               F ) Marca
	try:
		hoy = datetime.datetime.now()
		ingreso = datetime.datetime(2015,3,1)
		nombre_DDBB = "Supermercado"
		nombre_tabla = " Articulos"
		nombre_columna_1 = " Codigo"
		tipo_columna_1 = " VARCHAR(255),"
		nombre_columna_2 = " Descripcion"
		tipo_columna_2 = " VARCHAR(255),"
		nombre_columna_3 = " Costo"
		tipo_columna_3 = " FLOAT,"
		nombre_columna_4 = " Precio"
		tipo_columna_4 = " FLOAT,"
		nombre_columna_5 = " Stock"
		tipo_columna_5 = " FLOAT,"
		nombre_columna_6 = " Unidad"
		tipo_columna_6 = " VARCHAR(255),"
		nombre_columna_7 = " Vencimiento"
		tipo_columna_7 = " date ,"
		nombre_columna_8 = " Marca"
		tipo_columna_8 = " VARCHAR(255),"
		nombre_columna_9 = " Area"
		tipo_columna_9 = " VARCHAR(255)"
		print ("Conectamos con MySQL")#							1.4 Se comentaran los pasos con print enconsola para su seguimiento  
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="")
		puntero = conectarse.cursor()
		print ("CREATE DATABASE")#								1.4 Se comentaran los pasos con print enconsola para su seguimiento  
		puntero.execute("CREATE DATABASE "+str(nombre_DDBB))
		conectarse.commit()
		puntero = conectarse.cursor()		
		print(puntero.rowcount, "record inserted.")#			1.4 Se comentaran los pasos con print enconsola para su seguimiento 
		print ("USE DATABASE")#									1.4 Se comentaran los pasos con print enconsola para su seguimiento 
		puntero.execute("USE "+str(nombre_DDBB))
		puntero = conectarse.cursor()
		print ("CREATE TABLE")#									1.4 Se comentaran los pasos con print enconsola para su seguimiento 
		print ("CREATE COLUMN")#								1.4 Se comentaran los pasos con print enconsola para su seguimiento 
		#
		puntero.execute("CREATE TABLE "+str(nombre_tabla) + "( id INT AUTO_INCREMENT PRIMARY KEY,"+str(nombre_columna_1)+str(tipo_columna_1)+str(nombre_columna_2)+str(tipo_columna_2)+str(nombre_columna_3)+str(tipo_columna_3)+str(nombre_columna_4)+str(tipo_columna_4)+str(nombre_columna_5)+str(tipo_columna_5)+str(nombre_columna_6)+str(tipo_columna_6)+str(nombre_columna_7)+str(tipo_columna_7)+str(nombre_columna_8)+str(tipo_columna_8)+str(nombre_columna_9)+str(tipo_columna_9)+" )")
		puntero = conectarse.cursor()
		print ("RECORD INSERT")#								1.4 Se comentaran los pasos con print enconsola para su seguimiento 
		
#          1.2 Iniciar la base con 10 articulos para una nueva sucursal que se cargaran en una funcion de inicializacion de base
#             (Las cantidades a ingresar seran de 10 productos por art.)
		columnas_mysql = "INSERT INTO  "+str(nombre_tabla) + "( "+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+", "+str(nombre_columna_4)+", "+str(nombre_columna_5)+", "+str(nombre_columna_6)+", "+str(nombre_columna_7)+", "+str(nombre_columna_8)+", "+str(nombre_columna_9)+" ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		print ("RECORDs")#										1.4 Se comentaran los pasos con print enconsola para su seguimiento 
		ingreso = datetime.datetime(2019,4,1)
		puntero.execute(columnas_mysql, ("F1","Fideos", 30.50 ,  36.50 , 10,"Paquete" , ingreso,"Fidelim","Alimentos"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("A1","Arroz", 25.25 ,  29.50 , 10,"Kg" , ingreso,"Arromatic","Alimentos"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("P1","Pan", 20.50 ,  40.00 , 10,"Kg" , ingreso,"Farguito","Alimentos"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("C1","Capas", 100.00 ,  125.00 , 10,"Unidades" , ingreso,"Superman","Ropa"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("T1","Tasas", 30.5 ,  36.5 , 10,"Kg" , ingreso,"Brindis","Bazar"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("G1","Gel", 50.50 ,  60.50 , 10,"Pote" , ingreso,"Rock","Perfumeria"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("H1","Harinas", 8.50 ,  16.50 , 10,"Kg" , ingreso,"Blanca","Alimentos"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("S1","Sal", 10.5 ,  12.5 , 10,"Paquete 50g" , ingreso,"SuperSal","Alimentos"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("P1","Pantalones", 9.00 ,  15.00 , 10,"unidades" , ingreso,"Pair","Ropa"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("L1","Dentifrico", 15.08 ,  20.50 , 10,"pomos" , ingreso, "Dentin","Perfumeria"))
		conectarse.commit()
		print(puntero.rowcount, "record inserted.")#				1.4 Se comentaran los pasos con print enconsola para su seguimiento 
		print("cerramos coneccion");#								1.4 Se comentaran los pasos con print enconsola para su seguimiento 
		puntero.close

#          1.3 Se cargaran 2 productos ya existentes con fecha de 10 dias posterior a la original.

		puntero = conectarse.cursor()
		print ("RECORD INSERT")
		columnas_mysql = "INSERT INTO  "+str(nombre_tabla) + "( "+str(nombre_columna_1)+", "+str(nombre_columna_2)+", "+str(nombre_columna_3)+", "+str(nombre_columna_4)+", "+str(nombre_columna_5)+", "+str(nombre_columna_6)+", "+str(nombre_columna_7)+", "+str(nombre_columna_8)+", "+str(nombre_columna_9)+" ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		print ("RECORDs")
		ingreso = datetime.datetime(2019,4,21)

		puntero.execute(columnas_mysql, ("T1","Tasas", 32.50 ,  42.50 , 20,"Kg" , ingreso,"Brindis","Bazar"))
		conectarse.commit()
		puntero.execute(columnas_mysql, ("G1","Gel", 55.00 ,  65.00 , 20,"Pote" , ingreso,"Rock","Perfumeria"))
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

