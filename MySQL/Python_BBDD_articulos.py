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

import datetime
import mysql.connector
hoy = datetime.date.today()
print(hoy)
host_local="localhost"
usuario = "root"
password_de_msql=""
nombre_DDBB = "bd1"


class articulos:

	def abrir(self):
		print ("Conectamos con MySQL")
		#connection = mysql.connector.connect(host="localhost",user="root", passwd="")
		connection = mysql.connector.connect(host= host_local ,user= usuario , passwd= password_de_msql , database=nombre_DDBB)
		return connection

	def alta(self, datos):
		cone=self.abrir()
		cursor=cone.cursor()
		# PM: Agrego codigo ->
		sql="insert into articulos(descripcion, precio, codigo) values (%s,%s,%s)" 
		cursor.execute(sql, datos)
		cone.commit()
		cone.close()

	def consulta(self, datos):
		cone=self.abrir()
		cursor=cone.cursor()
#		sql="select descripcion, precio from artículos where codigo=%s"
#		sql="select descripcion, precio from artículos where codigo="+str(datos)
		sql="select * from articulos where codigo='s1'"
		print ("#############################################################################")
		print (sql)
		print ("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
#		cursor.execute(sql, datos)
		cursor.execute(sql)
		print ("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
		resultados = cursor.fetchall()
		print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print (resultados)
		cone.close()
		return resultados

	def recuperar_todos(self):
		cone=self.abrir()
		cursor=cone.cursor()
		sql="select codigo, descripcion, precio from articulos"
		cursor.execute(sql)

		resultados = cursor.fetchall()
#		for cada_rec in resultados:
#			print(cada_rec)
		cone.close()
		return resultados



	def baja(self, datos):
		cone=self.abrir()
		cursor=cone.cursor()
		sql="delete from articulos where codigo=%s"
		cursor.execute(sql, datos)
		cone.commit()
		cone.close()
		return cursor.rowcount # retornamos la cantidad de filas borradas

	def modificacion(self, datos):
		cone=self.abrir()
		cursor=cone.cursor()
		sql="update articulos set descripcion=%s, precio=%s where codigo=%s"
		cursor.execute(sql, datos)
		cone.commit()
		cone.close()
		return cursor.rowcount # retornamos la cantidad de filas modificadas
