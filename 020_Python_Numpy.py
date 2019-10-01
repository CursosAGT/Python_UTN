from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                        Numpy                                ║
╠═════════════════════════════════════════════════════════════════════════════╣
║   NumPy es un módulo/biblioteca que se utiliza para cálculos científicos    ║
║                                                                             ║
║   It provides:                                                              ║
║                                                                             ║
║   Numpy is a powerful N-dimensional array object sophisticated(broadcasting)║
║   functions tools for integrating C/C++ and Fortran code useful linear      ║
║   algebra, Fourier transform, and random number capabilities and much more  ║
║   Besides its obvious scientific uses, NumPy can also be used as an         ║
║   efficient multi-dimensional container of generic data. Arbitrary          ║
║   data-types can be defined. This allows NumPy to seamlessly and speedily   ║
║   integrate with a wide variety of databases.                               ║
║                                                                             ║
║   NumPy proporciona un objeto el cual es un arreglo multidimensional y otras║
║   matrices derivadas, como matrices enmascaradas o matrices                 ║
║   multidimensionales enmascaradas.                                          ║
║   El módulo NumPy proporciona un objeto ndarray que podemos usar para       ║
║   realizar operaciones en una arreglo de cualquier dimensión. El array      ║
║   significa arreglo de N dimensiones donde N es cualquier número.           ║
║   Los arreglos NumPy puede ser de cualquier dimensión.                      ║
║   NumPy tiene una serie de ventajas sobre las listas de Python.             ║
║   Podemos realizar operaciones de alto rendimiento en los arreglos NumPy    ║
║                                                                             ║
║        Ordenar los miembros de un arreglo                                   ║
║        Operaciones matemáticas y lógicas.                                   ║
║        Funciones de entrada / salida                                        ║
║        Operaciones estadísticas y de álgebra lineal.                        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

				pip install numpy


		https://unipython.com/numpy-algebra/

    ndarray.ndim –> Proporciona el número de dimensiones de nuestro array.
    ndarray.dtype –> Es un objeto que describe el tipo de elementos del array.
    ndarray.shape –> Devuelve la dimensión del array, es decir, una tupla de enteros indicando el tamaño del array en cada dimensión. Para una matriz de n filas y m columnas obtendremos (n,m).
    ndarray.data –> El buffer contiene los elementos actuales del array.
    ndarray.itemsize –> devuelve el tamaño del array en bytes.
    ndarray.size –> Es el número total de elementos del array.
    
    
		import numpy as np # Importamos numpy como el alias np
		miArray = np.arange(10) # Creamos un array de 0 a 9 separados de uno en uno
		print(type(miArray))
		numdim= miArray.ndim
		dim=miArray.shape
		tam= miArray.size
		byte=miArray.itemsize

 

    identity(n,dtype) –>Devuelve la matriz identidad, es decir, uma matriz cuadrada nula excepto en su diagonal principal que es unitaria. n es el número de filas (y columnas) que tendrá la matriz y dtype es el tipo de dato. Este argumento es opcional. Si no se establece, se toma por defecto como flotante.
    ones(shape,dtype) –>Crea un array de 1 compuesto de shape elementos.
    zeros(shape, dtype) –>Crea un array de 0 compuesto de “shape” elementos”.
    linspace(start,stop,num,endpoint=True,retstep=False) –>Crea un array con valor inicial start, valor final stop y num elementos.
    empty(shape, dtype) –>Crea un array de ceros compuesto de “shape” elementos” sin entradas.
    meshgrid(x,y) –>Genera una malla a partir de dos los arrays x, y.
    eye(N, M, k, dtype) –>Crea un array bidimensional con unos en la diagonal k y ceros en el resto. Es similar a identity. Todos los argumentos son opcionales. N es el número de filas, M el de columnas y k es el índice de la diagonal. Cuando k=0 nos referimos a la diagonal principal y por tanto eye es similar a identity.
    arange([start,]stop[,step,],dtype=None) –>Crea un array con valores distanciados step entre el valor inicial star y el valor final stop. Si no se establece step python establecerá uno por defecto.

		import numpy as np # Importamos numpy como el alias np
		g=np.zeros( (3,4) )
		print(g)
		k=np.linspace( 1, 4, 9 )
		print(k)
		X,Y=np.meshgrid([1,2,3],[7,9,34])
		print(X)
		print(Y)
    
 """);
limpiar();
#################################################################
#Clase_Numpy_Ej_01 

import numpy
 
a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[400], [800]])
print("antes\n",a)
print("antes\n",b)
c = a+b;
print("+\n",c)
c = a*b;
print("*\n",c)
newArray = numpy.append(a, b, axis = 1)
print("despues\n",newArray)
newArray = numpy.insert(a, 1, 90)
print("despues\n",newArray)
a = numpy.array([[1, 2, 3], [4, 5, 6]])
nuevo(1);
#################################################################
#Clase_Numpy_Ej_02
print("antes\n",a)
newArray = numpy.append(a, [[50, 60, 70]], axis = 0)
print("despues\n",newArray)
a = numpy.array([1, 2, 3])
newArray = numpy.delete(a, 1, axis = 0)
print("despues\n",newArray)
a = numpy.array([[1, 2, 3], [4, 5, 6], [10, 20, 30]])
print("antes\n",a)
newArray = numpy.delete(a, 1, axis = 0)
print("despues\n",newArray)
nuevo(2);
#################################################################
#Clase_Numpy_Ej_03 
a = numpy.array([1, 2, 3, 4, 5])
print("original\n",a)
index = numpy.where(a == 5)
print("'5' se encuentra en index nº: ", index[0])
nuevo(3);
#################################################################
#Clase_Numpy_Ej_04 
a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])
print("original\n",a)
print("Seccion del array = ", a[2:5])
nuevo(4);
#################################################################
#Clase_Numpy_Ej_05
a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])
print("original\n",a)
print("Seccion del array = ", a[-3:])
nuevo(5);
#################################################################
#Clase_Numpy_Ej_06
addition = lambda x: x + 2
a = numpy.array([1, 2, 3, 4, 5, 6])
print("original\n",a)
print("Array desde funcion de suma: ", addition(a))
nuevo(6);
#################################################################
#Clase_Numpy_Ej_07
a = numpy.array([1, 2, 3, 4, 5, 6])
print("The size of array = ", a.size)
l = [1, 2, 3, 4, 5]
a = numpy.array(l)
print("original\n",a)
print("genero un array NumPy desde una lista de Python  = ", a)
nuevo(7);
#################################################################
#Clase_Numpy_Ej_08
t = (1, 2, 3, 4, 5)
print("original\n",t)
a = numpy.array(t)
print("original\n",a)
print("genero un array NumPy desde una tuple de Python = ", a)
nuevo(8);
#################################################################
#Clase_Numpy_Ej_09 
a = numpy.array([1, 2, 3, 4, 5])
print("original\n",a)
print("Array listado = ", a.tolist())
nuevo(9);
#################################################################
#Clase_Numpy_Ej_010 
a = numpy.array([1, 2, 3, 4, 5])
print("original\n",a)
numpy.savetxt("mi_Array.csv", a)#modificar el nombre del archivo
a = numpy.array([16, 3, 2, 6, 8, 10, 1])
print("Ordenar el array = ", numpy.sort(a))
nuevo(10);
#################################################################
#Clase_Numpy_Ej_011 
x= numpy.array([400, 800, 200, 700, 1000, 2000, 300])
print("original\n",x)
xmax = x.max()
xmin = x.min()
x = (x - xmin)/(xmax - xmin)
print("Luego de la modificacion del array x = \n", x)
nuevo(11);
#################################################################
#Clase_Numpy_Ej_012 
a = numpy.array([20, 13, 42, 86, 81, 9, 11])
print("original\n",a)
print("Element at index 3 = ", a[3])
nuevo(12);
#################################################################
#Clase_Numpy_Ej_013 
a = numpy.array([[20, 13, 42], [86, 81, 9]])
print("original\n",a)
print("Elementos en el index a[1][2] = ", a[1][2])
nuevo(13);
#################################################################
#Clase_Numpy_Ej_014 
a = numpy.array([1, 2, 3, 4, 5])
print("original\n",a)
b = numpy.array([10, 20, 30, 40, 50])
print("original\n",b)
newArray = numpy.append(a, b)
print("Array modificado = ", newArray)
nuevo(14);
#################################################################
#Clase_Numpy_Ej_015
g=numpy.matrix( [[3,4,-9], [7,4,-5] ,[1,3,9]] )
print(g)
b=numpy.matrix( [[-9], [-5] ,[9]] )
print(b)
c=g*b
print(c)
bt=b.T #traspuestas
print("\ntraspuestas\n",bt)
bh=b.H #traspuestas y conjudaga
print("\ntraspuestas y conjudaga\n",bh)
gi=g.I #inversa
print("\ninversa\n",gi)
detgi=numpy.linalg.det(gi) #calculo del determinante
print("\ndeterminante\n",detgi)
tragi=numpy.trace(gi) #calculo de la traza
print("\ntraza\n",tragi)
nuevo(15);
#################################################################
#Clase_Numpy_Ej_016
a = numpy.array([[8, 1, 4]])
print("antes\n",a)
b= numpy.array([[3, 7, 4]])
print("antes\n",b)
c= numpy.cross(a, b) # Producto vectorial
print("\nProducto vectorial ",c)
d=numpy.outer(a, b) # Producto exterior
print("\nProducto exterior ",d)
nuevo(16);
#################################################################
#Clase_Numpy_Ej_017 
x=numpy.linspace(0,1,100)
y=numpy.sin(x)
print ("\nTransformada de Fourier:\n",numpy.fft.fft(y))
nuevo(17,"fin");
#################################################################
