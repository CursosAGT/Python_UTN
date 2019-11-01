#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>
import math
def resultado_suma_metodo(valor_1,valor_2):
	return valor_1+valor_2
def resultado_resta_metodo(valor_1,valor_2):
	return  valor_1-valor_2
def resultado_multiplica_metodo(valor_1,valor_2):
	return valor_1*valor_2
def resultado_divide_metodo(valor_1,valor_2):
	try:
		return valor_1/valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
def resultado_portenciación_metodo(valor_1,valor_2):
	return valor_1**valor_2
def resultado_radicacion_metodo(valor_1,valor_2):
	return  math.sqrt(valor_2);
def resultado_porcentaje_metodo(valor_1,valor_2):
	try:
		return valor_1/valor_2*100
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
def resultado_cociente_metodo(valor_1,valor_2):
	try:
		return valor_1//valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
def resultado_resto_metodo(valor_1,valor_2):
	try:
		return valor_1%valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
