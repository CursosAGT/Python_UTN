#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
#módulo: formularioPython_BBDD_articulos.py
# Copyright 2019 Ariel H Garcia T <cursos.agt@gmail.com>
from Estructura import *
#################################################################
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                               Trabajo Final Python                          ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                          presentacion_BBDD_en_pantalla_grafica              ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from PIL import ImageTk, Image

import Python_BBDD_articulos#--------------------------------------------------------------------------------LLamo a mi armador

class Formularioarticulos:
	def __init__(self):
		self.articulo1=Python_BBDD_articulos.articulos()
		self.ventana1=tk.Tk()
		self.ventana1.title("Mantenimiento de artículos")
		self.cuaderno1 = ttk.Notebook(self.ventana1)
		self.carga_articulos()
		self.consulta_por_codigo()
		self.listado_completo()
		self.borrado()
		self.modificar()
		self.mostrar_vender()
		self.salir()
		self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
		self.ventana1.mainloop()

	def carga_articulos(self):
		self.pagina1 = ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina1, text="Carga de artículos")

		self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo")
		self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

		self.label1=ttk.Label(self.labelframe1, text="Codigo:")
		self.label1.grid(column=0, row=0, padx=4, pady=4)
		self.Codigocarga=tk.StringVar()
		self.entryCodigo=ttk.Entry(self.labelframe1, textvariable=self.Codigocarga)
		self.entryCodigo.grid(column=1, row=0, padx=4, pady=4)

		self.label2=ttk.Label(self.labelframe1, text="Descripción:")
		self.label2.grid(column=0, row=1, padx=4, pady=4)
		self.descripcioncarga=tk.StringVar()
		self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
		self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)

		self.label3=ttk.Label(self.labelframe1, text="Precio:")
		self.label3.grid(column=0, row=2, padx=4, pady=4)
		self.preciocarga=tk.StringVar()
		self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
		self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

		self.label4=ttk.Label(self.labelframe1, text="Stock:")
		self.label4.grid(column=0, row=3, padx=4, pady=4)
		self.Stockcarga=tk.StringVar()
		self.entryStock=ttk.Entry(self.labelframe1, textvariable=self.Stockcarga)
		self.entryStock.grid(column=1, row=3, padx=4, pady=4)

		self.label5=ttk.Label(self.labelframe1, text="Vencimiento:")
		self.label5.grid(column=0, row=4, padx=4, pady=4)
		self.Vencimientocarga=tk.StringVar()
		self.entryVencimiento=ttk.Entry(self.labelframe1, textvariable=self.Vencimientocarga)
		self.entryVencimiento.grid(column=1, row=4, padx=4, pady=4)

		self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
		self.boton1.grid(column=1, row=5, padx=4, pady=4)

	def agregar(self):
		datos=(self.Codigocarga.get(), self.descripcioncarga.get(), self.preciocarga.get(), self.Stockcarga.get(), self.Vencimientocarga.get())
		self.articulo1.alta(datos)
		mb.showinfo("Información", "Los datos fueron cargados")
		self.codigo.set("")
		self.descripcion.set("")
		self.precio.set("")
		self.Stock.set("")
		self.Vencimiento.set("")

	def consulta_por_codigo(self):
		self.pagina2 = ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina2, text="Consulta por código")

		self.labelframe1=ttk.LabelFrame(self.pagina2, text="Artículo")
		self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

		self.label1=ttk.Label(self.labelframe1, text="Código:")
		self.label1.grid(column=0, row=0, padx=4, pady=4)
		self.codigo=tk.StringVar()
		self.entrycodigo=ttk.Entry(self.labelframe1, textvariable=self.codigo)
		self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

		self.label2=ttk.Label(self.labelframe1, text="Descripción:")
		self.label2.grid(column=0, row=1, padx=4, pady=4)
		self.descripcion=tk.StringVar()
		self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcion, state="readonly")
		self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)

		self.label3=ttk.Label(self.labelframe1, text="Precio:")
		self.label3.grid(column=0, row=2, padx=4, pady=4)
		self.precio=tk.StringVar()
		self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.precio, state="readonly")
		self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

		self.label4=ttk.Label(self.labelframe1, text="stock:")
		self.label4.grid(column=0, row=3, padx=4, pady=4)
		self.stock=tk.StringVar()
		self.entrystock=ttk.Entry(self.labelframe1, textvariable=self.stock, state="readonly")
		self.entrystock.grid(column=1, row=3, padx=4, pady=4)

		self.label5=ttk.Label(self.labelframe1, text="Vencimiento:")
		self.label5.grid(column=0, row=4, padx=4, pady=4)
		self.Vencimiento=tk.StringVar()
		self.entryVencimiento=ttk.Entry(self.labelframe1, textvariable=self.Vencimiento, state="readonly")
		self.entryVencimiento.grid(column=1, row=4, padx=4, pady=4)

		self.label4=ttk.Label(self.labelframe1, text="Iva:")
		self.label4.grid(column=0, row=5, padx=4, pady=4)

		self.iva=tk.StringVar()
		self.entryiva=ttk.Entry(self.labelframe1, textvariable= self.iva, state="readonly")
		self.entryiva.grid(column=1, row=5, padx=4, pady=4)

		self.label5=ttk.Label(self.labelframe1, text="Observacion:")
		self.label5.grid(column=0, row=6, padx=4, pady=4)

		self.cuidado=tk.StringVar()
		self.entrycuidado=ttk.Entry(self.labelframe1, textvariable= self.cuidado, state="readonly")
		self.entrycuidado.grid(column=1, row=6, padx=4, pady=4)


		self.label6=ttk.Label(self.labelframe1, text="Mayor Precio Alimenticio hoy:")
		self.label6.grid(column=0, row=7, padx=4, pady=4)

		self.maximo=tk.StringVar()
		self.entrymaximo=ttk.Entry(self.labelframe1, textvariable= self.maximo, state="readonly")
		self.entrymaximo.grid(column=1, row=7, padx=4, pady=4)


		self.label7=ttk.Label(self.labelframe1, text="Comprando 2 packs de:")
		self.label7.grid(column=0, row=8, padx=40, pady=40)

		self.minimo=tk.StringVar()
		self.entryminimo=ttk.Entry(self.labelframe1, textvariable= self.minimo, state="readonly")
		self.entryminimo.grid(column=1, row=8, padx=4, pady=4)


		self.label8=ttk.Label(self.labelframe1, text="ult.nro dni = utl. nro Codigo 10% descuento:")
		self.label8.grid(column=0, row=9, padx=4, pady=4)

		self.ultimo=tk.StringVar()
		self.entryultimo=ttk.Entry(self.labelframe1, textvariable= self.ultimo, state="readonly")
		self.entryultimo.grid(column=1, row=9, padx=4, pady=4)

		self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar)
		self.boton1.grid(column=1, row=15, padx=4, pady=4)

	def salir(self): #esta funcion se agrego y no andaaaaaa!!!!!
		def Confirmar():
			mb.showinfo("cancelado","Vuelve a la página que deseas")


		self.pagina7 = ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina7, text="Salida")

		self.labelframe7=ttk.LabelFrame(self.pagina7, text="Salida del programa")
		self.labelframe7.grid(column=0, row=0, padx=5, pady=10)

		self.label1=ttk.Label(self.labelframe7, text="Saliendo:"  )
		self.label1.grid(column=0, row=0, padx=4, pady=4)
		self.Codigocarga=tk.StringVar()

		self.boton0=ttk.Button(self.labelframe7, text="Cancelar", command=Confirmar)
		self.boton0.grid(column=2, row=15, padx=4, pady=4)
		self.boton1=ttk.Button(self.labelframe7, text="Salir", command=self.ventana1.destroy)
		self.boton1.grid(column=4, row=15, padx=4, pady=4)

	def consultar(self):
		datos=(self.codigo.get())
		respuesta=self.articulo1.consulta(datos)
		print ("respuesta",respuesta)
		if len(respuesta)>0:
			self.descripcion.set(respuesta[0][1])
			self.precio.set(respuesta[0][2])
			self.codigo.set(respuesta[0][0])
			self.stock.set(respuesta[0][3])
			self.Vencimiento.set(respuesta[0][4])
			self.iva.set(respuesta[0][5])
			A = (respuesta[0][2])
			if float(A) < 11.0:	self.cuidado.set('Precio sin Cuotas')
			if float(A) > 10.0:	self.cuidado.set('Precio Cuidado')
			self.maximo.set(respuesta[0][6])
			self.minimo.set(respuesta[0][1] +str(" gratis ") +respuesta[0][7])
			self.ultimo.set(respuesta[0][8] + str( ' $ ')  + str(A - ((A * 0.10))))

			#PABLOOOOOO
			STRING = "imagenes/"+self.codigo.get() + ".jpg"
			print(STRING)
			load = Image.open(STRING)
			render = ImageTk.PhotoImage(load)
			img = Label(self.pagina2, image=render)
			img.image = render
			img.place(x=450, y=16)

		else:
			self.descripcion.set('')
			self.precio.set('')
			self.stock.set('')
			self.codigo.set('')
			self.Vencimiento.set('')
			self.iva.set('')
			self.cuidado.set('');
			self.maximo.set('');
			self.minimo.set('');
			self.ultimo.set('');
			mb.showinfo("Información", "No existe un artículo con dicho código")

	def listado_completo(self):
		self.pagina3 = ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina3, text="Listado completo")

		self.labelframe1=ttk.LabelFrame(self.pagina3, text="Artículo")
		self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

		self.boton1=ttk.Button(self.labelframe1, text="Listado completo", command=self.listar)
		self.boton1.grid(column=0, row=0, padx=4, pady=4)
		self.scrolledtext1=st.ScrolledText(self.labelframe1, width=30, height=10)
		self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

	def listar(self):
		respuesta=self.articulo1.recuperar_todos()
		print (respuesta)
		self.scrolledtext1.delete("1.0", tk.END)
		for fila in respuesta:
			self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+ "\ndescripción:"+fila[1]+ "\nprecio:"+str(fila[2])+"\nstock:"+str(fila[3])+"\nVencimiento:"+str(fila[4])+"\n\n")

	def borrado(self):
		self.pagina4 = ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina4, text="Borrado de artículos")
		self.labelframe1=ttk.LabelFrame(self.pagina4, text="Artículo")
		self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
		self.label1=ttk.Label(self.labelframe1, text="Código:")
		self.label1.grid(column=0, row=0, padx=4, pady=4)
		self.codigoborra=tk.StringVar()
		self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
		self.entryborra.grid(column=1, row=0, padx=4, pady=4)
		self.boton1=ttk.Button(self.labelframe1, text="Borrar", command=self.borrar)
		self.boton1.grid(column=1, row=1, padx=4, pady=4)

	def borrar(self):
		datos=(self.codigoborra.get(), )
		cantidad=self.articulo1.baja(datos)
		if cantidad==1:
			mb.showinfo("Información", "Se borró el artículo con dicho código")
		else:
			mb.showinfo("Información", "No existe un artículo con dicho código")

	def modificar(self):
		self.pagina5 = ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina5, text="Modificar artículo")
		self.labelframe1=ttk.LabelFrame(self.pagina5, text="Artículo")
		self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
		self.label1=ttk.Label(self.labelframe1, text="Código:")
		self.label1.grid(column=0, row=0, padx=4, pady=4)
		self.codigomod=tk.StringVar()
		self.entrycodigo=ttk.Entry(self.labelframe1, textvariable=self.codigomod)
		self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
		self.label2=ttk.Label(self.labelframe1, text="Descripción:")
		self.label2.grid(column=0, row=1, padx=4, pady=4)
		self.descripcionmod=tk.StringVar()
		self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcionmod)
		self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
		self.label3=ttk.Label(self.labelframe1, text="Precio:")
		self.label3.grid(column=0, row=2, padx=4, pady=4)
		self.preciomod=tk.StringVar()
		self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciomod)
		self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
		self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar_mod)
		self.boton1.grid(column=1, row=3, padx=4, pady=4)
		self.boton1=ttk.Button(self.labelframe1, text="Modificar", command=self.modifica)
		self.boton1.grid(column=1, row=4, padx=4, pady=4)

	def vender(self):
		art = {
			"id_articulo":self.aux_codigo_venta.get(),
			"cant_vendidos":self.aux_cantidad_venta.get()
		}

		msj = self.articulo1.venta(art)

		if not msj:
			mb.showinfo("Información", "Se vendió el artículo")
		else:
			mb.showinfo("Información", msj)

	def mostrar_vender(self):
		self.pagina6 = ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina6, text="Vender articulo")
		self.labelframe1=ttk.LabelFrame(self.pagina6, text="Artículo")
		self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

		self.label1=ttk.Label(self.labelframe1, text="Código:")
		self.label1.grid(column=0, row=0, padx=4, pady=4)

		self.aux_codigo_venta=tk.StringVar()
		self.codigo_venta=ttk.Entry(self.labelframe1, textvariable=self.aux_codigo_venta)
		self.codigo_venta.grid(column=1, row=0, padx=4, pady=4)

		self.label2=ttk.Label(self.labelframe1, text="Cantidad:")
		self.label2.grid(column=0, row=1, padx=4, pady=4)

		self.aux_cantidad_venta=tk.StringVar()
		self.cantidad_venta=ttk.Entry(self.labelframe1, textvariable=self.aux_cantidad_venta)
		self.cantidad_venta.grid(column=1, row=1, padx=4, pady=4)

		self.boton1=ttk.Button(self.labelframe1, text="Vender", command=self.vender)
		self.boton1.grid(column=1, row=4, padx=4, pady=4)

	def modifica(self):

		datos=(self.descripcionmod.get(), self.preciomod.get(), self.codigomod.get())
		cantidad=self.articulo1.modificacion(datos)
		if cantidad==1:
			mb.showinfo("Información", "Se modificó el artículo")
		else:
			mb.showinfo("Información", "No existe un artículo con dicho código")

	def consultar_mod(self):
		datos=(self.codigomod.get())#datos=(self.codigomod.get(), )
		print (datos)
		respuesta=self.articulo1.consulta(datos)
		if len(respuesta)>0:
			self.descripcionmod.set(respuesta[0][0])
			self.preciomod.set(respuesta[0][1])
			self.codigomod.set(respuesta[0][2])
		else:
			self.descripcionmod.set('')
			self.preciomod.set('')
			mb.showinfo("Información", "No existe un artículo con dicho código")




aplicacion1=Formularioarticulos()
