from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass

limpiar();
#################################################################
#Clase_Print_01 
print ("linea 1");
print ("linea 2");
print ("linea 3");
print ("--------");
print ()
print ("c:\nicolas");
print (r"c:\nicolas");
print ("c:\\nicolas");
nuevo(1);
#################################################################
#Clase_Print_02
def ej_02():
	print ("\nlinea 1");
	print ("linea 2");
	print ("linea 3");
	print ("--------");
ej_02() #llamada a la funcion
ej_02() #llamada a la funcion
ej_02() #llamada a la funcion
nuevo(2);
#################################################################
#Clase_Print_03
cadena = "es hora de Segundo Apellidojar grupo 2019-UTN"
print ("La Cadena original es : ", cadena);
print(input("continuar?"));
print(" print ('cadena',end=''); el, end=' ' genera que al final no se genere un final de linea por lo que siguiente printe sera seguido")
print ("La Cadena original es : ", cadena, end="");
print (cadena);
print(input("continuar?"));
# multiples lineas 
print ("# multiples lineas ")
cadena2 = '''...Es hora
            de Segundo Apellidojar grupo 2019
            ...UTN...'''
print("Cadena 2 multilinea ", end="");
print(cadena2);
print(input("continuar?"));
print ("La Cadena original es : ", cadena, "");
# Impresion del primir caracter 
print("El primer caracter de la Cadena es: ", end="");
print(cadena[0]);
# Impresion del ultimo caracter 
print("El ultimo caracter de la Cadena es: ", end="");
print(cadena[-1]);
# Impresion del 3er al 12do caracter 
print("Sector de la cadena ubicada entre los caracteres 3-19: ", end="");
print(cadena[3:19]);
print(input("continuar?"));
print ("Rellena con 0 en un sector de 40 caracteres");
print(cadena.zfill(40)) 
# Impresion del Cadena alinecion centrada
print ("Alinecion en un sector de 40 caracteres");
print ("Alinecion centrada de la Cadena : ", end="");
print (cadena.center(40), "");
# Impresion del Cadena alinecion centrada con numerales
print ("Alinecion centrada con agregando #: ", end="");
print (cadena.center(40, '#'));
print(input("continuar?"));
# Impresion del Cadena alinecion izquierda
print ("Alinecion izquierda de la Cadena : ", end="");
print (cadena.ljust(40), "");
# Impresion del Cadena alinecion izquierda con numerales
print ("Alinecion izquierda de la Cadena adregando #: ", end="");
print (cadena.ljust(40, '#'));
print(input("continuar?"));
# Impresion del Cadena alinecion derecha
print ("Alinecion derecha de la Cadena : ", end="");
print (cadena.rjust(40), "");
# Impresion del Cadena alinecion derecha con numerales
print ("Alinecion derecha de la Cadena adregando #: ", end="");
print (cadena.rjust(40, '#'));
nuevo(2);
#################################################################
#Clase_Print_03
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║      Unidad 1 -¿Qué es Python?                                              ║
║            * Instalación y configuración                                    ║
║            * Errores sintácticos y lógicos                                  ║
║            * Programación secuencial                                        ║
║            * Estructuras condicionales simples, compuestas y anidadas       ║
║            * Estructuras repetitivas                                        ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                    Amigarse - nomenclatura                                  ║
║                                                                             ║
║     Estilos*      Cod. ANSI     ||  Colores   Texto   Fondo                 ║
║     Sin efecto      0           ||   Negro      30      40                  ║
║     Negrita         1           ||   Blanco     37      47                  ║
║     Débil           2           ||   Amarillo   33      43                  ║
║     Cursiva         3           ||   Azul       34      44                  ║
║     Subrayado       4           ||   Rojo       31      41                  ║
║     Inverso         5           ||   Verde      32      42                  ║
║     Oculto          6           ||   Morado     35      45                  ║
║     Tachado         7           ||   Cian       36      46                  ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                        VER EN UNA MAQUINA EN LINUX                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");

limpiar()


#\033[cod_formato;cod_color_texto;cod_color_fondom
print("https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html")
print(chr(27)+"[1;33m"+"Texto en negrita de color amarillo") 
print("\x1b[1;33m"+"Texto en negrita de color amarillo") 
print("\033[4;35m"+"Texto en negrita y subrayado de color morado") 
print("\033[4;35m"+"Texto en negrita y subrayado de color morado")
print ("Cambios de formato añadiendo uno nuevo al final de cada línea:")
print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
print("\033[1;33m"+"Texto en negrita color amarillo"+'\033[0;m') 
print("\033[;36m"+"Texto normal de color cian")
print("\033[4;35;47m"+"Texto subr morado sobre blanco"+'\033[0;m') 
print("\033[4;35m"+"Texto normal subr color morado"+'\033[0;m')
print ("\n\ntabla con todos los formatos posibles, recorriendo y cambiando estilos y colores:")
def construye_tabla_formatos():
    for estilo in range(8):
        for color_texto    in range(30,38):
            cad_cod = ''
            for color_fondo    in range(40,48): 
                fmto = ';'.join([str(estilo), 
                                 str(color_texto   ),
                                 str(color_fondo   )]) 
                cad_cod+="\033["+fmto+"m "+fmto+" \033[0m" 
            print(cad_cod)
        print('\n')
construye_tabla_formatos()
nuevo(3);
#################################################################
#Clase_Print_04
def ej001_4():
	var_entera_1 = 5
	var_entera_2 = 3
	var_entera_3 = 4
	print (var_entera_1);
	print (var_entera_2);
	print (var_entera_3);
	print (var_entera_1*var_entera_3-var_entera_2);
	print ((var_entera_1*var_entera_3+1)/var_entera_2);
nuevo(4);
#################################################################
#Clase_Print_05
def ej001_5(var_entera_1,var_entera_2,var_entera_3):
	print ("var_entera_1 = "+ str(var_entera_1));
	print ("var_entera_2 = "+ str(var_entera_2));
	print ("var_entera_3 = "+ str(var_entera_3));
	print ("operacion N 1 = "+ str(var_entera_1*var_entera_3-var_entera_2));
	print ("operacion N 2 = "+ str((var_entera_1*var_entera_3+1)/var_entera_2));
ej001_5(4,5,6) #llamada a la funcion
nuevo(5);
#################################################################
#Clase_Print_06
var_entera_1 = 4
var_entera_2 = 5
var_entera_3 = 6
print ("var_entera_1 = "+ str(var_entera_1));
print ("var_entera_2 = "+ str(var_entera_2));
print ("var_entera_3 = "+ str(var_entera_3));
def ej001_6(var_entera_1_2,var_entera_2_2,var_entera_3_2):
	respuesta1 =(var_entera_1_2*var_entera_3_2-var_entera_2_2);
	respuesta2 = ((var_entera_1_2*var_entera_3_2+1)/var_entera_2_2);
	return respuesta1

operacion_N1 = ej001_6(var_entera_1,var_entera_2,var_entera_3) #llamada a la funcion 
print ("operacion N 1 = "+ str(operacion_N1));
nuevo(6);
#################################################################
#Clase_Print_07
var_entera_1 = 4.5
var_entera_2 = 5.5
var_entera_3 = 6.5
print(f"var_entera_1 = {var_entera_1}");
print(f"var_entera_2 = {var_entera_2}");
print(f"var_entera_3 = {var_entera_3}");
def ej001_7(var_entera_1_2,var_entera_2_2,var_entera_3_2):
	respuesta1 =(var_entera_1_2*var_entera_3_2-var_entera_2_2);
	respuesta2 = ((var_entera_1_2*var_entera_3_2+1)/var_entera_2_2);
	return respuesta1
print ("llamo a una funcion que devuelve un resultado que imprimo")
print ("operacion N 1 = "+ str(ej001_7(var_entera_1,var_entera_2,var_entera_3)))
print ("operacion N 1 = "+ str(operacion_N1));
print("largo de la cadena :"+str(len(str(operacion_N1))));
nuevo(7);
#################################################################
#Clase_Print_08
print ("Solos");
print ("llamada a la funcion cambiando el orden de las variables en el llamado luego en la definicion");
nuevo(8);
#################################################################
#Clase_Print_09
print ("Solos");
print ("llamada a la funcion para que la devolucion sea la respuesta 2");
nuevo(9);
#################################################################
#Clase_Print_10
print("leer\nhttp://pyspanishdoc.sourceforge.net/lib/string-methods.html");
texto_en_memoria=" Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina. El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina. "
print(texto_en_memoria);
print("---------------------------------------------------------------------");
print("Upper : "+str(texto_en_memoria.upper()));
print("---------------------------------------------------------------------");
print("lower : "+str(texto_en_memoria.lower()));
print("---------------------------------------------------------------------");
print("capitalize : "+str(texto_en_memoria.capitalize()));
print("---------------------------------------------------------------------");
caracter_buscado="i"
contador_caracter_buscado=texto_en_memoria.count(caracter_buscado);
print("Cantidad de caracteres "+str(caracter_buscado)+" : "+str(contador_caracter_buscado));
print("---------------------------------------------------------------------");
print(texto_en_memoria);
print("---------------------------------------------------------------------");
print("split : "+str(texto_en_memoria.split()));
print("---------------------------------------------------------------------");
print("strip : "+str(texto_en_memoria.strip("un")));
print("---------------------------------------------------------------------");
print("replace : "+str(texto_en_memoria.replace("lenguaje", "l.de alto nivel")));
print("---------------------------------------------------------------------");
texto_buscado="lenguaje"
contador_texto_buscado_izq=texto_en_memoria.find(texto_buscado);
print("Cantidad de caracteres en texto buscado desde la izquierda "+str(caracter_buscado)+" : "+str(contador_texto_buscado_izq));
contador_texto_buscado_der=texto_en_memoria.rfind(texto_buscado);
print("Cantidad de caracteres en texto buscado desde la derecha  "+str(caracter_buscado)+" : "+str(contador_texto_buscado_der));
nuevo(10);
#################################################################
#Clase_Print_11
nombre = "Name"
apellido=["APELLIDO","Apellido_2"]
edad = 13
print ("Formateo de string con objetos dentro")
print ("Hola {name} se que tenes {age} años.".format(name=nombre, age=edad))
print ("Hola {} se que tenes {} años.".format(nombre, edad))
print (f"Hola {nombre} se que tenes {edad} años.") 
nuevo(11);
#################################################################
#Clase_Print_12
print ("Formateo de string con objetos y funciones dentro")
nombre = "Name"
apellido=["APELLIDO","Apellido_2"]
edad = 13
barrio="LOURDES"
apellido1="APELLIDO"
apellido2="Apellido_2"
print (" Uso de objeto.upper(), .lower() .capitalize() en un string ")
print (f"Hola {nombre.upper()} se que vivis en {barrio.lower()}, que cumpliras {int(edad)+1} años.")
print (f"{nombre.upper()} tus apellidos son {apellido[0].capitalize()} y {apellido[1].capitalize()} se que vivis en {barrio.lower()}")
nuevo(12);
#################################################################
#Clase_Print_13
print (" Uso de objeto.swapcase(), .title() en un string ")
cadena_de_datos=" Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina. El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina."
print("swapcase() :- invierte minusculas por mayosculas y viceversa")
# Coverting string into its swapped case 
print("Cadena_de_datos :\n"+cadena_de_datos.swapcase()); 
print("title() :- coloca cada letra despues de un espacio en mayuscula, el resto en minuscula")  
print("Cadena_de_datos :\n"+cadena_de_datos.title()); 
nuevo(13);
#################################################################
#Clase_Print_14
print ("uso de libreria # datetime ")
import datetime 
fecha = datetime.datetime.today() 
print(f"hoy es {fecha:%d %B, %Y}") 
nuevo(14);
#################################################################
#Clase_Print_15
print (f"En {nombre} el caracter mas bajo es :"+(min(nombre))); 
print (f"En {nombre} el caracter mas alto es :"+(max(nombre))); 
nuevo(15);
#################################################################
#Clase_Print_16);
print (" Uso de objeto.split(), .rsplit() .join() .rstrip() .lstrip() en un string ")
print ("split convierte una cadena de texto en una lista. Por defecto al separarse por espacios, los elementos de dicha lista serán las palabras de la cadena.")
print ("join convierte una lista en una cadena formada por los elementos de la lista separados por comas.")
gracia= "Ariel Garcia"
print ("split divido-fracciono-separo una cadena dependiendo del caracter bucado")
print(gracia.split( ))# divido en un espacios
print ("split divido-fracciono-separo al encontrar 'a'")
print(gracia.rsplit('a'))# divido despues 'a'
print ("split divido-fracciono-separo al encontrar la 2da'a' ")
print(gracia.split('a', 2))# divido despues del limite de 1 'a'
print ("rsplit() divido-fracciono-separo una cadena dependiendo del caracter bucado de DERECHA a izq")
print ("rsplit divido-fracciono-separo al encontrar la 2da'a' de derecha a iz")
print(gracia.rsplit('a', 2))# divido despues del limite de 2 'a'
resultado=gracia.split()# divido en un espacios
print ("lista original :"+str(resultado))
print ("Join - genero una cadena de caracteres a una lista' ")
lista =",".join(resultado)
print ("Join -"+lista)
print ("rpartition convierte una lista en una cadena a partir de una cadena de corte.")
busqueda="cia"
print("Busqueda :"+busqueda+" en "+gracia+"  :",end= " ")
print(gracia.rpartition(busqueda)) 
print ("lstrip corta de una cadena la parte buscada de izquierda a derecha.")
busqueda="Fac"
print("Busqueda :"+busqueda+" en "+gracia+"  :",end= " ")
print(gracia.lstrip('Fac')) 
print ("rstrip corta de una cadena la parte buscada de derecha a izquierda.")
busqueda="ti"
print("Busqueda :"+busqueda+" en "+gracia+"  :",end= " ")
print(gracia.rstrip('busqueda')) 
nuevo(16);
#################################################################
#Clase_Print_17
print (" Uso de objeto.rfind(), .find()  en un string ")
cadena_de_datos=" Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina. El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina."
busqueda = "lenguaje"
print("cadena_de_datos : \n"+cadena_de_datos);
print("busqueda : "+busqueda);
# using find() to find first occurrence of busqueda 
print ("Primer encuentro (desde la izquierda) Caracter nº: ", end="") 
print (cadena_de_datos.find( busqueda, 4) ) 
# using rfind() to find last occurrence of busqueda 
print ("Primer encuentro (desde la derecha) o ultimo Caracter nº: ", end="") 
print ( cadena_de_datos.rfind( busqueda, 4) ) 
nuevo(17);
#################################################################
#Clase_Print_18;
print (" Uso de objeto.isupper(), .islower() .isspace() .rstrip() .lstrip() en un string ")
string = input("Escriba una palabra  :")
if string.isupper() == True:
	print ("todo mayusculas")
elif string.islower() == True:
	print ("todo minusculas")
elif string.isspace():
	print ("espacio en blanco")
else:
	print ("mezclado")
nuevo(18);
#################################################################
#Clase_Print_19
print (" Uso de objeto.isupper(), .islower() .isspace() .rstrip() .lstrip() en un string ")
cadena_de_datos="abcdefg1234567890hijk"
print("cadena_de_datos : "+cadena_de_datos);
print("isalnum - es alfanumerica :"+str(cadena_de_datos.isalnum()));

cadena_de_datos="ab cd efg123 456789 0hijk"
print("cadena_de_datos : "+cadena_de_datos);
print("isalnum - es alfanumerica :"+str(cadena_de_datos.isalnum()));
print (" Uso de objeto.isupper(), .islower() .isspace() .rstrip() .lstrip() en un string ")
print(gracia.casefold());
nuevo(20);
#################################################################

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                 format_map                                  ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")

cadena = 'Empleado {Nombre} esta en la empresa como {Trabajo}'
Nombre_diccionario_1 = {'Nombre': 'Juan X', 'Trabajo': 'Programador'}

print(cadena.format_map(Nombre_diccionario_1))
print(cadena.format(**Nombre_diccionario_1))
nuevo(21,"fin");
#################################################################

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                   pprint                                    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://docs.python.org/3/library/pprint.html
The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter. If the formatted structures include objects which are not fundamental Python types, the representation may not be loadable. This may be the case if objects such as files, sockets or classes are included, as well as many other objects which are not representable as Python literals.
The formatted representation keeps objects on a single line if it can, and breaks them onto multiple lines if they don’t fit within the allowed width. Construct PrettyPrinter objects explicitly if you need to adjust the width constraint.
Dictionaries are sorted by key before the display is computed.
The pprint module defines one class:
class pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False)
    Construct a PrettyPrinter instance. This constructor understands several keyword parameters. An output stream may be set using the stream keyword; the only method used on the stream object is the file protocol’s write() method. If not specified, the PrettyPrinter adopts sys.stdout. The amount of indentation added for each recursive level is specified by indent; the default is one. Other values can cause output to look a little odd, but can make nesting easier to spot. The number of levels which may be printed is controlled by depth; if the data structure being printed is too deep, the next contained level is replaced by .... By default, there is no constraint on the depth of the objects being formatted. The desired output width is constrained using the width parameter; the default is 80 characters. If a structure cannot be formatted within the constrained width, a best effort will be made. If compact is false (the default) each item of a long sequence will be formatted on a separate line. If compact is true, as many items as will fit within the width will be formatted on each output line.
    Changed in version 3.4: Added the compact parameter.
""")
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)

tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)

print("""
pprint.pformat(object, indent=1, width=80, depth=None, *, compact=False)
    Return the formatted representation of object as a string. indent, width, depth and compact will be passed to the PrettyPrinter constructor as formatting parameters.
    Changed in version 3.4: Added the compact parameter.
pprint.pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False)
    Prints the formatted representation of object on stream, followed by a newline. If stream is None, sys.stdout is used. This may be used in the interactive interpreter instead of the print() function for inspecting values (you can even reassign print = pprint.pprint for use within a scope). indent, width, depth and compact will be passed to the PrettyPrinter constructor as formatting parameters.
    Changed in version 3.4: Added the compact parameter.
""")
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff)
pprint.pprint(stuff)
print("""
pprint.isreadable(object)
    Determine if the formatted representation of object is “readable,” or can be used to reconstruct the value using eval(). This always returns False for recursive objects.
""")
pprint.isreadable(stuff)
print("""
pprint.isrecursive(object)
    Determine if object requires a recursive representation.
One more support function is also defined:
pprint.saferepr(object)
    Return a string representation of object, protected against recursive data structures. If the representation of object exposes a recursive entry, the recursive reference will be represented as <Recursion on typename with id=number>. The representation is not otherwise formatted.
pprint.isrecursive(object)
    Determine if object requires a recursive representation.
One more support function is also defined:
pprint.saferepr(object)
    Return a string representation of object, protected against recursive data structures. If the representation of object exposes a recursive entry, the recursive reference will be represented as <Recursion on typename with id=number>. The representation is not otherwise formatted.
""")
pprint.saferepr(stuff)

