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
║                              Python_BBDD_articulos                          ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");

import datetime
import mysql.connector
hoy = datetime.date.today()
print(hoy)
host_local="localhost"
usuario = "root"
password_de_msql="utn"
nombre_DDBB = "Supermercado"

class articulos:

	def abrir(self):
		connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql , database=nombre_DDBB)
		print ("Conectamos con MySQL 	connection = ",connection)
		return connection

	def alta(self, datos):
		connection=self.abrir()
		cursor=connection.cursor()
		sql="insert into articulos(codigo, descripcion, precio, stock, Vencimiento) values (%s,%s,%s,%s,%s)"
		cursor.execute(sql, datos)
		connection.commit()
		connection.close()

	def consulta(self, datos):

		connection=self.abrir()
		cursor=connection.cursor()
		datos2 = ("'"+str(datos)+"'")
		sql="select descripcion, precio, codigo, stock, Vencimiento from articulos where codigo="+str(datos2)
		cursor.execute(sql)
		resultados = cursor.fetchall()
		print (resultados)
		connection.close()
		return resultados

	def recuperar_todos(self):
		connection=self.abrir()
		cursor=connection.cursor()
		sql="select codigo, descripcion, precio, stock, Vencimiento from articulos"
		cursor.execute(sql)

		resultados = cursor.fetchall()
#		for cada_rec in resultados:
#			print(cada_rec)
		connection.close()
		return resultados



	def baja(self, datos):
		connection=self.abrir()
		cursor=connection.cursor()
		sql="delete from articulos where codigo=%s"
		cursor.execute(sql, datos)
		connection.commit()
		connection.close()
		return cursor.rowcount # retornamos la cantidad de filas borradas

	def modificacion(self, datos):
		connection=self.abrir()
		cursor=connection.cursor()
		sql="update articulos set descripcion=%s, precio=%s where codigo=%s"
		cursor.execute(sql, datos)
		connection.commit()
		connection.close()
		return cursor.rowcount # retornamos la cantidad de filas modificadas
