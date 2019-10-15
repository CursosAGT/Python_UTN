from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                    librerias                                ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
lenguajes de programacion hacia 2020
https://www.youtube.com/channel/UCX9NJ471o7Wie1DQe94RVIg
Javascript moviles pequeñas aplicaciones de desktop
Rust--(mozilla)-web
Dart (google) app moviles
swift-(Apples)-ios-compidado
Java (oracle) moviles pequeñas aplicaciones de desktop
Python +big data ingenieria, ciencia, seguridad informatica, backend
C++-backend/app escritorio o ontencivas
Go/Golang (google) backend en servidores pero compilado, tipeadoestatico
C# (Microsoft)
haskell
ocaml
erlang
ML
CLojure
Elexir

en caida PHP, Ruby

https://codigofacilito.com/articulos/librerias_python
#\033[1;34;41m Librerías más populares de Python \033[0m


\033[4;35m pygame \033[0m
Pygame es una librería de código abierto la cual nos permite crear aplicaciones multimedia. Aunque su principal enfoque es crear videojuegos, nosotros podemos dejar aun lado esto y realizar otro tipo de aplicaciones, aplicaciones donde necesitemos trabajar con imágenes, animaciones, música, texto, eventos, tanto del teclado como del mouse, entre otros.
Es de suma importancia mencionar que Pygame no cuenta con soporte para implementar física avanzada, por lo que esto queda por parte del desarrollador.

\033[4;35m request \033[0m
Request es una librería que nos permite realizar peticiones HTTP sin muchas complicaciones. Extremadamente útil cuando de consumir servicios web se refiere.
Con esta librería podemos trabajar con los diferentes métodos del protocolo HTTP, así como crear, enviar y recibir paquetes, modificar su contenido, trabajar con sesiones, cookies, formularios e inclusive trabajar con autenticación OAuth.
Si necesitas consurmir algún tipo de servicio web, quizás un API, esta librería sin duda te será de mucha ayuda.

\033[4;35m pillow \033[0m
Pillow o PIL (Python Image Library) me atrevería a decir que es la librería más popular de este listado. Con esta librería podemos trabajar con imágenes de una forma muy sencilla.
Podemos abrir, modificar y almacenar imágenes de diferentes formatos, así como manipular los pixeles, trabajar con máscaras, transparencias, dimensiones, agregar texto, aplicar filtros, por mencionar algunas acciones.

\033[4;35m sqlAlchemy \033[0m
trabajar con base de datos ya no es una opción, prácticamente todas nuestras aplicaciones funcionan con una. sqlAlchemy es una librería la cual nos permite trabajar con las bases de datos mediante objetos, es decir, es un ORM.
Con esta librería podemos crear, modificar, consultar y eliminar nuestras tablas, así como crear, leer, actualizar y eliminar nuestros registros. El poder de SqlAlchemy no se limita únicamente esto. Podemos crear modelos con diferentes relaciones, uno a uno, uno a muchos, muchos a muchos inclusive relaciones polimórficas.
Podemos trabajar con joins, ordenamiento, conteo, commits, roollback etc... todo lo que hagas comúnmente en SQL lo podrás hacer con esta librería.

\033[4;35m Peewee \033[0m
Al igual que sqlAlchemy, Peewee es un ORM que nos permite trabajar con diferentes de gestores de base de datos. Destacando Postgres, MySQL y SQLite.
Si eres nuevo en el mundo de base de datos y python te recomiendo comiences con este ORM. De forma personal considero que Peewee tiene una curva de aprendizaje muy baja. Además que si tu objetivo es utilizar un Framework Web como Django trasladar los conocimientos de Peewee se te será muy sencillo.
A Diferencia de las librerías mencionadas anteriormente, re no necesita instalación alguna, ya que esta, se encuentra lista para ser usada con un simple import, claro, siempre y cuando hayas instalado Python.


\033[4;35m import re \033[0m
con re podemos trabajar con expresiones regulares, podemos crearlas y aplicarlas.
Si necesitas validar algun formato, quizás un correo electronico, que mejor que hacerlo con una expresión regular.

El tema de expresiones regulares es muy amplio, si te interesa puedes leer más
 en la documentación oficial.

\033[4;35m collections \033[0m
Al igual que re, collections es una librería la cual ya se encuentra lista para usar. Esta librería nos permite trabajar con listas, tuplas, diccionarios entre otras estructuras de datos.
Las acciones que podemos realizar con esta librería son muchas así como variadas, desde ordenar diccionarios, agrupar objetos hasta combinar estructuras y concatenarlas.

>>> import collections
>>> c = collections.Counter('helloworld')
>>> c

Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

""")
import math
print(dir(math));
limpiar()
print(help(math));
print(math.pi);

