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
║                           Objetos                                           ║
║                                  self.                                      ║
║                                                                             ║
║                           Clases                                            ║
║                                  Atributos (del objeto)                     ║
║                                  métodos (funciones del objeto)             ║
║                                                                             ║
║                           Constructor                                       ║
║                                  __init__                                   ║
║                                  __str__                                    ║
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
║                               _oculta                                       ║
║                               __privada                                     ║
║                                                                             ║
║                           Herencia Simple y múltiple                        ║
║                           	Orden de herencia                             ║
║                               super()                                       ║
║                               isinstance                                    ║
║                                                                             ║
║                           Polimorfismo                                      ║
║                                                                             ║
║                           Abstracción                                       ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
El concepto de encapsulamiento se apoya sobre el concepto de abstracción.

En POO solo necesita saber como interaccionar con los objetos, no necesita conocer los detalles de cómo está implementada la clase a partir de la cual se instancia el objeto. Sólo necesita conocer su interfaz pública.

La encapsulación es una forma de abstracción, ademas es un mecanismo para llevar a la práctica la abstracción.

El nivel de abstracción puede ser bajo (en un objeto se manipulan datos y métodos individualmente), o alto (en un objeto solo se usan sus métodos de servicio).
""");
nuevo(0,"inicio");
##################################################################################################################################
#Ejercicio_Clases_01

nuevo(1);
##################################################################################################################################
#Ejercicio_Clases_02

nuevo(2);
##################################################################################################################################
#Ejercicio_Clases_03

limpiar();
#################################################################
