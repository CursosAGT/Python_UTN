#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>


#módulo: articulos.py
import mysql.connector

class Articulos:

	def abrir(self):
		conexion=mysql.connector.connect(host="localhost", user="root", passwd="", database="Supermercado")
		return conexion

	def alta(self, datos):
		cone=self.abrir()
		cursor=cone.cursor()
		sql="insert into articulos(codigo, descripcion, precio, stock, Vencimiento) values (%s,%s,%s,%s,%s)"
		cursor.execute(sql, datos)
		cone.commit()
		cone.close()

	def consulta(self, datos):

		cone=self.abrir()
		cursor=cone.cursor()
		datos2 = ("'"+str(datos)+"'")
		sql="select descripcion, precio, codigo, stock, Vencimiento from articulos where codigo="+str(datos2)
		cursor.execute(sql)
		resultados = cursor.fetchall()
		print (resultados)
		cone.close()
		return resultados

	def recuperar_todos(self):
		cone=self.abrir()
		cursor=cone.cursor()
		sql="select codigo, descripcion, precio, stock, Vencimiento from articulos"
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
