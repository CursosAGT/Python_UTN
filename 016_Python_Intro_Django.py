from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print('''
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                     Django                                  ║
║                                    --------                                 ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║          Instalación                                                        ║
║                python -m pip install --upgrade pip                          ║
║                pip install Django                                           ║
║                                                                             ║
║                cd...voy a un directorio para crear el proyecto Django2019   ║
║                                                                             ║
║          Creo un proyecto                                                   ║
║                django-admin.py startproject TP_django                       ║
║                                                                             ║
║          (ver en el navegador las carpetas que se crean en el disco local)  ║
║                                                                             ║
║          Bases de datos                                                     ║
║                Se generaran las bases de datos necesarias con la instalación║
║                básica donde se crearan las bases y tablas django.           ║
║                                                                             ║
║               opciones:              	                                      ║
║                 A) Dejo por defauld sqlite como base de datos para django   ║
║                 B) configuro mi base de datos con el conector y demas       ║
║                    requerimientos                                           ║
║          Genero las bases y tablas                                          ║
║                 python manage.py migrate                                    ║
║                 python3 manage.py migrate                                   ║
║                                                                             ║
║           Primera prueba                                                    ║
║                cd...voy a un directorio creado por django para mi proyecto  ║
║                /Django2019/TP_django/                                       ║
║                                                                             ║
║               opciones:              	                                      ║
║                 Desde consola        	                                      ║
║                          A) python manage.py runserver                      ║
║                          B) python3 manage.py runserver                     ║
║                 Desde un IDE                                                ║
║                          C) Abro la consola del IDE y sigo como opción A o B║
║                          C) voy a comando de ejecución y agrego runserver   ║
║                                       python "%f" runserver                 ║
║                                       python3 "%f" runserver                ║
║                                                                             ║
║          Abro el navegador web(firefox, chrome, opera, etc.) y cargo la pag.║
║              http://localhost:8000/                                         ║
║              http://127.0.0.1:8000/                                         ║
║                                                                             ║
║          <<< debería aparecer una pantalla de bienvenida >>>                ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║          Configuración                                                      ║
║                cd...voy a un directorio creado por django para mi proyecto  ║
║                /Django2019/TP_django/                                       ║
║                python manage.py createsuperuser                             ║
║                python3 manage.py createsuperuser                            ║
║                                                                             ║
║                creamos el usuario                                           ║
║                     Username (leave blank to use 'xxx'): utn                ║
║                     Email address: cursos.agt@gmail.com                     ║
║                     Password: utn_2019                                      ║
║                     Password (again): utn_2019                              ║
║                          + de 8 caracteres                                  ║
║                     >>>Superuser created successfully.                      ║
║                                                                             ║
║          Abro el navegador web(firefox, chrome, opera, etc.) y cargo la pag.║
║              http://localhost:8000/admin/                                   ║
║              http://127.0.0.1:8000/admin/                                   ║
║                                                                             ║
║                     Ingresamos al menú vía navegador web                    ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║          Primer ejercicio                                                   ║
║                desde el IDE creo en el directorio pertinente admin.py       ║
║                /Django2019/TP_django/TP_django/admin.py                     ║
║                                                                             ║
╚ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╝
'''
from django.contrib import admin
from myapp.models import Name
admin.site.register(Name)
'''
╔ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╗
║                                                                             ║
║                desde el IDE abro en el directorio pertinente urls.py        ║
║                /Django2019/TP_django/TP_django/urls.py                      ║
║                                                                             ║
╚ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╝
'''
from django.contrib import admin
from django.urls import path
#from TP_django.views import utn#        Importa aqui desde tu proyecto la funcione)
'''
╔ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╗
║                                                                             ║
║                desde el IDE creo en el directorio pertinente views.py       ║
║                /Django2019/TP_django/TP_django/views.py                     ║
║                                                                             ║
╚ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╝
'''
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render, redirect
import datetime
class clase(object):
	def __init__(self,dato_1,dato_2,dato_3,dato_4):
		self.dato_1=dato_1
		self.dato_2=dato_2
		self.dato_3=dato_3
		self.dato_4=dato_4
# Create your views here.

def index(request):
    names_from_db = Name.objects.all()
    context_dict = {'names_from_context': names_from_db}
    return render(request, 'index.html', context_dict)


def utn(request):# primera funcion de vista

	return HttpResponse("Menu\n primera pagina Django  --> <a href='../menu/'>enlace al Menu</a>	")

def menu(request):# segunda funcion de vista

	return HttpResponse("""
	<HTML>
		<HEAD>
			<TITLE>pagina Menu Django</TITLE>
		</HEAD>
		<BODY>
			<center>
				<H1>Esto es un ejemplo de lo simple que es usar Django</H1>
				<P><IMG SRC= "http://www.mithril.com.ar/imagenes/cartel_0.gif" width="600" height="400"/></P>
				<P><FONT COLOR="blue">Segundo cuatrimestre</font></P>
				<BR> Salto de linea. Uso de <STRONG>negritas </STRONG> para complementar.
				<P><h2>Python Django</h2></P>
				<H3><FONT COLOR="red">Hola Alumnos UTN 2019</FONT><H3>
				<P>Un <a href= "http://www.mithril.com.ar/">enlace</a></P>
				<HR>
			</center>
			<UL>
				<LI> Generamos una lista de objetos.
				<LI> <a href='../uno/'>enlace a la pagina uno</a>
				<LI> <a href='../dos/'>enlace a la pagina dos</a>
				<LI> <a href='../tres/'>enlace a la pagina tres</a>
				<LI> <a href='../cuatro/'>enlace a la pagina cuatro</a>
				<LI> <a href='../cinco/'>enlace a la pagina cinco</a>
				<LI> <a href='../seis/'>enlace a la pagina seis</a>
			</UL>
		</BODY>
	</HTML>
	""")

def uno(request):#
	temp = datetime.datetime.now()
	Hoy = str(temp.strftime("%x"));
	Hora = str(temp.strftime("%I:%M"));
	con_fecha=("""
	<HTML>
		<HEAD>
			<TITLE>pagina UNO Django</TITLE>
		</HEAD>
		<BODY>
			<center>
				<H1>Hoy es %s</H1>
				<H1>y la hora GMT es %s  en su servidor</H1>
			</center>
			<a href='../menu/'>enlace al Menu</a>
		</BODY>
	</HTML>
	""")%(Hoy, Hora)
	return HttpResponse(con_fecha)#<--------------------------------se envian datos desde el programa a la pagina
def dos(request ):#
	desde_templates= open("TP_django/templates/plantilla_dos.html");
	Template_pagina_dos = Template(desde_templates.read());
	desde_templates.close();
	Context_pagina_dos=Context();
	pagina_dos=Template_pagina_dos.render(Context_pagina_dos);
	return HttpResponse(pagina_dos)#<--------------------------------Uso de una pagina externa

def tres(request):#
	date_time = datetime.datetime.now()
	Hoy = str(date_time.strftime("%x"));
	Hora = str(date_time.strftime("%I:%M"));

	desde_templates= open("TP_django/templates/plantilla_tres.html");
	Template_pagina_tres = Template(desde_templates.read());
	desde_templates.close();
	Context_pagina_tres=Context({"pag_dia":Hoy,"pag_hora":Hora,"pag_date_time":date_time});
	pagina_tres=Template_pagina_tres.render(Context_pagina_tres);
	return HttpResponse(pagina_tres)#<--------------------------------se envian datos a pag externa desde el programa a la pagina

def cuatro(request):#

	objeto_desde_clase=clase("dato 1","dato 2","dato 3","dato 4")
	desde_templates= open("TP_django/templates/plantilla_cuatro.html");
	Template_pagina_cuatro = Template(desde_templates.read());
	desde_templates.close();
	Context_pagina_cuatro=Context({"pag_dato_1":objeto_desde_clase.dato_1,"pag_dato_2":objeto_desde_clase.dato_2,"pag_dato_3":objeto_desde_clase.dato_3,"pag_dato_4":objeto_desde_clase.dato_4});
	pagina_cuatro=Template_pagina_cuatro.render(Context_pagina_cuatro);
	return HttpResponse(pagina_cuatro)#<--------------------------------se envian datos a pag externa desde el programa a la pagina

def cinco(request):#

	Nombre_tupla_1 = ["item 1","item 2","item 3","item 4","item 5","item 6"]
	Direccion_tupla_2 = ["../uno/","../dos/","../tres/","../cuatro/","../cinco/","../seis/"]
	desde_templates= open("TP_django/templates/plantilla_cinco.html");
	Template_pagina_cinco = Template(desde_templates.read());
	desde_templates.close();
	Context_pagina_cinco=Context({"pag_Nombre_tupla_1":Nombre_tupla_1,"pag_Direccion_tupla_2":Direccion_tupla_2});
	pagina_cinco=Template_pagina_cinco.render(Context_pagina_cinco);
	return HttpResponse(pagina_cinco)#<--------------------------------se envian datos a pag externa desde el programa a la pagina

def seis(request):#
	objeto_desde_clase=clase("dato 1","dato 2","dato 3","dato 4")
	return render(request,"templates/plantilla_seis.html",{"pag_dato_1":objeto_desde_clase.dato_1,"pag_dato_2":objeto_desde_clase.dato_2,"pag_dato_3":objeto_desde_clase.dato_3,"pag_dato_4":objeto_desde_clase.dato_4});#<--------------------------------se envian datos a pag externa desde el programa a la pagina
'''
╔ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╗
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
'''

