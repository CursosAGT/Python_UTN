from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
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
""");
class Mascota:
	def __init__(self,nombre, especie=None, raza=None, patas=4,  edad=None):
		self.nombre=nombre;
		self.especie=especie;	
		self.raza=raza;
		self.patas=patas;
		self.edad=edad;
	def nombrar(self, dato_nombre):
		self.nombre =dato_nombre;
	def datar(self,especie=None, raza=None, patas=4, nombre=None, edad=None):
		self.especie=especie;	
		self.raza=raza;
		self.patas=patas;
		self.nombre=nombre;
		self.edad=edad;
perro= Mascota("Wanda","Can","Weimaraner",4,6)
gato1= Mascota("Manchas","Felino","calle",4,5)
gato2 =Mascota("Grey")
print (f"Mi 1ra mascota stiene las sig caracteristicas: ",perro.especie,perro.raza,perro.patas,perro.nombre,perro.edad);
print (f"Mi 2da mascota stiene las sig caracteristicas: ",gato1.especie,gato1.raza,gato1.patas,gato1.nombre,gato1.edad);
print (f"Mi 2da mascota stiene las sig caracteristicas: ",gato2.especie,gato2.raza,gato2.patas,gato2.nombre,gato2.edad);
gato2.datar (nombre="Grey", especie="Felino", raza="calle", patas=4,  edad=2)
print (f"Mi 2da mascota stiene las sig caracteristicas: ",gato2.especie,gato2.raza,gato2.patas,gato2.nombre,gato2.edad);

gato2.datar (nombre="Grey", especie="Felino", raza="angora", patas=8,  edad=2)
print (f"Mi 2da mascota stiene las sig caracteristicas: ",gato2.especie,gato2.raza,gato2.patas,gato2.nombre,gato2.edad);

limpiar();
#################################################################
