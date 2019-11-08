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
from tkinter import messagebox as mb
from tkinter import scrolledtext as st

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

		self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar)
		self.boton1.grid(column=1, row=5, padx=4, pady=4)

	def consultar(self):
		datos=(self.codigo.get())
		respuesta=self.articulo1.consulta(datos)
		print ("respuesta",respuesta)
		if len(respuesta)>0:
			self.descripcion.set(respuesta[0][0])
			self.precio.set(respuesta[0][1])
			self.codigo.set(respuesta[0][2])
			self.stock.set(respuesta[0][3])
			self.Vencimiento.set(respuesta[0][4])
		else:
			self.descripcion.set('')
			self.precio.set('')
			self.stock.set('')
			self.codigo.set('')
			self.Vencimiento.set('')
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
