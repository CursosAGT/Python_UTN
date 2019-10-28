from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                     CLASES                                  ║
║                                    --------                                 ║
║                                                                             ║
║          __init__(self, ...)                                                ║
║              This method is called just before the newly created object is  ║
║              returned for usage.                                            ║
║                                                                             ║
║          __del__(self)                                                      ║
║              Called just before the object is destroyed (which has          ║
║              unpredictable timing, so avoid using this)                     ║
║                                                                             ║
║          __str__(self)                                                      ║
║              Called when we use the print function or when str() is used.   ║
║                                                                             ║
║          __lt__(self, other)                                                ║
║              Called when the less than operator (<) is used. Similarly,     ║
║               there are special methods for all the operators (+, >, etc.)  ║
║                                                                             ║
║          __getitem__(self, key)                                             ║
║              Called when x[key] indexing operation is used.                 ║
║                                                                             ║
║          __len__(self)                                                      ║
║              Called when the built-in len() function is used for            ║
║              the sequence object.                                           ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                           Clases                                            ║
║                                                                             ║
║                           Class (object) Padre                              ║
║                                                                             ║
║                           Objetos                  	                      ║
║                                  estado                                     ║
║                                  propiedades                                ║
║                                  comportamiento                             ║
║                                                                             ║
║                           Instancia                                         ║
║                                                                             ║
║                           Modularizacion                                    ║
║                                                                             ║
║                           Encapsulado                                       ║
║                                                                             ║
║                           Herencia                                          ║
║                                                                             ║
║                           Polimorfismo                                      ║
║                                                                             ║
║                           def funcion (general)                             ║
║                           def metodo (clase)                                ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://www.youtube.com/watch?v=2UNrSiKEI8w
https://www.youtube.com/watch?v=Y_SiIgxc-xI


En un lenguaje orientado a objetos cuando hacemos que una clase(subclase) herede de otra clase (superclase) estamos haciendo que la
subclase contenga todos los atributos y métodos que tenía la superclase.

""")
nuevo(0,"inicio");


class A:
    def __init__(self):
        print("desde clase A")
    def a(self):
        print("Este método lo heredo de A")

class B:
    def __init__(self):
        print("desde clase B")
    def b(self):
        print("Este método lo heredo de B")

class C(A,B):
	print("desde clase c")
	print("que llama desde A y B")
	def c(self):
		print("Este método es de C")


c = C()
print("=====================")
c.a()
print("---------------------")
c.b()
print("---------------------")
c.c()
nuevo(0);
#################################################################
#Ejercicio_Clases_01

class Padre(object): 									#Creamos la clase Padre
	def __init__(self, ojos, cejas): 					#Definimos los Atributos
		self.ojos = ojos
		self.cejas = cejas


class Hijo(Padre): 										#Creamos clase hija que hereda de Padre
	def __init__(self, ojos, cejas, cara): 				#creamos el constructor de la clase especificando atributos
		Padre.__init__(self, ojos, cejas) 				#Especificamos la clase y llamamos a su constructor + Atributos
		self.cara = cara 								#Especificamos el nuevo atributo para Hijo


Tomas = Hijo('Marrones', 'Negras', 'Larga')
Pedro = Padre('Negros', 'Cortas')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)

print ("""De estas ultimas dos formas llamamos al Padre de la clase Hijo para no perder su código y ademas agregamos un atributo nuevo "cara" para la clase Hija.
Recomiendo en caso de herencia simple utilizar Super()""")
print ("isinstance(Tomas, Hijo)",isinstance(Tomas, Hijo))		#imprime si es de una clase (objeto, clase que suponemos ==> true/ false)
print ("isinstance(Tomas, Padre)",isinstance(Tomas, Padre))	#imprime si es de una clase (objeto, clase que suponemos ==> true/ false)
print ("isinstance(Pedro, Hijo)",isinstance(Pedro, Hijo))		#imprime si es de una clase (objeto, clase que suponemos ==> true/ false)
print ("isinstance(Pedro, Padre)",isinstance(Pedro, Padre))	#imprime si es de una clase (objeto, clase que suponemos ==> true/ false)
nuevo(1);



#################################################################
#Ejercicio_Clases_02
#desde Ejercicio_Clases_07

class stock_general(object):
	def __init__(self,codigo,nombre,stock,descripcion):
		self.codigo = codigo
		self.nombre = nombre
		self.stock = stock
		self.descripcion = descripcion
	def __str__(self):
		return f"LUGAR\t\t{self.__class__.__name__}\n" \
				f"\nREFERENCIA\t {self.codigo}\n" \
				f"NOMBRE\t\t {self.nombre}\n" \
				f"STOCK\t\t {self.stock}\n" \
				f"DESCRIPCIÓN\t {self.descripcion}\n"
class almacen_1(stock_general):#creo una clase que hereda de productos
	def __init__(self,codigo,nombre,stock,descripcion,costo_estibaje=100):
		stock_general.__init__(self,codigo,nombre,stock,descripcion)
		self.costo_estibaje=costo_estibaje
class almacen_2(stock_general):#creo una clase que hereda de productos
	def __init__(self,codigo,nombre,stock,descripcion,costo_estibaje=250):
		stock_general.__init__(self,codigo,nombre,stock,descripcion)
		self.costo_estibaje=costo_estibaje
item1 = almacen_2("xx2034yy", "Vaso",15, "Vaso de porcelana 50 cc, color blanco con dibujos",50)
item2 = almacen_2("25cc25cxc", "copa",50, "Copa cristal x 6 unidades, cristal",)
item3 = almacen_2("sad122", "plato",25, "Plato  x 6 unidades, Blanco",200)
item4 = almacen_1("ss123", "silla",600, "silla x 6 unidades, Negro",300)
item5 = almacen_1("mm147", "mesa",500, "mesa  x 1 unidad, Negro")
item6 = almacen_1("s258s", "sillon",250, "sillon  x 1 unidad, Negro",1000)
prod=[item1,item2,item3,item4,item5,item6]
for productos in prod:
	print("\n--------------------------")
	#print("\n",productos )
	print("Item: ",productos.nombre)
	if( isinstance(productos, stock_general) ):#pregunta si es de una clase (objeto, clase que suponemos ==> true/ false)
		print(f"En stock_general hay {productos.stock} unidades de { productos.nombre} con codigo {productos.codigo}")
	if( isinstance(productos, almacen_1) ):
		print(F"Ubicadas en {productos.__class__.__name__,} direccion xxx\nCosto estibaje",productos.costo_estibaje)
	elif( isinstance(productos, almacen_2) ):
		print(F"Ubicadas en {productos.__class__.__name__,} direccion xxx\nCosto estibaje",productos.costo_estibaje)
nuevo(2);
#################################################################
#Ejercicio_Clases_03

class Animal():
	def __init__(self,nombre,raza, color):
		self.nombre=nombre
		self.raza=raza
		self.color=color
	def mostrar(self):
		print(f"{self.nombre} es el nombre de un {self.raza} color{self.color}")
class Mascota(Animal):
	def __init__(self,nombre,raza, color,dueno,codigo):
		super().__init__(nombre,raza, color)#llamo al init del super y le paso el paquete de valores
		self.raza=raza
		self.color=color
		self.dueno=dueno
		self.codigo=codigo
	def mostrar(self):
		print(f"{self.nombre} es el nombre de un {self.raza} color {self.color} cuyo dueño es {self.dueno} registrado con el codigo {self.codigo}")
objeto_1=Animal("white","oso","blanco")
objeto_2=Mascota("wanda","algo parecido a u perro ","gris/marron/plata","Ariel","xxxx")
objeto_1.mostrar()
objeto_2.mostrar()
nuevo(3);
#################################################################
#Ejercicio_Clases_04

class Humanoide(object):#				clases padre
	def __init__(self):#					Constructor de estado inicial
		self.__cabeza=1#           			estado inicial en la clase padre
		self.__piernas=2#           		estado inicial en la clase padre
		self.__brazos=2#           			estado inicial en la clase padre
		self.__ojos=2#           			estado inicial en la clase padre
		self.__orejas=2#           			estado inicial en la clase padre
		self.vigilia_reposo=False#          estado inicial en la clase padre
		self.hiberna=False#           		estado inicial en la clase padre
		self.simbionte=False#           	estado inicial en la clase padre
		self.emociones=True#           		estado inicial en la clase padre
		self.comerciantes=False#           	estado inicial en la clase padre
		self.luchadores=False#           	estado inicial en la clase padre
		self.logicos=False#           		estado inicial en la clase padre
		self.reproduccion_sexual=True#      estado inicial en la clase padre
		self.pelo=True#           			estado inicial en la clase padre
	def despertar(self,llamado):
		self.vigilia_reposo=llamado
		if (self.vigilia_reposo):
			return "Estado para audiencia: disponible"
		else:
			return "durmiendo, comunicacion pendiente"
	def estados(self,tipo,llamado):
		print ("Propiedad humanoide -"+(tipo));
		print ("	cabeza :",self.__cabeza);
		print ("	piernas :",self.__piernas);
		print ("	brazos :",self.__brazos);
		print ("	ojos :",self.__ojos);
		print ("	orejas :",self.__orejas);
		print ("	vigilia_reposo :",self.vigilia_reposo);
		print ("	hiberna :",self.hiberna);
		print ("	simbionte :",self.simbionte);
		print ("	emociones :",self.emociones);
		print ("	comerciantes :",self.comerciantes);
		print ("	luchadores :",self.luchadores);
		print ("	logicos :",self.logicos);
		print ("	reproduccion_sexual :",self.reproduccion_sexual);
		print ("	pelo :",self.pelo);
		print ("		comportamiento humanoide -terraqueo reunion :",self.despertar(llamado)) #Accion despertar
class Terraqueo(Humanoide):#									 		clases hija
	def __init__(self):#								Constructor de estado inicial
		super(Terraqueo,self).__init__(vigilia_reposo)#			se define a partir del constructor padre
		super(Terraqueo,self).__init__(hiberna)#				se define a partir del constructor padre
		super(Terraqueo,self).__init__(simbionte)#				se define a partir del constructor padre
		super(Terraqueo,self).__init__(emociones)#				se define a partir del constructor padre
		super(Terraqueo,self).__init__(comerciantes)#			se define a partir del constructor padre
		super(Terraqueo,self).__init__(luchadores)#				se define a partir del constructor padre
		super(Terraqueo,self).__init__(logicos)#				se define a partir del constructor padre
		super(Terraqueo,self).__init__(reproduccion_sexual)#	se define a partir del constructor padre
		super(Terraqueo,self).__init__(pelo)#					se define a partir del constructor padre
		self.continente_origen="Africa"#        				estado inicial en la clase hija
		self.pais_origen="Egipto"#       						estado inicial en la clase hija
		self.ciudad_origen="El Cairo"#       					estado inicial en la clase hija
		self.ano_origen=3500#       							estado inicial en la clase hija
class Europeo(Terraqueo):#									 		clases nieta
	def __init__(self):#								Constructor de estado inicial
		super(Europeo,self).__init__(vigilia_reposo)#			se define a partir del padre e hija
		self.continente_origen="Europa"
		Europeo,self.__init__(pais_origen)#						se define a partir del hijo
		Europeo,self.__init__(ciudad_origen)#					se define a partir del hijo
		Europeo,self.__init__(ano_origen)#						se define a partir del hijo
	pass
class Americano(Terraqueo):#									 	clases nieta
	pass
class Asiatico(Terraqueo):#									 		clases nieta
	pass
terraqueo=Humanoide() #instancia desde clases
klingon=Humanoide() #instancia desde clases
vulcano=Humanoide() #instancia desde clases
bajoriano=Humanoide() #instancia desde clases
ferengi=Humanoide() #instancia desde clases
trill=Humanoide() #instancia desde clases
romuliano=Humanoide() #instancia desde clases

#genero impresión
terraqueo.estados("terraqueo",True);
klingon.estados("klingon",False);
vulcano.estados("vulcano",True);
bajoriano.estados("bajoriano",False);
ferengi.estados("ferengi",True);
trill.estados("trill",False);
romuliano.estados("romuliano",True);
var=input("enter para hacer cambios");

terraqueo.emociones=True#       Cambio estado inicial
klingon.luchadores=True#        Cambio estado inicial
klingon.emociones=True#         Cambio estado inicial
vulcano.emociones=False#        Cambio estado inicial
vulcano.logicos=False#         	Cambio estado inicial
bajoriano.emociones=True#     	Cambio estado inicial
ferengi.comerciantes=False#		Cambio estado inicial
trill.simbionte=True#           Cambio estado inicial
romuliano.luchadores=True#      Cambio estado inicial
terraqueo.__cabeza=4#           estado inicial
klingon.__cabeza=2#           	estado inicial
vulcano.__piernas=6#           	estado inicial
bajoriano.__brazos=9#           estado inicial
trill.__ojos=4#           		estado inicial
romuliano.__orejas=3#           estado inicial

terraqueo.estados("terraqueo",True);
klingon.estados("klingon",False);
vulcano.estados("vulcano",True);
bajoriano.estados("bajoriano",False);
ferengi.estados("ferengi",True);
trill.estados("trill",False);
romuliano.estados("romuliano",True);
nuevo(3);
#################################################################

print("Herencias multiples, problemas a tener en cuenta")

class fruta:#a/o
	def tipo(self):
		print("rodajas")
class verdura:
	def cortar(self):
		print(" cubos")
class ensalada(fruta,verdura):#El orden de prioridad de herencia múltiple siempre va de izquierda a derecha
	pass

tomate=ensalada()
lechuga=ensalada()
tomate.tipo()
lechuga.tipo()
print ()
nuevo(3,"fin");

