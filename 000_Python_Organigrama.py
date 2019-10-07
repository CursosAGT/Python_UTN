from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass

limpiar();
#################################################################
print("""
#http://docs.fabfile.org/en/2.4/
  Durante el siglo XX, científicos como Alan Turing y Lorenzo Church fundaron las bases del cómputo, la programación y sus lenguajes. Los lenguajes de programación actuales, a diferencia de los lenguajes humanos tienen una morfología rígida y simplificada con el fin de ejecutar instrucciones específicas en los sistemas de cómputo. 
  Lenguajes de alto y bajo nivel. 
  Los lenguajes de bajo nivel constan de un conjunto básico de instrucciones que son ejecutados directamente por la unidad de procesamiento de un sistema de cómputo, tal como es el caso del lenguaje ensamblador. Dichos lenguajes están ligados intrínsecamente al tipo de procesador que los ejecuta y resultan ser muy complicados de elaborar e interpretar por las personas. 
  Por su parte, los lenguajes de alto nivel son más accesibles para el ser humano e incluso menos dependientes del tipo de hardware, pero deben de ser a su vez traducidos a lenguaje de de bajo nivel. 
  Lenguajes compilados e interpretados. 
  Los lenguajes de alto nivel interactúan con los sistema de cómputo de dos formas. 
      Mediante un compilador, el cual traduce el código de un programa a lenguaje de bajo nivel, dando por resultado un 'archivo binario' el cual es susceptible de ser ejecutado. 
      Mediante un intérprete, el cual ejecuta de inmediato las instrucciones que se ingresan. 
  Por lo general los lenguajes compilados son más rápidos y consumen menos recursos que los lenguajes interpretados en vista de que el archivo resultante es código de bajo nivel, mientras que los lenguajes interpretados deben seguir un proceso a través de varios niveles de abstracción hasta que las instrucciones son ejecutadas por el sistema. 
  Python es un lenguaje interpretado de alto nivel. 
""");
limpiar();
#################################################################
print("""
* * * * * Sinoptico* * * * * 
  * Programar, manipulacion de datos(objetos) tras su ingreso hasta su salida
      Un lenguaje es un conjunto de cadenas de símbolos con los que se pueden crear mensajes. De ese modo los mensajes son transmitidos de un emisor a un receptor. Aún cuando en la naturaleza se pueden identificar ciertos lenguajes, los seres humanos hemos desarrollado lenguajes de diversos tipos y gran complejidad. 
      Los lenguajes constan principamente de la gramática, la cual trata sobre la construcción del lenguaje, y la semántica, la cual trata sobre el significado del lenguaje. 
         A su vez, la gramática consta de: 
              Morfología: cómo se construyen las notaciones (género, tiempos, declinaciones). 
             Sintaxis: cómo se deben escribir las notaciones (orden, estructura). 
  * Nombre, es la referencia de un dato en un tiempo y espàcio
      Nombre : en =/= espacios ,  =  tiempo de ejecucion =/= datos
      Nombre : en  =  espacios , =/= tiempo de ejecucion =/= datos
  * Objeto, es su espacio con nombre. Individualidad, con caracteristicas
      es su materialización de algo incluso un dato
      Posee atributos propios o heredados
      Genera acciones propias o heredadas
  * Funcion-Metodo-Accion-Tarea-Proceso-Verbo
      Es el verbo o accion perteneciente a un objeto
      Los métodos son bloques de código (o funciones) de una clase que se utilizan para definir el comportamiento de los objetos.
  * Atributos definen las características propias del objeto y modifican su estado. Son datos asociados a las clases y a los objetos creados a partir de ellas.
      De ello, se deducen los dos tipos de atributos o de variables existentes: variables de clase y variables de instancia (objetos).
  Tanto para acceder a los atributos como para llamar a los métodos se utiliza el método denominado de notación de punto que se basa en escribir el nombre del objeto o de la clase seguido de un punto y el nombre del atributo o del método con los argumentos que procedan: clase.atributo, objeto.atributo, objeto.método([argumentos]).
  * Instanciar, es crear objetos desde una clase.
  * Clase, es el razonamiento abstracto de un objeto. Segundo Apellidojo en distintos capas, en equipo, en grupo, Fron end orientada (al usuario)/ back end (orientada al proceso)
  * Las clases en este contexto permiten definir los atributos y el comportamiento, mediante métodos, de los objetos de un programa. Una clase es una especie de plantilla o prototipo que se utiliza para crear instancias individuales del mismo tipo de objeto.
  * Ambito, es una region en el espacio donde los nombres (cuyos datos busco) son accesibles directamente.(Recordad que puede haber el mismo nombre como atributo como accion y en distintos ambitos
  * Ambito, es observable por estructuras de tabulacion
""");
limpiar();
#################################################################
print("""
  * Un espacio con un nombre hereda del Nombre ser la referencia a un dato en un tiempo y espàcio.
      Si en el espacio nombrado su dato No cambia durante el tiempo de ejecucion se denomina * constante (constantes, tuple etc)
      Si en el espacio nombrado su dato Si cambia durante el tiempo de ejecucion se denomina * variable (variable, lista, diccionario, etc
      puede haber muchos espacio nombrado igual en distintos ambitos y sus datos podran ser distintos o no
      Mutable: su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.
      Inmutable: su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución. 
  * Una variable es espacio que tendra un nombre para poder acceder a ella y sus caracteristicas seran dadas por el dato que se incorpore (* tipeado dinamico)
  * Una variable de clase es compartida por todas las instancias de una clase. Se definen dentro de la clase (después del encabezado de la clase) pero nunca dentro de un método. Este tipo de variables no se utilizan con tanta frecuencia como las variables de instancia.
  * Una variable de instancia se define dentro de un método y pertenece a un objeto determinado de la clase instanciada. 
      Mutable: su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.
      Inmutable: su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución. 
""");
limpiar();
#################################################################
print("""
Categoría de tipo________Nombre______Descripción
Números inmutables_______int_________entero
_________________________long________entero largo
_________________________float_______coma flotante
_________________________complex_____complejo
_________________________bool________booleano True / False
Secuencias inmutables____str_________cadena de caracteres
_________________________unicode_____cadena de caracteres Unicode
_________________________tuple_______tupla
_________________________xrange______rango inmutable
Secuencias mutables______list________lista
_________________________range_______rango mutable
Mapeosprint______________dict________diccionario
Conjuntos mutables_______set_________conjunto mutable
Conjuntos inmutables_____frozenset___Conjunto inmutable
""");
limpiar();
#################################################################
print("""
https://pythonprogramming.net/
http://docs.python.org.ar/tutorial/3/classes.html
https://pythonista.io/cursos/py101
Características de Python.
 
  A lo largo de estos cursos se explorarán y aprovecharán las características que hacen de Python un lenguaje tan popular y poderoso.
  
      Sintaxis muy clara y legible.
      Fuerte capacidad de introspección.
      Orientación a objetos intuitiva.
      Expresión del código procedimental.
      Altamente modular, soporta paquetes jerárquicos.
      Enfocado en el uso de excepciones para el manejo de errores.
      Tipos de datos dinámicos de muy alto nivel.
      Extensa biblioteca estándar (STL) y módulos de terceros para prácticamente todas las tareas.
      Extensiones y módulos fácilmente escritos en C, C + + (o Java para Jython, o. NET para IronPython).
      Integrable dentro de las aplicaciones como una interfaz de scripting.
""");
limpiar();
#################################################################
print("""
  Aplicaciones de Python.
  
  Al ser un lenguaje multipropósito y altamente portable, Python se ha utilizado para desarrollar:
  
      Aplicaciones de escritorio.
      Aplicaciones web.
      Análisis de datos.
      Administración de servidores.
      Seguridad y análisis de penetración.
      Cómputo en la nube.
      Cómputo científico.
      Análisis de lenguaje natural.
      Visión artificial.
      Animación, videojuegos e imágenes generadas por computadora.
      Aplicaciones móviles.
""");
limpiar();
#################################################################
print("""
  Distribuciones: 
 ----------------- 
  Python ya viene con una gran biblioteca estándar, sin embargo existen algunas 'distribuciones' que pretenden extender al lenguaje con propósitos particulares. Aquí es posible consultar las diversas distribuciones de Python. 
  Instalación: 
 -------------- 
 Las principales distribuciones de GNU/Linux, los sistemas *BSD, así como Mac OS X y la mayoría de los UNIX vienen al menos con Python 2 preinstalado. Del mismo modo, las principales distribuciones de GNU/Linux cuentan con paquetes de instalación de Python 3. 
  Las versiones más recientes de Python pueden ser descargadas desde el sitio principal de Python incluyendo binarios para Mac OS X y Windows e incluso es posible descargar el código fuente. 
   
  NOTA Anaconda es una distribución de Python 2 y Python 3 especializada en cómputo científico, sin embargo es de muy fácil instalación y gestión tanto en Windows como en Mac OS X y GNU/Linux. Es una alternativa muy recomendable a las versiones oficiales de Python. 
  Breve introducción a los lenguajes de programación. 
  Un lenguaje es un conjunto de cadenas de símbolos con los que se pueden crear mensajes. De ese modo los mensajes son transmitidos de un emisor a un receptor. Aún cuando en la naturaleza se pueden identificar ciertos lenguajes, los seres humanos hemos desarrollado lenguajes de diversos tipos y gran complejidad. 
  Los lenguajes constan principamente de la gramática, la cual trata sobre la construcción del lenguaje, y la semántica, la cual trata sobre el significado del lenguaje. 
   
  A su vez, la gramática consta de: 
      Morfología: cómo se construyen las notaciones (género, tiempos, declinaciones). 
      Sintaxis: cómo se deben escribir las notaciones (orden, estructura). 
Gracias
""");
limpiar();
#################################################################
print("""

import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import time
from datetime import timedelta
from dateutil.relativedelta import relativedelta

import time
import calendar

pip install imutils
import imutils
import os

pip install tkintertable
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

pip install numpy
import numpy as np


pip install opencv-python
import cv2

pip install matplotlib
import math
from matplotlib import pyplot as plt


pip install Pillow==2.2.2
from PIL import Image, ImageTk

Instalar MySQL// maria db // workbench
pip install mysql-connector 
import mysql.connector

pip install schedule
import schedule

from collections import Counter

python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
zypper -n in mysql mysql-administration mysql-client mysql-query-browser mysql-gui-tools
""");
