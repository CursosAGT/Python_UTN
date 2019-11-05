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
#módulo: artículos.py
import mysql.connector

class artículos:

	def abrir(self):
		conexion=mysql.connector.connect(host="localhost", user="root", passwd="utn", database="bd1")
		return conexion

	def alta(self, datos):
		cone=self.abrir()
		cursor=cone.cursor()
		sql="insert into artículos(descripción, precio) values (%s,%s)"
		cursor.execute(sql, datos)
		cone.commit()
		cone.close()

	def consulta(self, datos):
		cone=self.abrir()
		cursor=cone.cursor()
#		sql="select descripción, precio from artículos where codigo=%s"
#		sql="select descripción, precio from artículos where codigo="+str(datos)
		sql="select * from artículos where codigo='s1'"
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
		sql="select codigo, descripción, precio from artículos"
		cursor.execute(sql)

		resultados = cursor.fetchall()
#		for cada_rec in resultados:
#			print(cada_rec)
		cone.close()
		return resultados



	def baja(self, datos):
		cone=self.abrir()
		cursor=cone.cursor()
		sql="delete from artículos where codigo=%s"
		cursor.execute(sql, datos)
		cone.commit()
		cone.close()
		return cursor.rowcount # retornamos la cantidad de filas borradas

	def modificacion(self, datos):
		cone=self.abrir()
		cursor=cone.cursor()
		sql="update artículos set descripción=%s, precio=%s where codigo=%s"
		cursor.execute(sql, datos)
		cone.commit()
		cone.close()
		return cursor.rowcount # retornamos la cantidad de filas modificadas
