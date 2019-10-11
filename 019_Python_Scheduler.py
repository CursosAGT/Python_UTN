from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║              Unidad 9 - Programación de eventos                             ║
║                 * Módulo sched                                              ║
║                 * Declaración de programadores                              ║
║                 * Programar eventos y poner en marcha el programador        ║
║                 * Programación de eventos considerando prioridades          ║
║                 * Cancelación de eventos                                    ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              manejo de eventos                              ║
║                                 scheduler                                   ║
║                              libreria sched                                 ║
║                                                                             ║
║                 enterabs()    Inicia en un momento específico               ║
║                       time                                                  ║
║                       priority                                              ║
║                       action                                                ║
║                       argument=()                                           ║
║                       kwargs={}                                             ║
║                                                                             ║
║                 enter()       Inicia en un lapso de espera                  ║
║                       delay                                                 ║
║                       priority                                              ║
║                       action                                                ║
║                       argument=()                                           ║
║                       kwargs={}                                             ║
║                                                                             ║
║                 cancel()      Cansela mientras el evento este en cola       ║
║                               o no haya empezado a ejecutarse               ║
║                                                                             ║
║                 empty()       Devuelve si quedan eventos pendientes.        ║
║                                                                             ║
║                 queue         Devuelve los eventos pendientes de ejecución. ║
║                                                                             ║
║                 run()         Inicia o poner en marcha el programador.      ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║        Los dos métodos tienen los siguientes argumentos:                    ║
║                                                                             ║
║        time/delay: en entertabs() define el momento de ejecución del evento ║
║          y en enter() el tiempo de espera. El valor expresado debe ser      ║
║          compatible con el valor devuelto por la función indicada como      ║
║          primer argumento del constructor scheduler().                      ║
║                                                                             ║
║        priority: establece la prioridad de ejecución cuando dos o más       ║
║          eventos tienen el mismo momento de ejecución. Cuanto más bajo es   ║
║          el número mayor prioridad tiene.                                   ║
║                                                                             ║
║        action: es la función a ejecutar.                                    ║
║                                                                             ║
║        argument: normalmente, es una tupla con los valores de los           ║
║          argumentos de la función de action. Opcional.                      ║
║                                                                             ║
║        kwargs: es un diccionario que se puede pasar como argumento de la    ║
║          función de action. Opcional.                                       ║
║                                                                             ║
║          Scheduler.add(intervalo, repeticiones, funcion, argumentos,        ║
║                                                argumentos_por_nombre)       ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

					pip install schedule

https://argentinaenpython.com/quiero-aprender-python/
https://pymotw.com/2/sched/
https://pymotw.com/3/sched/
https://python-para-impacientes.blogspot.com/2017/03/
""");

limpiar();
#################################################################
print("""
sched — Timed Event Scheduler
Purpose:	Generic event scheduler.
The sched module implements a generic event scheduler for running tasks at specific times. The scheduler class uses a time function to learn the current time, and a delay function to wait for a specific period of time. The actual units of time are not important, which makes the interface flexible enough to be used for many purposes.
The time function is called without any arguments, and should return a number representing the current time. The delay function is called with a single integer argument, using the same scale as the time function, and should wait that many time units before returning. By default monotonic() and sleep() from time are used, but the examples in this section use time.time(), which also meets the requirements, because it makes the output easier to understand.
To support multi-threaded applications, the delay function is called with argument 0 after each event is generated, to ensure that other threads also have a chance to run.

Scheduler
---------
methods and attributes:
-----------------------
scheduler.enterabs(time, priority, action, argument=(), kwargs={})

    Schedule a new event. The time argument should be a numeric type compatible with the return value of the timefunc function passed to the constructor. Events scheduled for the same time will be executed in the order of their priority. A lower number represents a higher priority.
    Executing the event means executing action(*argument, **kwargs). argument is a sequence holding the positional arguments for action. kwargs is a dictionary holding the keyword arguments for action.
    Return value is an event which may be used for later cancellation of the event (see cancel()).

scheduler.enter(delay, priority, action, argument=(), kwargs={})
    Schedule an event for delay more time units. Other than the relative time, the other arguments, the effect and the return value are the same as those for enterabs().

scheduler.cancel(event)
    Remove the event from the queue. If event is not an event currently in the queue, this method will raise a ValueError.

scheduler.empty()
    Return true if the event queue is empty.

scheduler.run(blocking=True)
    Run all scheduled events. This method will wait (using the delayfunc() function passed to the constructor) for the next event, then execute it and so on until there are no more scheduled events.
    If blocking is false executes the scheduled events due to expire soonest (if any) and then return the deadline of the next scheduled call in the scheduler (if any).
    Either action or delayfunc can raise an exception. In either case, the scheduler will maintain a consistent state and propagate the exception. If an exception is raised by action, the event will not be attempted in future calls to run().
    If a sequence of events takes longer to run than the time available before the next event, the scheduler will simply fall behind. No events will be dropped; the calling code is responsible for canceling events which are no longer pertinent.

scheduler.queue
	Read-only attribute returning a list of upcoming events in the order they will be run. Each event is shown as a named tuple with the following fields: time, priority, action, argument, kwargs.


El módulo sched implementa un programador o planificador de eventos para ejecutar tareas después de que transcurra un tiempo específico, o bien, para ejecutar en un momento determinado (por ejemplo, en una fecha y hora concretas).
El módulo sched se basa en la clase scheduler  que tiene métodos para declarar un programador; definir, ejecutar y cancelar eventos; y para consultar información sobre eventos pendientes de ejecución.

Declarar un programador
-----------------------
Para declarar un programador se utiliza el método constructor scheduler() que tiene como primer argumento una función para obtener la hora actual -que por defecto es monotonic()- y una función para introducir los tiempos de espera -que de forma predeterminada es sleep()-. Las dos funciones son del módulo time:
sched.scheduler(timefunc=time.monotonic, delayfunc=time.sleep)
Se pueden utilizar otras funciones para los argumentos de scheduler() pero las dos deben trabajar con la misma escala temporal.

# Declarar un programador con los valores por defecto:
programador1 = sched.scheduler()


Programar eventos y poner en marcha el programador
Para programar los eventos se emplean dos métodos: enterabs() y enter(). Mientras que el primero define los eventos de un programador para que se ejecuten en un momento específico, el segundo establece la ejecución para después de un tiempo de espera.

# Definir un evento para ejecutar en un momento específico
scheduler.enterabs(time, priority, action, argument=(), kwargs={})

# Definir un evento para ejecutar después de un tiempo de espera
scheduler.enter(delay, priority, action, argument=(), kwargs={})

Los dos métodos tienen los siguientes argumentos:

    time/delay: en entertabs() define el momento de ejecución del evento y en enter() el tiempo de espera. El valor expresado debe ser compatible con el valor devuelto por la función indicada como primer argumento del constructor scheduler().
    priority: establece la prioridad de ejecución cuando dos o más eventos tienen el mismo momento de ejecución. Cuanto más bajo es el número mayor prioridad tiene.
    action: es la función a ejecutar.
    argument: normalmente, es una tupla con los valores de los argumentos de la función de action. Opcional.
    kwargs: es un diccionario que se puede pasar como argumento de la función de action. Opcional.

Los métodos enterabs() y enter() devuelven un valor que se puede utilizar para cancelar con posterioridad un evento con el método cancel(), siempre que el evento no haya iniciado su ejecución o, dicho de otro modo, cuando el evento esté en cola esperando a ejecutarse. El método empty() se utiliza para conocer si quedan eventos pendientes. La clase scheduler también cuenta con el atributo queue, muy útil, para consultar información sobre los eventos pendientes de ejecución.
Después de definir los eventos hay que poner en marcha el programador con el método run(). Este método hace que el programador espere (valiéndose de la función de retardo especificada en el método constructor) a que los eventos se vayan ejecutando, uno a uno, en el tiempo establecido y hasta que no quede ninguno pendiente. El método run() espera la ejecución porque tiene el argumento blocking con el valor True, por defecto. Si el valor de este argumento es False se ejecutarán sólo los eventos que vencen inmediatamente (por ejemplo, eventos con tiempo de espera en 0), devolviendo run(), si existe, el momento límite de la siguiente ejecución programada. Este argumento está disponible a partir de Python 3.3.

Programar eventos para ejecutar en un momento determinado
En el siguiente ejemplo se declara un programador con dos eventos para ejecutar una tarea 1 segundo después de poner en marcha el programador y la misma tarea cinco segundos después. El programador se crea con la función time.time() que devuelve el tiempo expresado en segundos. (Cualquier fecha-hora se puede expresar en segundos y viceversa. Ver: El módulo time)
""");
limpiar();
#################################################################
#Clase_Scheduler_Ej_01
import schedule
#from schedule import Scheduler
import sched
import time
import os
import tarfile

# Función que es llamada por los eventos
def abrir_cerrar(estado):
	formato = '%d-%m-%Y %H:%M:%S'
	print ('TIEMPO:',time.asctime( time.localtime(time.time()) ))
	if estado:
		print("Abriendo compuertas...")
		# Obtiene fecha/hora local como tupla struct_time
		st_tiempo = time.localtime()

		# Convierte fecha/hora a segundos
		tiempo = time.mktime(st_tiempo)

		# Convierte fecha/hora a cadena
		str_tiempo = time.strftime(formato, st_tiempo)
		print(str_tiempo)
#		result=commands.getoutput('python_energia_cinetica.py')

		# Obtiene fecha/hora local como tupla struct_time, paso fecha/hora a segundos pasamos fecha/hora a cadena
		tiempo = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
		print(tiempo)


	else:
		print("Cerrando compuertas...")

# Declarar el programador
programador = sched.scheduler(time.time, time.sleep)

# Asignar el tiempo de comienzo (en segundos)
comienzo = int(time.time())
tiempo_inicio = comienzo + 1   # Tiempo para abrir compuertas (1")
tiempo_cierre = comienzo + 5   # Tiempo para cerrar compuertas (5")
print('PROGRAMADOR INICIADO:',time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(comienzo)))
# Definir los dos eventos indicando: momento de ejecución,
# prioridad, función a la que se llama y el valor que se
# pasa al argumento de la función:
programador.enterabs(tiempo_inicio, 1, abrir_cerrar, (1,))
programador.enterabs(tiempo_cierre, 1, abrir_cerrar, (0,))

# Poner en marcha el programador.
# El programa permanece a la espera hasta que se
# ejecuten los dos eventos. La ejecución se producirá
# cuando se alcance el momento definido.
programador.run()
print('PROGRAMADOR FINALIZADO:',time.strftime('%d-%m-%Y %H:%M:%S', time.localtime()))



"""
def print_time(a='default'):
	print("En memoria print_time", time.time(), a)
def print_some_times():
	print(time.time())
	programador.enter(10, 1, print_time)
	programador.enter(5, 2, print_time, argument=('positional',))
	programador.enter(5, 1, print_time, kwargs={'a': 'keyword'})
	programador.run()
	print(time.time())
print_some_times()"""
'''
Salida:

PROGRAMADOR INICIADO: 1489659568
TIEMPO: 1489659569
Abriendo compuertas...
TIEMPO: 1489659573
Cerrando compuertas...
PROGRAMADOR FINALIZADO: 1489659573
'''
nuevo(1);
#################################################################
#Clase_Scheduler_Ej_02
print("""
Programar eventos con posibilidad de cancelación
Se declara un programador con dos eventos de las mismas características que en el ejemplo anterior. En este caso se utiliza el valor de retorno del método enterabs() para cancelar el segundo evento cuando el número aleatorio devuelto por la función randint() es impar.
""");
import sched
import time
import random

# Función que es llamada por los eventos
def abrir_cerrar(estado, mantener):
    print ('TIEMPO:',time.asctime( time.localtime(time.time()) ))
    if mantener and not programador.empty():
        programador.cancel(ev2)

    if estado:
        print("Abriendo compuertas...")
    else:
        print("Cerrando compuertas...")

# Obtener un número aleatorio entre 1 y 5
# Si el valor es impar: no cerrar compuertas
valor = random.randint(1, 5)
if valor % 2:
    print("No mantener compuertas abiertas")
    mantener_abiertas = False
else:
    print("Mantener compuertas abiertas")
    mantener_abiertas = True

# Declarar el programador
programador = sched.scheduler(time.time, time.sleep)

# Asignar el tiempo de comienzo (en segundos)
comienzo = int(time.time())
tiempo_inicio = comienzo + 1   # Tiempo para abrir compuertas
tiempo_cierre = comienzo + 5         # Tiempo para cerrar compuertas
print('PROGRAMADOR INICIADO:',time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(comienzo)))

# Definir los dos eventos indicando: momento de ejecución,
# prioridad, función a la que se llama y valores que se
# pasan a los argumentos de la función:
ev1 = programador.enterabs(tiempo_inicio, 1, abrir_cerrar, (1, mantener_abiertas))
ev2 = programador.enterabs(tiempo_cierre, 1, abrir_cerrar, (0, mantener_abiertas))

# Poner en marcha el programador.
# El programa permanece a la espera hasta que se
# ejecuten los dos eventos. La ejecución se producirá
# cuando se alcance el momento definido.
programador.run()
print('PROGRAMADOR FINALIZADO:',time.strftime('%d-%m-%Y %H:%M:%S', time.localtime()))

'''
Salidas posibles:

1) Si el número devuelto por randint() es par
No mantener compuertas abiertas
PROGRAMADOR INICIADO: 1489659900
TIEMPO: 1489659901
Abriendo compuertas...
TIEMPO: 1489659905
Cerrando compuertas...
PROGRAMADOR FINALIZADO: 1489659905

2) Si el número devuelto por randint() es impar
Mantener compuertas abiertas
PROGRAMADOR INICIADO: 1489659972
TIEMPO: 1489659973
Abriendo compuertas...
PROGRAMADOR FINALIZADO: 1489659973
'''
nuevo(2);
#################################################################
#Clase_Scheduler_Ej_03
print("""
Programar eventos para ejecutar después de un tiempo de espera
Programamor con tres eventos para ejecutar la misma tarea después de esperar 1, 2 y 3 segundos, respectivamente. El programador se crea con time.monotonic() que es la función que utiliza por defecto el constructor, que devuelve el tiempo expresado en segundos. En este caso el primer argumento de la función enter() representa el valor del tiempo de espera que utiliza la función sleep() en el constructor.
""");

def tarea(nombre, comienzo):
    ahora = time.time()
    diferencia = int(ahora - comienzo)

    print('MOMENTO :', (time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(ahora))),
          'Diferencia:', diferencia, 'segundos',
          'Tarea:', nombre)

programador = sched.scheduler()
comienzo = time.time()
print('COMIENZO:', time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(comienzo)))

programador.enter(1, 1, tarea, ('TAREA_1', comienzo))
programador.enter(2, 1, tarea, ('TAREA_2', comienzo))
programador.enter(3, 1, tarea, ('TAREA_3', comienzo))
programador.run()

print('FINAL   :', time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(time.time())))
'''
Salida:

COMIENZO: 1489579919.1849022
MOMENTO : 1489579920 Diferencia: 1 segundos Tarea: TAREA_1
MOMENTO : 1489579921 Diferencia: 2 segundos Tarea: TAREA_2
MOMENTO : 1489579922 Diferencia: 3 segundos Tarea: TAREA_3
FINAL   : 1489579922.1852293
'''
print("""
Programar eventos para ejecutar considerando la prioridad
Programamos tres eventos para ejecutar la misma tarea. Uno de ellos, la ejecuta después de 1 segundo de espera y los otros dos eventos como tienen el mismo tiempo de espera (3 segundos) utilizan el argumento de la prioridad para establecer el orden de ejecución. En este caso el tercero que tiene una prioridad más alta se ejecuta antes que el segundo.

El programador se crea con la función time.time() y la función tiempo() se utiliza para 'humanizar' la salida del tiempo que se expresa en esta ocasión con el siguiente formato de fecha/hora: '%d-%m-%Y %H:%M:%S'.
""");
nuevo(3);
#################################################################
#Clase_Scheduler_Ej_04
import sched
import time

def tiempo():
    formato = '%d-%m-%Y %H:%M:%S'

    # Obtiene fecha/hora local como tupla struct_time
    st_tiempo = time.localtime()

    # Convierte fecha/hora a segundos
    tiempo = time.mktime(st_tiempo)

    # Convierte fecha/hora a cadena
    str_tiempo = time.strftime(formato, st_tiempo)
    return tiempo, str_tiempo

def tarea(nombre, comienzo):
    ahora, str_ahora = tiempo()
    diferencia = int(ahora - comienzo)
    print('MOMENTO :', (time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(ahora))),
          'Diferencia:', diferencia, 'segundos',
          'Tarea:', nombre)

programador = sched.scheduler(time.time, time.sleep)
comienzo, str_comienzo = tiempo()
print('COMIENZO:', time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(comienzo)))

programador.enter(1, 1, tarea, ('TAREA_1', comienzo))
programador.enter(3, 2, tarea, ('TAREA_2', comienzo))
programador.enter(3, 1, tarea, ('TAREA_3', comienzo))
programador.run()

final, str_final = tiempo()
print('FINAL   :', time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(time.time())))

'''
Salida:

COMIENZO: 15-03-2017 11:36:07
MOMENTO : 15-03-2017 11:36:08 Diferencia: 1 segundos Tarea: TAREA_1
MOMENTO : 15-03-2017 11:36:10 Diferencia: 3 segundos Tarea: TAREA_3
MOMENTO : 15-03-2017 11:36:10 Diferencia: 3 segundos Tarea: TAREA_2
FINAL   : 15-03-2017 11:36:10
'''
nuevo(4);
#################################################################
#Clase_Scheduler_Ej_05
print("""
Programar eventos para ejecutar controlando el bloqueo

Para finalizar, un ejemplo en el que se utiliza el argumento blocking del método run() para bloquear el programa para que espere a que finalice la ejecución de todos los eventos o, bien, para que se ejecuten sólo los eventos de ejecución inmediata (son aquellos que tienen el valor 0 en el tiempo de espera.

En este caso se utiliza también la función randint() para generar un número aleatorio. Si el número obtenido es par blocking toma el valor True y el programa espera la ejecución de todos los eventos. Si el número es impar sólo se ejecutan los eventos inmediatos.

El programador se crea con la función time.time() y la función tiempo() se utiliza para 'humanizar' la salida del tiempo que se expresa en esta ocasión con el siguiente formato de fecha/hora: '%d-%m-%Y %H:%M:%S'.
""");
import sched
import time
import random

def tiempo():
    formato = '%d-%m-%Y %H:%M:%S'

    # Obtiene fecha/hora local como tupla struct_time
    st_tiempo = time.localtime()

    # Convierte fecha/hora a segundos
    tiempo = time.mktime(st_tiempo)

    # Convierte fecha/hora a cadena
    str_tiempo = time.strftime(formato, st_tiempo)
    return tiempo, str_tiempo

def tarea(nombre, comienzo):
    ahora, str_ahora = tiempo()
    diferencia = int(ahora - comienzo)
    print('MOMENTO :', (time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(ahora))),
          'Diferencia:', diferencia, 'segundos',
          'Tarea:', nombre)

# Obtener un número aleatorio entre 1 y 5
# Si el valor es impar: ejecutar todos los eventos
valor = random.randint(1, 5)
if valor % 2:
    print("Ejecutar todos los eventos")
    bloquear = True
else:
    print("Ejecutar sólo eventos inmediatos")
    bloquear = False

programador = sched.scheduler(time.time, time.sleep)
comienzo, str_comienzo = tiempo()
print('COMIENZO:', time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(comienzo)))

programador.enter(0, 1, tarea, ('TAREA_1', comienzo))
programador.enter(0, 1, tarea, ('TAREA_2', comienzo))
programador.enter(3, 1, tarea, ('TAREA_3', comienzo))
programador.run(blocking=bloquear)

final, str_final = tiempo()
print('FINAL   :', time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(time.time())))

'''
Salidas posibles:

1) Si el número devuelto por randint() es impar:

Ejecutar todos los eventos
COMIENZO: 16-03-2017 12:13:44
MOMENTO : 16-03-2017 12:13:44 Diferencia: 0 segundos Tarea: TAREA_1
MOMENTO : 16-03-2017 12:13:44 Diferencia: 0 segundos Tarea: TAREA_2
MOMENTO : 16-03-2017 12:13:47 Diferencia: 3 segundos Tarea: TAREA_3
FINAL   : 16-03-2017 12:13:47

2) Si el número devuelto por randint() es par:

Ejecutar sólo eventos inmediatos
COMIENZO: 16-03-2017 12:14:11
MOMENTO : 16-03-2017 12:14:11 Diferencia: 0 segundos Tarea: TAREA_1
MOMENTO : 16-03-2017 12:14:11 Diferencia: 0 segundos Tarea: TAREA_2
FINAL   : 16-03-2017 12:14:11
'''
nuevo(5,"fin");
#################################################################

#scheduler.queue
