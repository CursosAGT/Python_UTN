from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                AMBITOS                                      ║
║                               ---------                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝
 * Ambito, es una region en el espacio donde los nombres (cuyos datos busco) son accesibles directamente.(Recordad que puede haber el mismo nombre como atributo como accion y en distintos ambitos");
 * Ambito, es observable por estructuras de tabulacion")
 * Un espacio con un nombre hereda del Nombre ser la referencia a un dato en un tiempo y espàcio.");
	 Si en el espacio nombrado su dato No cambia durante el tiempo de ejecucion se denomina * constante (constantes, tuple etc)");
	 Si en el espacio nombrado su dato Si cambia durante el tiempo de ejecucion se denomina * variable (variable, lista, diccionario, etc");
	 puede haber muchos espacio nombrado igual en distintos ambitos y sus datos podran ser distintos o no");
	 Mutable: su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.");
	 Inmutable: su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.\n");
 * Una variable es espacio que tendra un nombre para poder acceder a ella y sus caracteristicas seran dadas por el dato que se incorpore (* tipeado dinamico)");
 * Una variable de clase es compartida por todas las instancias de una clase. Se definen dentro de la clase (después del encabezado de la clase) pero nunca dentro de un método.
	Este tipo de variables no se utilizan con tanta frecuencia como las variables de instancia.");
 * Una variable de instancia se define dentro de un método y pertenece a un objeto determinado de la clase instanciada. ");
http://docs.python.org.ar/tutorial/3/classes.html
""");
limpiar();
#################################################################
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                Estructuras                                  ║
║                               -------------                                 ║
║                              programa lineal/por objetos                    ║
║                                                                             ║
║                         * linealidad  sentencia de disrupcion               ║
║                         * llamados a metodos internos                       ║
║                         * llamados a metodos externos                       ║
║                                  * propios                                  ║
║                                  * ajenos Librerias                         ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
http://docs.python.org.ar/tutorial/3/classes.html
https://pythones.net/instalando-python-3-que-es-un-ide/""")
limpiar();
#################################################################
#IO Ej_AMBITOS_1");
variable = "RAIZ"
class clase_1:
	variable = "CLASE_1"
	def prueba_ambitos():
		variable = "FUNCION"
		cont = 0
		for i in variable:
			variable = "BUCLE"
#			print ("valor de I es : "+ i);
			cont = cont + 1
			print ("valor de variable = "+variable, end=" ");
			print ("valor de contador es : "+ str(cont));
			if cont>2:
				variable = "CONDICIONAL"
				print ("valor de variable = "+variable, end=" ");
				print ("valor de contador es : "+ str(cont));
		print ("valor de variable = "+variable);
	print ("1er valor de variable = "+variable);
	prueba_ambitos()
	print ("valor de variable = "+variable);
print ("valor de variable = "+variable);
class clase_2:
	variable = "CLASE_2"
	def prueba_ambitos_2():
		pass
	print ("valor de variable = "+variable);
print ("valor de variable = "+variable);
nuevo(1);
#################################################################
#IO Ej_AMBITOS_2");
def prueba_ambitos3():
	def funcion_local():
		variable = "variable local"
	def funcion_nonlocal():
		nonlocal variable
		variable = "variable no local"
	def funcion_global():
		global variable
		variable = "variable global"
	variable = "variable de prueba"
	funcion_local()
	print("Luego de la asignación local a la variable:", variable)
	funcion_nonlocal()
	print("Luego de la asignación no local a la variable:", variable)
	funcion_global()
	print("Luego de la asignación global a la variable:", variable)
prueba_ambitos3()
print("Ambito glogal:", variable)
nuevo(2);
#################################################################
#IO Ej_AMBITOS_3");
lista_datos_ingresados=[]
pares = [];
impares = [];
def funcion():
	print("10' datos minimo, 0 para salir");
	ingreso_num=input("ingrese un dato numerico entero > 0  :");
	ingreso_num=int(ingreso_num);
	if ingreso_num==0:
		return("nada")
#	if isinstance(ingreso, int) and ingreso !=0:
#		print("Integer: %d" % ingreso)
#	ingreso_num=int(ingreso);
	lista_datos_ingresados=[]
	pares = [];
	impares = [];
	print("Cero-'0' para salir");
	while ingreso_num>0:
		lista_datos_ingresados.append(ingreso_num);
		ingreso_num=int(input("ingrese un dato numerico entero > 0  :"));
	print ("lista : "+str(lista_datos_ingresados));
	print ("lista lugar 2 : "+str(lista_datos_ingresados[2]));
	print ("maximo: "+str(max(lista_datos_ingresados))+" de la lista");
	print ("minimo: %d de lo la lista" % min(lista_datos_ingresados));
	print ("datos: %d en la lista" % len(lista_datos_ingresados));
	print ("lista original: "+str(lista_datos_ingresados));
	lista_datos_ingresados.append("999999")  # Agrega elemento al final de lista con append();
	print ("Agrege elemento al final de lista con append ('9999'): "+str(lista_datos_ingresados));
	lista_datos_ingresados.pop()  # Borra último elemento de lista con método pop();
	print ("Borre último elemento de lista con método pop(): "+str(lista_datos_ingresados));
	lista_datos_ingresados.sort()  # Ordena la lista con el método sort();
	print ("Ordena la lista con el método sort(): "+str(lista_datos_ingresados));
	for elementos in lista_datos_ingresados:
		if elementos%2 == 0:# es par
			print ("pares  :" +str(elementos));
			pares.append(str(elementos))
		else:
			print ("Impares  :" +str(elementos));
			impares.append(str(elementos))
	print (pares);
	print (impares);
	return (lista_datos_ingresados)
print (funcion());
print ((lista_datos_ingresados));
print (pares);
print (impares);
nuevo(3);
#################################################################
#IO Ej_AMBITOS_4");
def exterior():
	variable = "local"
	print("exterior - principio :", variable);
	def interior():
		nonlocal variable
		variable = "nonlocal"
		print("interior:", variable);
	interior();
	print("exterior - final:", variable);
exterior();
nuevo(4);
#################################################################
#IO Ej_AMBITOS_5");
print ("La variablo `global` puede ser usada dentro y fuera de una funcion",);
def funcion_ext():
	variable = 20
	print("Antes de llamar a la funcion_int : ", variable);
	print("llamamos a la funcion_int");
	def funcion_int():
		global variable
		variable = 25
		print("Desntro de la funcion_int: ", variable);
	funcion_int();
	print("Salimos de la funcion_int");
	print("Despues de llamar a la funcion_int: ", variable);
funcion_ext();
print("variable en funcion_ext : ", variable);
nuevo(5);
#################################################################
#IO Ej_AMBITOS_6");
def prueba_ambitos():
	def hacer_local():
		algo = "algo local"
	def hacer_nonlocal():
		nonlocal algo
		algo = "algo no local"
	def hacer_global():
		global algo
		algo = "algo global"
	algo = "algo de prueba"
	hacer_local();
	print("Luego de la asignación local:", algo);
	hacer_nonlocal();
	print("Luego de la asignación no local:", algo);
	hacer_global();
	print("Luego de la asignación global:", algo);

prueba_ambitos();
print("In global scope:", algo);
nuevo(6);
#################################################################
#IO Ej_AMBITOS_7");
print("este programa dara un error");
distancia=10#             		Define variable local (ámbito programa principal);
velocidad=distancia/1
def acelerar():
    global distancia# 			Declara la variable 'distancia' como global y se podrá utilizar dentro de la función
    global velocidad
    tiempo=10# 					Declara variable local (ámbito función);
    distancia=distancia+5# 		Se incrementa la velocidad en 5 distancia
    velocidad=distancia/tiempo
    print('Tiempo:', tiempo);
	# 
print("velocidad=distancia/tiempo")
print("distancia= "+ str(distancia));
print("tiempo inicial = 1 ");
print('Velocidad inicial:', velocidad);# Muestra variable 'distancia'
print("Llama a la función acelerar()")
acelerar();# Llama a la función acelerar();
print('Velocidad tras acelerar:', velocidad);# Muestra variable 'distancia'
print("distancia= "+ str(distancia));
print("tiempo dos= ...'NameError...'");
# Intenta mostrar la variable 'tiempo. Se produce una excepción (error) de tipo NameError
# porque la variable no pertenece a este ámbito: # NameError: name 'tiempo' is not defined
print(tiempo);#<--------------------error
nuevo(7,"fin");
#################################################################
