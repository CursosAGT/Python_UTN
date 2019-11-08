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
		sql="select codigo, descripcion, precio, stock, Vencimiento, (precio/0.21) as iva, (select concat(precio,'$ -' ,descripcion) from articulos order by precio desc limit 1) as maximo , (select concat(descripcion,' - $' ,precio)  from articulos order by precio asc limit 1) as minimo, SUBSTRING(codigo, -1) as ultimo from articulos where codigo=" +str(datos2)
#		sql="select descripcion, precio, codigo, stock, Vencimiento from articulos where codigo="+str(datos2)
#		cursor.execute(sql)
		cursor.execute(sql,datos2)
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

	#Metodo de venta de articulo
	def venta(self,datos):
		msj = ''

		try:
			connection=self.abrir()
			cursor = connection.cursor()
		except:
			msj = 'Error al conectar con la base de datos'

		if msj:
			return msj

		try:
			existe = self.consulta(datos['id_articulo'])

			#Si no existe el articulo
			if len(existe) == 0:
				raise ValueError('El artículo no existe')

			#Si se paso el stock a negativo
			if existe[0][3] < int(datos['cant_vendidos']):
				raise ValueError('No se puede realizar la venta por falta de mercadería')

			SQL_UPDATE = "UPDATE ARTICULOS A SET A.STOCK = A.STOCK - {} WHERE CODIGO = '{}'" . format(datos['cant_vendidos'],datos['id_articulo'])
			cursor.execute(SQL_UPDATE)

			SQL_INS = "INSERT INTO VENTAS(ID_ARTICULO,CANT_ARTICULOS_VENDIDOS,FECHA_VENTA) VALUES ('{}',{},NOW())" . format(datos['id_articulo'],datos['cant_vendidos'])
			cursor.execute(SQL_INS)

			connection.commit()
			connection.close()
		except ValueError as e :
			connection.rollback()
			connection.close()
			msj = str(e)
		except Exception as e :
			connection.rollback()
			connection.close()
			msj = 'No se pudo realizar la venta: ' + str(e)

		return msj
