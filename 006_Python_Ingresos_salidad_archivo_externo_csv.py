from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos(x):
	#Con tab colocaremos aqui las precticas hechas
	pass

####################                  CSV(texto separado por comas)
print("""
╔═════════════════════════════════════════════════════════════════════════════╗ 
║                                                                             ║
║                                       CVS                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde""");

#################################################################
#IO_ext Ej_01;

import csv
 
with open('desde_plan_calculo.csv', newline='') as archivo_de_csv:  
	csv_a_memoria = csv.reader(archivo_de_csv)
	for row in csv_a_memoria:
		print(row)
nuevo(1);
with open('desde_plan_calculo.csv', newline='') as archivo_de_csv:  
	csv_a_memoria = csv.reader(archivo_de_csv, delimiter=',', quotechar=',',
						quoting=csv.QUOTE_MINIMAL)
	for row in csv_a_memoria:
		print(row)

nuevo(2);
import csv
archivo = open('salida_a_csv2.csv', 'w')
with archivo:
	writer = csv.writer(archivo)
	writer.writerows([{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'},
					  {'Grade': 'A', 'first_name': 'Rachael','last_name': 'Rodriguez'},
					  {'Grade': 'C', 'first_name': 'Tom', 'last_name': 'smith'},
					  {'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
					  {'Grade': 'A', 'first_name': 'Kennzy', 'last_name': 'Tim'}])
print("grabamos el archivo 'salida_a_csv2.csv' ver en el directorio y abrir con la planilla de calculo")
limpiar()
archivo = open('salida_a_csv3.csv', 'w')
with archivo:
	fieldnames = ['first_name', 'last_name', 'Grade']
	writer = csv.DictWriter(archivo, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows([{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'},
					  {'Grade': 'A', 'first_name': 'Rachael',
						  'last_name': 'Rodriguez'},
					  {'Grade': 'C', 'first_name': 'Tom', 'last_name': 'smith'},
					  {'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
					  {'Grade': 'A', 'first_name': 'Kennzy', 'last_name': 'Tim'}])
print("grabamos el archivo 'salida_a_csv3.csv' ver en el directorio y abrir con la planilla de calculo")
nuevo(3);
print("""
╔═════════════════════════════════════════════════════════════════════════════╗ 
║                                                                             ║
║                                     Pandas                                  ║
║          https://www.doctormetrics.com/importando-datos-en-python/          ║
║   https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html     ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde""");

import pandas as pd
df = pd.read_csv('desde_plan_calculo.csv')
print("Habro el archivo 'desde_plan_calculo.csv'" )
print("dataframe = df")
for row in df:
	print(row)
limpiar()
print("Imprimo la columna Dato1")
print(df['Dato1'])
limpiar()

print(df['Dato1'])
print("Imprimo la columna Dato1 x Dato3")
print(df)
df[['Dato3','Dato1']]=df[['Dato1','Dato3']]
print(df)
limpiar()

print("original\n",df)
print("Imprimo los index 0 a 5 de Dato2")
print(df.loc[:5])#gets rows (or columns) with particular labels from the index
limpiar()
print(df.loc[8:15])#c gets rows (or columns) at particular positions in the index (so it only takes integers).
limpiar()
print(df.loc[5:])
limpiar()
print(df.loc[df.index[[0,2,3,4,5]],'Dato2'])
limpiar()
print("Imprimo criterios lambda")
criterio = df['DatoALF'].map(lambda x: x.startswith('b'))
print(criterio)
limpiar()

criterio = df['DatoALF'].map(lambda x: x.startswith('b'))
print(criterio)
limpiar()

print("Imprimo la columna Dato4 ordenada ascendente")
print(df.sort_values(by='Dato4'))
limpiar()
print("Imprimo la columna Dato4 ordenada decendente")
print(df.sort_values(by='Dato4',ascending=False))
limpiar()
print("Imprimo la 5ta columna Datos >50 %")
print(df[df.ix[:,5]>50])

print("utilizamos los métodos head, que sería cabeza, para mostrar las primeras filas del marco de datos.")
print(df.head())
print("utilizamos tail o cola, que muestra las filas inferiores de los datos.")
print(df.tail())
nuevo(4);
print("Antes\n",df.head())
cabecera = ["ID", "Columna_1", "Columna_2", "Columna_3", "Columna_4", "Columna_5", "Columna_6"]
df.columns = cabecera
df.head()
print("Despues\n",df.head())
salida='salida_a_csv.csv'
df.to_csv(salida)

nuevo(5);

print("""
╔═════════════════════════════════════════════════════════════════════════════╗ 
║                                                                             ║
║                                   Plotly                                    ║
║                             pip install plotly                              ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde""");
#desde la web
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
print("Desde la web\n",df.head())
print("Abre el navegador web")
fig = px.line(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')
fig.show()

nuevo(6);
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
print("Desde la web\n",df.head())
fig = go.Figure(go.Scatter(x = df['AAPL_x'], y = df['AAPL_y'],
                  name='Share Prices (in USD)'))

fig.update_layout(title='Apple Share Prices over time (2014)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.show()
nuevo(7);


print("""
╔═════════════════════════════════════════════════════════════════════════════╗ 
║                                                                             ║
║                                    Numpy                                    ║
║          https://www.doctormetrics.com/importando-datos-en-python/          ║
║                           pip install -U numpy                              ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde""");
	
import numpy as np
print("""
Si en nuestro archivo tenemos datos de diferentes tipos, podemos usar dos funciones: genfromtext() y recfromcsv().
Cuando exista cabecera, especificaremos names=True.
Al pasar el argumento dtype=None, la función averigua qué tipo corresponde a cada columna.
""")
# Cargamos el fichero como el array: datos
#dato = np.loadtxt('desde_plan_calculo.csv' , delimiter=',')		recfromcsv

df = np.recfromcsv('desde_mapa.csv', delimiter=',', names=True, dtype=None)
for row in df:
	print(row)
nuevo(8);
print("""
╔═════════════════════════════════════════════════════════════════════════════╗ 
║                                                                             ║
║                                 Matplotlib                                  ║
║                         pip install -U matplotlib                           ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
import csv
import numpy as np
import matplotlib.pyplot as plt

data_path = 'desde_mapa.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data).astype(float)
    
print(headers)
print(data.shape)
print(data[:3])

nuevo(9);
print("primera pantalla\n cerrarla para continuar")
# Plot the data
plt.plot(data[:, 1], data[:, 0])
plt.axis('equal')
plt.xlabel(headers[1])
plt.ylabel(headers[0])
plt.show()
print("segunda pantalla\n cerrarla para continuar")
plt.plot(data[:, 2])
plt.xlabel('Tablas Index')
plt.ylabel(headers[2])
plt.show()

nuevo(10);


import matplotlib.pyplot as plt
import numpy as np

x,y= np.loadtxt('desde_2c.txt', delimiter=',', unpack=True)
print("Pantalla\n cerrarla para continuar")
plt.plot(x,y, marker='o')

plt.title('Datos desde_txt via archivo')

plt.xlabel('Cantidad de gente')
plt.ylabel('Gastos')

plt.show()

nuevo(11);

import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("desde_2c.csv")
x = dataframe.dato_x
y = dataframe.dato_y
plt.scatter(x, y)
plt.show()
plt.savefig("imagen_desde_cvs.png")


nuevo(12);

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

dataframe = pd.read_csv("desde_3c.csv")

x = dataframe.dato_x
y = dataframe.dato_y

stats = linregress(x, y)

m = stats.slope
b = stats.intercept

plt.scatter(x, y)
plt.plot(x, m * x + b, color="red")   # I've added a color argument here
plt.show()
plt.savefig("imagen2_desde_cvs.png")

# Or you can use plt.show()


nuevo(13);
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

dataframe = pd.read_csv("scottish_hills.csv")

x = dataframe.Height
y = dataframe.Latitude

stats = linregress(x, y)

m = stats.slope
b = stats.intercept

# Change the default figure size
plt.figure(figsize=(10,10))

# Change the default marker for the scatter from circles to x's
plt.scatter(x, y, marker='x')

# Set the linewidth on the regression line to 3px
plt.plot(x, m * x + b, color="red", linewidth=3)

# Add x and y lables, and set their font size
plt.xlabel("Height (m)", fontsize=20)
plt.ylabel("Latitude", fontsize=20)

# Set the font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()
plt.savefig("imagen3_desde_cvs.png")

nuevo(13,"fin");
