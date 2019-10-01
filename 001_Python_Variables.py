from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║      Unidad 2 - Variables, Listas                                           ║
║            * Tipos de variables                                             ║
║            * Procesamiento de cadenas                                       ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                                                             ║
║                                    Variables                                ║
║                            -----------------------                          ║
║                                                                             ║
║                            Crear archivos con extencion                     ║
║                                                        .py                  ║
║                                                        .pyc                 ║
║                                                        .c                   ║
║                                                                             ║
║                    and, as, assert, break, class, continue                  ║
║                    def, del, elif, else, except, exec                       ║
║                    finally, for, from, global, if, import                   ║
║                    in, is, lambda, nonlocal, not, or                        ║
║                    pass, raise, return, try, while, with                    ║
║                    yield, True, False, None                                 ║
║                                                                             ║
║                           tipos de variables                                ║
║                                               Mutable                       ║
║                                               Inmutable                     ║
║                                                                             ║
║                                               string                        ║
║                                               float                         ║
║                                               Intenger                      ║
║                                               long...                       ║
║                                                                             ║
║                 espacio en memoria                                          ║
║                                                                             ║
║                 limites de entrega del valor                                ║
║                                     locales                                 ║
║                                     nonlocal                                ║
║                                     globales                                ║
║                                                                             ║
║                 escribir un texto                                           ║
║                                                                             ║
║                 texto desde una variable                                    ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
limpiar();
print("""
Mutable: su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.");
Inmutable: su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.\n");
\n");
Categoría de tipo________Nombre______Descripción");
Números inmutables_______int_________entero");
_________________________long________entero largo");
_________________________float_______coma flotante");
_________________________complex_____complejo");
_________________________bool________booleano True / False");
Secuencias inmutables____str_________cadena de caracteres");
_________________________unicode_____cadena de caracteres Unicode");
_________________________tuple_______tupla");
_________________________xrange______rango inmutable");
Secuencias mutables______list________lista");
_________________________range_______rango mutable");
Mapeosprint______________dict________diccionario");
Conjuntos mutables_______set_________conjunto mutable");
Conjuntos inmutables_____frozenset___Conjunto inmutable");

\nhttp://docs.python.org.ar/tutorial/3/classes.html");
\n Objeto, es su materialización de algo incluso un dato");
\n Clase, es el razonamiento abstracto de un objeto");
\n Instanciar, es crear objetos desde una clase");
\n Las clases en este contexto permiten definir los atributos y el comportamiento, mediante métodos, de los objetos de un programa. Una clase es una especie de plantilla o prototipo que se utiliza para crear instancias individuales del mismo tipo de objeto.");
\n Los atributos definen las características propias del objeto y modifican su estado. Son datos asociados a las clases y a los objetos creados a partir de ellas.");
\n De ello, se deducen los dos tipos de atributos o de variables existentes: variables de clase y variables de instancia (objetos).");
\n Los métodos son bloques de código (o funciones) de una clase que se utilizan para definir el comportamiento de los objetos.");
\n Tanto para acceder a los atributos como para llamar a los métodos se utiliza el método denominado de notación de punto que se basa en escribir el nombre del objeto o de la clase seguido de un punto y el nombre del atributo o del método con los argumentos que procedan: clase.atributo, objeto.atributo, objeto.método([argumentos]).");
\n
\n Una variable de clase es compartida por todas las instancias de una clase. Se definen dentro de la clase (después del encabezado de la clase) pero nunca dentro de un método. Este tipo de variables no se utilizan con tanta frecuencia como las variables de instancia.");
\n Una variable de instancia se define dentro de un método y pertenece a un objeto determinado de la clase instanciada.
""");
nuevo(0,"inicio");
#################################################################
#Clase_Variables_01 
print("  *String - Cadenas puede incorporar en cualquiera de los dos comillas simples (') o comillas dobles (\") o para multiplas lineas se usan comillas triples de cada una (''' o """);
cadena=('''"http://docs.python.org.ar/tutorial/3/classes.html"\n"https://www.python.org/downloads/"\n"https://python-para-impacientes.blogspot.com/2016/02/variables-de-control-en-tkinter.html"\n"https://pythones.net/instalando-python-3-que-es-un-ide/")''');
print (cadena);
cadena=("""'http://docs.python.org.ar/tutorial/3/classes.html"\n"https://www.python.org/downloads/"\n"https://python-para-impacientes.blogspot.com/2016/02/variables-de-control-en-tkinter.html"\n"https://pythones.net/instalando-python-3-que-es-un-ide/")'""");
print (cadena);
cadena=("Hola, todo el mundo!");
print (type(cadena),cadena);
cadena=('Hola, todo el mundo!');
print (type(cadena),cadena);
cadena=("17");print (type(cadena),cadena);
cadena=(17);print (type(cadena),cadena);
cadena=(3.2);print (type(cadena),int(cadena));
print (input("Fin continuar?"));
print("  *String - Cadenas con doble comillas pueden incluir  comilla simple dentro o viceversa");
cadena='UTN\n 2019'
print (cadena);
cadena=("UTN 2019")
print (cadena);
cadena='"hola" como va todo'
print (cadena);
cadena="'hola' como va todo"
print (cadena);
cadena='"hola" como va todo'
print (cadena);
print("  *String - Cadenas pueden tener (en ingles por ejemplo) 'detras de una letra por lo que hay que salbarla con '\'");
cadena='Cat\'s plate'
print (cadena);
cadena='It s\'nt a problem'
print (cadena);
print (3*"UTN 2019")
variable="UTN 2019"
print (variable)
print (variable[2])
print (variable[:4])
print (variable[4:])
print (variable[2:6])

a, b, c = 1, 2.8, "3"
print ('a, b, c = 1, 2.8, "3"')
print ("a = "+str(a),type(a))
print ("b = "+str(b),type(b))
print ("c = "+str(c),type(c))
print ("#--------------------------------")
variable1,variable2="UTN "," 2019"
print (variable1+variable2)
print (variable2)
print (variable1)
print (variable2+variable1)
nuevo(1);
#################################################################
#Clase_Variables_02 
var = "xxx"
def funcion_ej_000_V_3():
	var = "yyy"
	print(var);
funcion_ej_000_V_3();
print(var);
#--------------------------------
print("Ingrese datos alfa, numericos y mixtos")
for i in range (3):
	print("#--------------------------------");
	var_a = input("variable A:")
	var_b = input("variable B:")
	print ("variable a: "+var_a)
	print ("variable b: "+var_b)
	print ("variable a+b"+(var_a+var_b))
	print ("variable a+2+b"+(var_a*2+var_b))
#--------------------------------
nuevo(2);
#################################################################
#Clase_Variables_03
radio = input("teniendo un circulo:¿Cuál es su radio?")
print(radio, type(radio))
radio = float(radio)
print(radio, type(radio))
area = 3.14159 * radio**2
print("El area es ", area)
#--------------------------------
nombre = "Primer Nombre"
Nombre = "Segundo Nombre"
print("nombre : "+nombre);
print("Nombre : "+Nombre);
nuevo(3);
#################################################################
#Clase_Variables_04
print("""
╔═════════════════════════════════════╦═══════════════════════════════════════╗
║                                     ║                                       ║ 
║                  a += b             ║ 	           a = a + b              ║
║                  a -= b 	          ║ 	           a = a - b              ║
║                  a *= b 	          ║ 	           a = a * b              ║
║                  a /= b 	          ║ 	           a = a / b              ║
║                  a **= b 	          ║ 	           a = a ** b             ║
║                  a //= b 	          ║ 	           a = a // b             ║
║                  a %= b 	          ║ 	           a = a % b              ║
║                                     ║                                       ║
╚═════════════════════════════════════╩═══════════════════════════════════════╝
""");
a=8
b=5
print ("a = "+str(a));
print ("b = "+str(b));
a += b;print ("a += b");
print ("a = "+str(a));
a -= b;print ("a -= b");
print ("a = "+str(a));
a *= b;print ("a *= b");
print ("a = "+str(a));
a /= b;print ("a /= b");
print ("a = "+str(a));
a **= b;print ("a **= b");
print ("a = "+str(a));
a //= b;print ("a //= b");
print ("a = "+str(a));
a %= b;print ("a %= b");
print ("a = "+str(a));

nuevo(4);
#################################################################
#Clase_Variables_05
variable = "variable original"
def variable_global():
	print ("INGERSO A LA FUNCION")
	global variable1
	variable = "variable global modificada desde dentro de una funcion"

print ("variable original: ",end=(""))
print (variable)
variable_global()
print ("variable global modificada: ",end=(""))
print (variable)
nuevo(5);
#################################################################
#Clase_Variables_06

variable = "variable original"
def variable_global():
	print ("INGERSO A LA FUNCION")
	global variable1
	variable = "variable global modificada desde dentro de una funcion"

print ("variable original: ",end=(""))
print (variable)
variable_global()
print ("variable global modificada: ",end=(""))
print (variable)
nuevo(6);
#################################################################
#Clase_Variables_07		La clase Counter es una subclase de diccionario utilizada para realizar cuentas:
from collections import Counter
dato = [1,2,3,4,1,2,3,1,2,1]
print(dato)
print(Counter(dato))

dato = ("palabra")
print(dato)
print(Counter(dato))


nuevo(7);
#################################################################
#Clase_Variables_08
#Algunas formas de utilizar un contador, sus métodos y conversiones:

animales = "gato perro canario perro canario perro"
dato = Counter(animales.split())
print(animales)
print(dato) 
print(dato.most_common(1))  # Primeros elemento más repetido
print(dato.most_common(2))  # Primeros dos elementos más repetidos
print(dato.most_common())   # Elementos ordenadores por repeticiones
nuevo(8);
#################################################################
#Clase_Variables_09

dato = [10,20,30,40,10,20,30,10,20,10]
c_dato = Counter(dato)

print(c_dato.items())        # Registros del contador por clave-valor
nuevo(9);
#################################################################
#Clase_Variables_010
cadena='"hola" como va todo AHORA DARE UN ERROR'
print (cadena);
del cadena
print (cadena);#<-----------------------------ver el error aqui

print("\n por favor cargue de Ambitos ");
nuevo(10,"fin");
#################################################################
