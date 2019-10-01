from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║                   Unidad 7 - Fechas, Horas, Archivos                        ║
║                      * Operaciones con archivos                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                Ingreso - salida de datos                    ║
║                                                                             ║
║                                                                             ║
║                                otros archivos de texto                      ║
║                                -----------------------                      ║
║                                                                             ║
║                                     crear archivos de texto                 ║
║                                                                             ║
║                                     escribir un texto                       ║
║                                                                             ║
║                             escribir una linea al final                     ║
║                                                                             ║
║                             leer un texto                                   ║
║                                                                             ║
║                             leer una linea                                  ║
║                                                                             ║
║                                     cerrar archivos                         ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                            IO  -  TIPO  o CVS 'text.txt                     ║
║                                                                             ║
║                          Unidad 7 - Fechas, Horas, Archivos                 ║
║                                * Operaciones con archivos                   ║
║                                                                             ║
║                          Unidad 4 - Listas, Tuplas y Diccionarios           ║
║                                * Operaciones con archivos                   ║
║                                libreria   pickle                            ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                   r      read   Lectura                                     ║
║                   r+     read+  Lectura/Escritura simultánea                ║
║                   w      write  Sobreescritura. Si no existe archivo se crea║
║                   a      append Añadir. Escribe al final del archivo        ║
║                          EN BINARIO                                         ║
║                   rb     read   Lectura binaria                             ║
║                   r+b    read+  Lectura/Escritura binaria simultánea        ║
║                   wb     write  Sobreescritura binaria                      ║
║                                                                             ║
║                   U            Salto de línea                               ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
	https://docs.python.org/3/library/pickle.html
""");
from io import *
nuevo(0,"inicio");
#################################################################
#IO_ext Ej_01 ;
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║ Abre el navegador en el directorio donde esta el archivo para ver que ocurre║
║   con los archivos que se generan via python                                ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
print("Un módulo es un fichero que contiene codigo PYTHON. Su extensión es .py. Almacena declaración de variables e implementación de funciones. Posibilidad de hacer referencia a otros módulos (mediante la instrucción import).")
print("salida de datos a otro archivo write");
archivo_de_texto=open("text.txt","w")#						abre el archivo text.txt para escritura y si no existe lo crea
texto_en_memoria="TEXT\nLenguaje interpretado\n Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.\n El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina.\n Los términos lenguaje interpretado y lenguaje compilado no están bien definidos porque, en teoría, cualquier lenguaje de programación puede ser interpretado o compilado.\n Cada vez es más popular, en las implementaciones más modernas de un lenguaje de programación, ofrecer ambas opciones.\n Los lenguajes interpretados también pueden diferenciarse de los lenguajes de máquina.\n Funcionalmente, tanto la ejecución y la interpretación significan lo mismo -obtener la siguiente instrucción/sentencia del programa y su ejecución-.\n Aunque el bytecode (código byte) interpretado es además idéntico a su forma en código máquina y tiene una representación en ensamblador, el término 'interpretado' se reserva en la práctica para lenguajes 'procesados por software' (como las máquinas virtuales o emuladores) por encima del procesado nativo (por ejemplo, por hardware).\n En principio, los programas de muchos lenguajes se pueden compilar o interpretar, emular o ejecutar nativamente, así que esta designación se aplica solamente a la implementación práctica más usual, en vez de representar una propiedad esencial del lenguaje.\n De forma parecida al microcódigo del procesador, muchos intérpretes, internamente recaen en una compilación en tiempo de ejecución.\n Evitando la compilación, los programas interpretados son más fáciles de evolucionar durante el desarrollo y la ejecución (transformándose en ocasiones de uno en la otra).\n De otra parte, ya que la compilación implica una traducción a un formato más amigable con la máquina, los programas interpretados corren más lentamente y menos eficientemente (es decir, gastan considerablemente más energía).\n Esto es especialmente verdad para los lenguajes de guion, cuyas sentencias son más complejas de analizar comparadas con las instrucciones máquina.\n Muchos lenguajes se han implementado usando tanto compiladores como intérpretes, incluyendo BASIC, C, Lisp, Pascal y Python. Java y C# se compilan a código byte, el lenguaje interpretado específico para la máquina virtual.\n Muchas implementaciones de Lisp pueden mezclar libremente código interpretado y compilado. "
archivo_de_texto.write(texto_en_memoria);
archivo_de_texto.close();
nuevo(1);
#################################################################
#IO_ext Ej_02 ;
print(" salida de datos a otro archivo append");
archivo_de_texto=open("text.txt","a")#						abre el archivo text.txt para agregar datos
linea_texto_en_memoria="\n fuente wikipedia : https://es.wikipedia.org/wiki/Int%C3%A9rprete_(inform%C3%A1tica)#Eficiencia"
archivo_de_texto.write(linea_texto_en_memoria);
archivo_de_texto.close();
nuevo(2);
#################################################################
#IO_ext Ej_03 ;
print("ingreso lectura de bloque de datos desde otro archivo read");
archivo_de_texto=open("text.txt","r")#						abre el archivo text.txt para lectura en bloque
texto_a_memoria=archivo_de_texto.read();
print(texto_a_memoria);
archivo_de_texto.close();
nuevo(3);
#################################################################
#IO_ext Ej_04 ;
print("ingreso lectura por lineas de datos desde otro archivo readlines");
archivo_de_texto=open("text.txt","r")#						abre el archivo text.txt para lectura en lineas
linea_texto_a_memoria=archivo_de_texto.readlines();
print(linea_texto_a_memoria[2]);
archivo_de_texto.close();
nuevo(4);
#################################################################
#IO_ext Ej_05 ;
####################                  BINARIOS "binario.dat"
print("""
╔═════════════════════════════════════════════════════════════════════════════╗ 
║                                                                             ║
║                       BINARIOS 'binario.dat'                                ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
import pickle


binario_en_memoria="PICKLE\nLenguaje interpretado\n Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.\n El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina.\n Los términos lenguaje interpretado y lenguaje compilado4​ no están bien definidos porque, en teoría, cualquier lenguaje de programación puede ser interpretado o compilado.\n Cada vez es más popular, en las implementaciones más modernas de un lenguaje de programación, ofrecer ambas opciones.\n Los lenguajes interpretados también pueden diferenciarse de los lenguajes de máquina.\n Funcionalmente, tanto la ejecución y la interpretación significan lo mismo -obtener la siguiente instrucción/sentencia del programa y su ejecución-.\n Aunque el bytecode (código byte) interpretado es además idéntico a su forma en código máquina y tiene una representación en ensamblador, el término 'interpretado' se reserva en la práctica para lenguajes 'procesados por software' (como las máquinas virtuales o emuladores) por encima del procesado nativo (por ejemplo, por hardware).\n En principio, los programas de muchos lenguajes se pueden compilar o interpretar, emular o ejecutar nativamente, así que esta designación se aplica solamente a la implementación práctica más usual, en vez de representar una propiedad esencial del lenguaje.\n De forma parecida al microcódigo del procesador, muchos intérpretes, internamente recaen en una compilación en tiempo de ejecución.\n Evitando la compilación, los programas interpretados son más fáciles de evolucionar durante el desarrollo y la ejecución (transformándose en ocasiones de uno en la otra).\n De otra parte, ya que la compilación implica una traducción a un formato más amigable con la máquina, los programas interpretados corren más lentamente y menos eficientemente (es decir, gastan considerablemente más energía).\n Esto es especialmente verdad para los lenguajes de guion, cuyas sentencias son más complejas de analizar comparadas con las instrucciones máquina.\n Muchos lenguajes se han implementado usando tanto compiladores como intérpretes, incluyendo BASIC, C, Lisp, Pascal y Python. Java y C# se compilan a código byte, el lenguaje interpretado específico para la máquina virtual.\n Muchas implementaciones de Lisp pueden mezclar libremente código interpretado y compilado. "
print("salida de datos a otro archivo binario write wr ");
from io import *
archivo_de_binario=open("binario.dat","wb")#				abre el archivo binario para escritura y si no existe lo crea
pickle.dump(binario_en_memoria,archivo_de_binario);
archivo_de_binario.close();
del archivo_de_binario
nuevo(5);
#################################################################
#IO_ext Ej_06;
print("Ingreso lectura de bloque de datos desde otro archivo binario read - rw");
archivo_de_binario=open("binario.dat","rb")#				abre el archivo binario para lectura en bloque
binario_a_memoria=pickle.load(archivo_de_binario);
print(binario_a_memoria);
archivo_de_binario.close();
del archivo_de_binario
nuevo(6);
#################################################################
#IO_ext Ej_07;
print("Ingreso lectura por lineas de datos desde otro archivo binario readlines");
archivo_de_binario=open("binario.dat","rb")#				abre el archivo binario para lectura en lineas
linea_binario_a_memoria=archivo_de_binario.readlines();
print(linea_binario_a_memoria[5]);
archivo_de_binario.close();
del archivo_de_binario
nuevo(7);
#################################################################
#IO_ext Ej_08;
####################                  JSON (JavaScript Object Notation)."binario.dat"
print("""
╔═════════════════════════════════════════════════════════════════════════════╗ 
║                                                                             ║
║                          JSON (JavaScript Object Notation).                 ║
║                                                                             ║
║                          JSON                 Python                        ║
║                          -----                ------                        ║
║                          object                dict                         ║
║                          array                 list                         ║
║                          string                unicode                      ║
║                          number (int)          int, long                    ║
║                          number (real)         float                        ║
║                          true                  True                         ║
║                          false                 False                        ║
║                          null                  None                         ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
import json




json_en_memoria="JSON\nLenguaje interpretado\n Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.\n El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina.\n Los términos lenguaje interpretado y lenguaje compilado4​ no están bien definidos porque, en teoría, cualquier lenguaje de programación puede ser interpretado o compilado.\n Cada vez es más popular, en las implementaciones más modernas de un lenguaje de programación, ofrecer ambas opciones.\n Los lenguajes interpretados también pueden diferenciarse de los lenguajes de máquina.\n Funcionalmente, tanto la ejecución y la interpretación significan lo mismo -obtener la siguiente instrucción/sentencia del programa y su ejecución-.\n Aunque el bytecode (código byte) interpretado es además idéntico a su forma en código máquina y tiene una representación en ensamblador, el término 'interpretado' se reserva en la práctica para lenguajes 'procesados por software' (como las máquinas virtuales o emuladores) por encima del procesado nativo (por ejemplo, por hardware).\n En principio, los programas de muchos lenguajes se pueden compilar o interpretar, emular o ejecutar nativamente, así que esta designación se aplica solamente a la implementación práctica más usual, en vez de representar una propiedad esencial del lenguaje.\n De forma parecida al microcódigo del procesador, muchos intérpretes, internamente recaen en una compilación en tiempo de ejecución.\n Evitando la compilación, los programas interpretados son más fáciles de evolucionar durante el desarrollo y la ejecución (transformándose en ocasiones de uno en la otra).\n De otra parte, ya que la compilación implica una traducción a un formato más amigable con la máquina, los programas interpretados corren más lentamente y menos eficientemente (es decir, gastan considerablemente más energía).\n Esto es especialmente verdad para los lenguajes de guion, cuyas sentencias son más complejas de analizar comparadas con las instrucciones máquina.\n Muchos lenguajes se han implementado usando tanto compiladores como intérpretes, incluyendo BASIC, C, Lisp, Pascal y Python. Java y C# se compilan a código byte, el lenguaje interpretado específico para la máquina virtual.\n Muchas implementaciones de Lisp pueden mezclar libremente código interpretado y compilado. "
print("salida de datos a otro archivo JavaScript_Object_Notation write wr ");
from io import *
archivo_de_json=open("JavaScript_Object_Notation.json","w")#		abre el archivo JavaScript_Object_Notation para escritura y si no existe lo crea
json.dump(json_en_memoria,archivo_de_json);
archivo_de_json.close();
del archivo_de_json
nuevo(7);
#################################################################
#IO_ext Ej_08;
print("Ingreso lectura de bloque de datos desde otro archivo JavaScript_Object_Notation read - rw");
archivo_de_json=open("JavaScript_Object_Notation.json","r")#		abre el archivo JavaScript_Object_Notation para lectura en bloque
json_en_memoria=json.load(archivo_de_json);
print(json_en_memoria);
archivo_de_json.close();
del archivo_de_json
nuevo(7);
#################################################################
#IO_ext Ej_08;
print("""
╔═════════════════════════════════════════════════════════════════════════════╗ 
║                                                                             ║
║                       metodo 'WITH' BINARIOS pickle                         ║
║                      --------------------------------                       ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
import pickle



print("Salida de datos con metodo WITH a otro archivo binario write wr ");
binario_en_memoria2="PICKLE_WITH\nLenguaje interpretado\n Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.\n El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina.\n Los términos lenguaje interpretado y lenguaje compilado4​ no están bien definidos porque, en teoría, cualquier lenguaje de programación puede ser interpretado o compilado.\n Cada vez es más popular, en las implementaciones más modernas de un lenguaje de programación, ofrecer ambas opciones.\n Los lenguajes interpretados también pueden diferenciarse de los lenguajes de máquina.\n Funcionalmente, tanto la ejecución y la interpretación significan lo mismo -obtener la siguiente instrucción/sentencia del programa y su ejecución-.\n Aunque el bytecode (código byte) interpretado es además idéntico a su forma en código máquina y tiene una representación en ensamblador, el término 'interpretado' se reserva en la práctica para lenguajes 'procesados por software' (como las máquinas virtuales o emuladores) por encima del procesado nativo (por ejemplo, por hardware).\n En principio, los programas de muchos lenguajes se pueden compilar o interpretar, emular o ejecutar nativamente, así que esta designación se aplica solamente a la implementación práctica más usual, en vez de representar una propiedad esencial del lenguaje.\n De forma parecida al microcódigo del procesador, muchos intérpretes, internamente recaen en una compilación en tiempo de ejecución.\n Evitando la compilación, los programas interpretados son más fáciles de evolucionar durante el desarrollo y la ejecución (transformándose en ocasiones de uno en la otra).\n De otra parte, ya que la compilación implica una traducción a un formato más amigable con la máquina, los programas interpretados corren más lentamente y menos eficientemente (es decir, gastan considerablemente más energía).\n Esto es especialmente verdad para los lenguajes de guion, cuyas sentencias son más complejas de analizar comparadas con las instrucciones máquina.\n Muchos lenguajes se han implementado usando tanto compiladores como intérpretes, incluyendo BASIC, C, Lisp, Pascal y Python. Java y C# se compilan a código byte, el lenguaje interpretado específico para la máquina virtual.\n Muchas implementaciones de Lisp pueden mezclar libremente código interpretado y compilado. "
with open("binario_metodo_with.dat","wb") as write_file:#			abre el archivo binario para escritura y si no existe lo crea
	pickle.dump(binario_en_memoria2, write_file, pickle.HIGHEST_PROTOCOL)
nuevo(7);
#################################################################
#IO_ext Ej_08;
print("Ingreso lectura de bloque de datos con metodo WITH desde otro archivo binario read - rw");
with open("binario_metodo_with.dat", "rb") as read_file:#			abre el archivo binario para lectura en bloque  
    binario_a_memoria2 = pickle.load(read_file)
print(binario_a_memoria2);
nuevo(7);
#################################################################
#IO_ext Ej_08;

print("""
╔═════════════════════════════════════════════════════════════════════════════╗ 
║                                                                             ║
║                   metodo 'WITH' JSON (JavaScript Object Notation).          ║
║                  --------------------------------------------------         ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");


import json



json_en_memoria2="JSON_WITH\nLenguaje interpretado\n Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.\n El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina.\n Los términos lenguaje interpretado y lenguaje compilado4​ no están bien definidos porque, en teoría, cualquier lenguaje de programación puede ser interpretado o compilado.\n Cada vez es más popular, en las implementaciones más modernas de un lenguaje de programación, ofrecer ambas opciones.\n Los lenguajes interpretados también pueden diferenciarse de los lenguajes de máquina.\n Funcionalmente, tanto la ejecución y la interpretación significan lo mismo -obtener la siguiente instrucción/sentencia del programa y su ejecución-.\n Aunque el bytecode (código byte) interpretado es además idéntico a su forma en código máquina y tiene una representación en ensamblador, el término 'interpretado' se reserva en la práctica para lenguajes 'procesados por software' (como las máquinas virtuales o emuladores) por encima del procesado nativo (por ejemplo, por hardware).\n En principio, los programas de muchos lenguajes se pueden compilar o interpretar, emular o ejecutar nativamente, así que esta designación se aplica solamente a la implementación práctica más usual, en vez de representar una propiedad esencial del lenguaje.\n De forma parecida al microcódigo del procesador, muchos intérpretes, internamente recaen en una compilación en tiempo de ejecución.\n Evitando la compilación, los programas interpretados son más fáciles de evolucionar durante el desarrollo y la ejecución (transformándose en ocasiones de uno en la otra).\n De otra parte, ya que la compilación implica una traducción a un formato más amigable con la máquina, los programas interpretados corren más lentamente y menos eficientemente (es decir, gastan considerablemente más energía).\n Esto es especialmente verdad para los lenguajes de guion, cuyas sentencias son más complejas de analizar comparadas con las instrucciones máquina.\n Muchos lenguajes se han implementado usando tanto compiladores como intérpretes, incluyendo BASIC, C, Lisp, Pascal y Python. Java y C# se compilan a código byte, el lenguaje interpretado específico para la máquina virtual.\n Muchas implementaciones de Lisp pueden mezclar libremente código interpretado y compilado. "
print("salida de datos con metodo WITH  a otro archivo JavaScript_Object_Notation write wr ");
with open("JavaScript_Object_Notation_with.json", "w") as write_file:# abre el archivo JavaScript_Object_Notation para escritura y si no existe lo crea
	json.dump(json_en_memoria2, write_file)
nuevo(7);
#################################################################
#IO_ext Ej_08;
print("Ingreso lectura de bloque de datos con metodo WITH  desde otro archivo JavaScript_Object_Notation read - rw");
with open("JavaScript_Object_Notation_with.json","r") as read_file:# abre el archivo JavaScript_Object_Notation para lectura en bloque
	json_en_memoria2 = json.load(read_file);
print(json_en_memoria2);
nuevo(7,"fin");
#################################################################


