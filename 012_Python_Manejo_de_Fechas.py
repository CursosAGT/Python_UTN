from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║              Unidad 5 - MySQL, Parte 1                                      ║
║                 * INSERT, UPDATE, DELETE, SELECT                            ║
║                 * FECHAS Y HORAS                                            ║
║                 * %LIKE%                                                    ║
║                 * JOIN                                                      ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                 Fecha  / hora                               ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://www.tutorialspoint.com/python/python_date_time.htm
""")
limpiar();
#################################################################
print ("""
Function with Description
-------------------------
1      time.altzone
The offset of the local DST timezone, in seconds west of UTC, if one is defined. This is negative if the local DST timezone is east of UTC (as in Western Europe, including the UK). Only use this if daylight is nonzero.

2      time.asctime([tupletime])
Accepts a time-tuple and returns a readable 24-character string such as 'Tue Dec 11 18:07:14 2008'.

3      time.clock( )
Returns the current CPU time as a floating-point number of seconds. To measure computational costs of different approaches, the value of time.clock is more useful than that of time.time().

4      time.ctime([secs])
Like asctime(localtime(secs)) and without arguments is like asctime( )

5      time.gmtime([secs])
Accepts an instant expressed in seconds since the epoch and returns a time-tuple t with the UTC time. Note : t.tm_isdst is always 0

6      time.localtime([secs])
Accepts an instant expressed in seconds since the epoch and returns a time-tuple t with the local time (t.tm_isdst is 0 or 1, depending on whether DST applies to instant secs by local rules).

7      time.mktime(tupletime)
Accepts an instant expressed as a time-tuple in local time and returns a floating-point value with the instant expressed in seconds since the epoch.

8      time.sleep(secs)
Suspends the calling thread for secs seconds.

9      time.strftime(fmt[,tupletime])
Accepts an instant expressed as a time-tuple in local time and returns a string representing the instant as specified by string fmt.

10      time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
Parses str according to format string fmt and returns the instant in time-tuple format.

11      time.time( )
Returns the current time instant, a floating-point number of seconds since the epoch.

12      time.tzset()
Resets the time conversion rules used by the library routines. The environment variable TZ specifies how this is done.
""")
limpiar();
#################################################################
print ("""
Attribute with Description
--------------------------
1      time.timezone
Attribute time.timezone is the offset in seconds of the local time zone (without DST) from UTC (>0 in the Americas; <=0 in most of Europe, Asia, Africa).

2      time.tzname
Attribute time.tzname is a pair of locale-dependent strings, which are the names of the local time zone without and with DST, respectively.

Function with Description
-------------------------
1      calendar.calendar(year,w=2,l=1,c=6)
Returns a multiline string with a calendar for year year formatted into three columns separated by c spaces. w is the width in characters of each date; each line has length 21*w+18+2*c. l is the number of lines for each week.

2      calendar.firstweekday( )
Returns the current setting for the weekday that starts each week. By default, when calendar is first imported, this is 0, meaning Monday.

3      calendar.isleap(year)
Returns True if year is a leap year; otherwise, False.

4      calendar.leapdays(y1,y2)
Returns the total number of leap days in the years within range(y1,y2).

5      calendar.month(year,month,w=2,l=1)
Returns a multiline string with a calendar for month month of year year, one line per week plus two header lines. w is the width in characters of each date; each line has length 7*w+6. l is the number of lines for each week.

6      calendar.monthcalendar(year,month)
Returns a list of lists of ints. Each sublist denotes a week. Days outside month month of year year are set to 0; days within the month are set to their day-of-month, 1 and up.

7      calendar.monthrange(year,month)
Returns two integers. The first one is the code of the weekday for the first day of the month month in year year; the second one is the number of days in the month. Weekday codes are 0 (Monday) to 6 (Sunday); month numbers are 1 to 12.

8      calendar.prcal(year,w=2,l=1,c=6)
Like print calendar.calendar(year,w,l,c).

9      calendar.prmonth(year,month,w=2,l=1)
Like print calendar.month(year,month,w,l).

10      calendar.setfirstweekday(weekday)
Sets the first day of each week to weekday code weekday. Weekday codes are 0 (Monday) to 6 (Sunday).

11      calendar.timegm(tupletime)
The inverse of time.gmtime: accepts a time instant in time-tuple form and returns the same instant as a floating-point number of seconds since the epoch.

12      calendar.weekday(year,month,day)
Returns the weekday code for the given date. Weekday codes are 0 (Monday) to 6 (Sunday); month numbers are 1 (January) to 12 (December).
""")
limpiar();
#################################################################
#Clase_fechas_Ej_001
import datetime


print ("uso de libreria # datetime ")
fecha = datetime.datetime.now()
print(f"Fecha - hora              :"+str(fecha))
print(f"Fecha                     :"+str(datetime.date.today()))
print(f"Dia numero                :"+str(fecha.day));
print(f"Mes                       :"+str(fecha.month));
print(f"Año                       :"+str(fecha.year));
print(f"La fecha es               :{fecha:%d %m, %Y}")
print(f"La fecha es               :{fecha:%d %B, %Y}")
print ("\nUsando strftime\n ver:https://www.guru99.com/date-time-and-datetime-classes-in-python.html")
print(f"Fecha - hora %c           :"+str(fecha.strftime("%c")));
print(f"Dia numero %D             :"+str(fecha.strftime("%D")));
print(f"Fecha %x                  :"+str(fecha.strftime("%x")));
print(f"Hora %X                   :"+str(fecha.strftime("%X")));
print(f"Dia de la semana %a       :"+str(fecha.strftime("%a")));
print(f"Dia de la semana %A       :"+str(fecha.strftime("%A")));
print(f"Dia numero %d             :"+str(fecha.strftime("%d")));
print(f"Mes %b                    :"+str(fecha.strftime("%b")));
print(f"Mes %B                    :"+str(fecha.strftime("%B")));
print(f"Año %y                    :"+str(fecha.strftime("%y")));
print(f"Año %Y                    :"+str(fecha.strftime("%Y")));
print(f"La hora es %I:%M:%S: %p   :"+str(fecha.strftime("%I:%M:%S: %p")));
print(f"La hora es %I:%M          :"+str(fecha.strftime("%I:%M")));
print (input("\n		continuar?"));
print('''	%a  Locale’s abbreviated weekday name.
	%A  Locale’s full weekday name.  
	%b  Locale’s abbreviated month name.
	%B  Locale’s full month name.
	%c  Locale’s appropriate date and time representation.
	%d  Day of the month as a decimal number [01,31]./
	%f  Microsecond as a decimal number [0,999999], zero-padded on the left
	%H  Hour (24-hour clock) as a decimal number [00,23].    
	%I  Hour (12-hour clock) as a decimal number [01,12].    
	%j  Day of the year as a decimal number [001,366].   
	%m  Month as a decimal number [01,12].   
	%M  Minute as a decimal number [00,59].      
	%p  Locale’s equivalent of either AM or PM.
	%S  Second as a decimal number [00,61].
	%U  Week number of the year (Sunday as the first day of the week)
	%w  Weekday as a decimal number [0(Sunday),6].   
	%W  Week number of the year (Monday as the first day of the week)
	%x  Locale’s appropriate date representation.    
	%X  Locale’s appropriate time representation.    
	%y  Year without century as a decimal number [00,99].    
	%Y  Year with century as a decimal number.   
	%z  UTC offset in the form +HHMM or -HHMM.
	%Z  Time zone name (empty string if the object is naive).    
	%%  A literal '%' character.''')
limpiar();
print(f".strftime( %a )			:"+str(fecha.strftime("%a")));
print(f".strftime( %b )			:"+str(fecha.strftime("%b")));
print(f".strftime( %c )			:"+str(fecha.strftime("%c")));
print(f".strftime( %d )			:"+str(fecha.strftime("%d")));
print(f".strftime( %e )			:"+str(fecha.strftime("%e")));
print(f".strftime( %f )			:"+str(fecha.strftime("%f")));
print(f".strftime( %g )			:"+str(fecha.strftime("%g")));
print(f".strftime( %h )			:"+str(fecha.strftime("%h")));
print(f".strftime( %j )			:"+str(fecha.strftime("%j")));
print(f".strftime( %k )			:"+str(fecha.strftime("%k")));
print(f".strftime( %l )			:"+str(fecha.strftime("%l")));
print(f".strftime( %m )			:"+str(fecha.strftime("%m")));
print(f".strftime( %p )			:"+str(fecha.strftime("%p")));
print(f".strftime( %r )			:"+str(fecha.strftime("%r")));
print(f".strftime( %s )			:"+str(fecha.strftime("%s")));
print(f".strftime( %u )			:"+str(fecha.strftime("%u")));
print(f".strftime( %w )			:"+str(fecha.strftime("%w")));
print(f".strftime( %x )			:"+str(fecha.strftime("%x")));
print(f".strftime( %y )			:"+str(fecha.strftime("%y")));
print(f".strftime( %A )			:"+str(fecha.strftime("%A")));
print(f".strftime( %B )			:"+str(fecha.strftime("%B")));
print(f".strftime( %C )			:"+str(fecha.strftime("%C")));
print(f".strftime( %D )			:"+str(fecha.strftime("%D")));
print(f".strftime( %F )			:"+str(fecha.strftime("%F")));
print(f".strftime( %G )			:"+str(fecha.strftime("%G")));
print(f".strftime( %H )			:"+str(fecha.strftime("%H")));
print(f".strftime( %I )			:"+str(fecha.strftime("%I")));
print(f".strftime( %M )			:"+str(fecha.strftime("%M")));
print(f".strftime( %R )			:"+str(fecha.strftime("%R")));
print(f".strftime( %S )			:"+str(fecha.strftime("%S")));
print(f".strftime( %T )			:"+str(fecha.strftime("%T")));
print(f".strftime( %U )			:"+str(fecha.strftime("%U")));
print(f".strftime( %V )			:"+str(fecha.strftime("%V")));
print(f".strftime( %W )			:"+str(fecha.strftime("%W")));
print(f".strftime( %X )			:"+str(fecha.strftime("%X")));
print(f".strftime( %Y )			:"+str(fecha.strftime("%Y")));
nuevo(1);
#################################################################
#Clase_fechas_Ej_002
import calendar
año=int(input("Año :"))
mes=int(input("Mes (en numeros):"))

calendario = calendar.month(año, mes)
print(f"Verifique por favor:\n {calendario}")
nuevo(2);
#################################################################
#Clase_fechas_Ej_003
a = datetime.time()
print("a =", a)

fecha = datetime.datetime.now()
#fecha2 = fecha(fecha,"%d %m, %Y")
fecha2 = (fecha.strftime("%x"));
print(f"Fecha %x		 	:"+str(fecha.strftime("%F")));
#		a = time.strptime('my date', "%b %d %Y %H:%M")
print(f"La fecha es 			:{fecha2}")


# time(hour, minute and second)
b = datetime.time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = datetime.time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = datetime.time(11, 34, 56, 234566)
print("d =", d)
nuevo(3);
#################################################################
#Clase_fechas_Ej_004
now = datetime.datetime.now()

print
print ("Current date and time using str method of datetime object:");
print (str(now));

print
print ("Current date and time using instance attributes:");
print ("Current year: %d" % now.year);
print ("Current month: %d" % now.month);
print ("Current day: %d" % now.day);
print ("Current hour: %d" % now.hour);
print ("Current minute: %d" % now.minute);
print ("Current second: %d" % now.second);
print ("Current microsecond: %d" % now.microsecond);

print ("Current date and time using strftime:");
print (now.strftime("%Y-%m-%d %H:%M"));

print ("Current date and time using isoformat:");
print (now.isoformat());

nuevo(4);
#################################################################
#Clase_fechas_Ej_005

from datetime import date
from datetime import time
from datetime import datetime




def main():
	##DATETIME OBJECTS
	#Get today's date from datetime class
	today=datetime.now()
	#print today
	# Get the current time
	#t = datetime.time(datetime.now())
	#print ("The current time is", t
	#weekday returns 0 (monday) through 6 (sunday)
	wd = date.weekday(today)
	#Days start at 0 for monday
	days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
	print (f"Today is day number %d" % wd)
	print (f"which is a " + days[wd])
main()
nuevo(5);
#################################################################
#Clase_fechas_Ej_006
from datetime import date
i_date = date(2019, 11, 2)
f_date = date(2019, 11, 11)
print("fecha inicial: ",i_date)
print("fecha final: ",f_date)
delta = f_date - i_date
print("diferencias entre fechas",delta.days)
nuevo(6);
#################################################################
#Clase_fechas_Ej_007
from datetime import datetime

#datetime(year, month, day)
paso_fecha_a_string = datetime(2018, 11, 28)
print(paso_fecha_a_string)

# datetime(year, month, day, hour, minute, second, microsecond)
paso_fechahora_a_string = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(paso_fechahora_a_string)

nuevo(7);
#################################################################
#Clase_fechas_Ej_008
from datetime import datetime
hoy = datetime.now()    # Fecha y hora actual

print(hoy)
print(hoy.year)         # año
print(hoy.month)        # mes
print(hoy.day)          # día

print(hoy.hour)         # hora
print(hoy.minute)       # minutos
print(hoy.second)       # segundos
print(hoy.microsecond)  # microsegundos

print("{}:{}:{}".format(hoy.hour, hoy.minute, hoy.second))
print("{}/{}/{}".format(hoy.day, hoy.month, hoy.year))
nuevo(8);
#################################################################
#Clase_fechas_Ej_009
from datetime import datetime
from datetime import time
hora_inicio = time(18,00,0) # 
hora_finalizacion = time(22,00,00) # 
print("hora_inicio ",hora_inicio) 
print("hora_finalizacion ",hora_finalizacion)
while True:
	actual = datetime.now()
	actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
	if actual > hora_inicio and actual < hora_finalizacion:
		print( actual )
	else:
		print("no")
		break
nuevo(9);
#################################################################
#Clase_fechas_Ej_010

print("""
Los módulos datetime y calendar amplían las posibilidades del módulo time que provee funciones para manipular expresiones de tiempo.
Al comienzo de un programa tendremos que importar estos módulos para tener acceso a un conjunto amplio de clases y funciones:
https://python-para-impacientes.blogspot.com/2014/02/operaciones-con-fechas-y-horas.html
""")
from datetime import datetime, date, time, timedelta
import calendar

print("Mostrar fecha y hora (datetime)")
ahora = datetime.now()  # Obtiene fecha y hora actual
print("Fecha y Hora:", ahora)  # Muestra fecha y hora
print("Fecha y Hora UTC:",ahora.utcnow())  # Muestra fecha/hora UTC
print("Día:",ahora.day)  # Muestra día
print("Mes:",ahora.month)  # Muestra mes
print("Año:",ahora.year)  # Muestra año
print("Hora:", ahora.hour)  # Muestra hora
print("Minutos:",ahora.minute)  # Muestra minuto
print("Segundos:", ahora.second)  # Muestra segundo
print("Microsegundos:",ahora.microsecond)  # Muestra microsegundo

print("Comparando fechas y horas (datetime, date)")
print("Horas:")
hora1 = time(10, 5, 0)  # Asigna 10h 5m 0s
print("\tHora1:", hora1)
hora2 = time(23, 15, 0)  # Asigna 23h 15m 0s
print("\tHora2:", hora2)

# Compara horas
print("\tHora1 < Hora2:", hora1 < hora2)  # True

print("Fechas:")
fecha1 = date.today()  # Asigna fecha actual
print("\tFecha1:", fecha1)

# Suma a la fecha actual 2 días
fecha2 = date.today() + timedelta(days=2)
print("\tFecha2:", fecha2)

# Compara fechas
print("\tFecha1 > Fecha2:", fecha1 > fecha2)  # False

nuevo(10);
#################################################################
#Clase_fechas_Ej_011

# Asigna formato de ejemplo1
formato1 = "%a %b %d %H:%M:%S %Y"

# Asigna formato de ejemplo2
formato2 = "%d-%m-%y %I:%m %p"

hoy = datetime.today()  # Asigna fecha-hora

# Muestra fecha-hora según ISO 8601
print("Fecha en formato ISO 8601:", hoy)

# Aplica formato ejemplo1
cadena1 = hoy.strftime(formato1)  

# Aplica formato ejemplo2
cadena2 = hoy.strftime(formato2)  

# Muestra fecha-hora según ejemplo1
print("Formato1:", cadena1)

# Muestra fecha-hora según ejemplo2
print("Formato2:", cadena2)

print("Para convertir una cadena a objeto datetime")

objeto_datetime = datetime.strptime(cadena1, formato1)
print("strptime:", fecha1.strftime(formato1))

nuevo(11);
#################################################################
#Clase_fechas_Ej_012
from datetime import datetime,timedelta


print("Operaciones con fechas y horas")
print("Se utiliza la función timedelta que permite operar con: microseconds, milliseconds, seconds, minutes, hours, days y weeks")

hoy = date.today()  # Asigna fecha actual

dias_menos = timedelta(days=1)
ayer = hoy - dias_menos # Resta a fecha actual 1 día
print("Ayer", ayer)
dias_mas = timedelta(days=1)
mañana = hoy + dias_mas  # Suma a fecha actual 1 día
print("Mañana", mañana)
diferencia_en_dias = hoy  - ayer # Resta las dos fechas

nuevo(12);
#################################################################
#Clase_fechas_Ej_013
print("Otros ejemplos de operaciones con otras unidades de tiempo")

hoy_mas_1_millon_segundos = hoy + timedelta(seconds=1000000)
ahora = datetime.now() 
hora_actual = time(ahora.hour, ahora.minute, ahora.second)
mas_5m = ahora + timedelta(seconds=300)
mas_5m = time(mas_5m.hour, mas_5m.minute, mas_5m.second)
racion_de_5h = timedelta(hours=5)
mas_5h = ahora + racion_de_5h

print("Ayer:", ayer)
print("Hoy:", hoy)
print("Mañana:", mañana)
print("Diferencia en días entre mañana y hoy:", 
      diferencia_en_dias.days)
print("La fecha de hoy más 1 millón de segundos:", 
      hoy_mas_1_millon_segundos)
print("Hora actual:", hora_actual)
print("Hora actual + 5 minutos:", mas_5m)
print("Hora actual + 5 horas:", mas_5h)
nuevo(13);
#################################################################
#Clase_fechas_Ej_014
print("Diferencia entre dos fechas (datetime)")

# Asigna datetime de la fecha actual
fecha1 = datetime.now()

# Asigna datetime específica
fecha2 = datetime(1995, 11, 5, 0, 0, 0)
diferencia = fecha1 - fecha2
print("Fecha1:", fecha1)
print("Fecha2:", fecha2)
print("Diferencia:", diferencia)
print("Entre las 2 fechas hay ", 
      diferencia.days, 
      "días y ", 
      diferencia.seconds, 
      "seg.")
nuevo(14);
#################################################################
#Clase_fechas_Ej_015
print("Diferencia entre dos fechas en días (datetime y strptime)")

formato_fecha = "%d-%m-%Y"
fecha_inicial = datetime.strptime("01-10-2013", 
                                  formato_fecha)
fecha_final = datetime.strptime("25-12-2013", 
                                formato_fecha)
diferencia = fecha_final - fecha_inicial
print("Fecha inicial:", fecha_inicial)
print("Fecha final:", fecha_final)
print("Diferencia:", diferencia.days, "días")
nuevo(15);
#################################################################
#Clase_fechas_Ej_016
print("Diferencia de dos fechas en días, introducidas por teclado")

from datetime import datetime

def main():
# Establecer formato de las fechas a introducir: dd/mm/aaaa
	formato = "%d/%m/%Y"
# Bucle 'sin fin' 
	while True:
		try:
	# Introducir fecha inicial utilizando el formato definido
			fecha_desde = input('Introducir fecha inicial (dd/mm/aaaa): ')   
	# Si no se introduce ningún valor se fuerza el final del bucle 
			if fecha_desde == "":
				break
	# Introducir fecha final utilizando el formato definido   
			fecha_hasta = input('Introducir fecha final   (dd/mm/aaaa): ') 
	# Si no se introduce ningún valor se fuerza el final del bucle 
			if fecha_hasta == "":
				break
	# Se evaluan las fechas según el formato dd/mm/aaaa
	# En caso de introducirse fechas incorrectas se capturará la excepción o error
			fecha_desde = datetime.strptime(fecha_desde, formato)
			fecha_hasta = datetime.strptime(fecha_hasta, formato)
	# Se comprueba que fecha_hasta sea mayor o igual que fecha_desde
			if fecha_hasta >= fecha_desde:
		# Se cálcula diferencia en día y se muestra el resultado
				diferencia = fecha_hasta - fecha_desde
				print("Diferencia:", diferencia.days, "días")
			else:
				print("La fecha fecha final debe ser mayor o igual que la inicial")
		except:
			print('Error en la/s fecha/s. ¡Inténtalo de nuevo!')
			return 0

if __name__ == '__main__':
	main()
nuevo(16);
#################################################################
#Clase_fechas_Ej_017
print("A partir de una hora se obtiene fracción del día")
# A partir de una hora introducida por teclado se obtiene
# fracción del día, teniendo en cuenta que 24 horas = 86400 seg
# Formato de entrada: hh:mm:ss
# Valores Hora...: 0 a 23
# Valores Minuto.: 0 a 59
# Valores Segundo: 0 a 59

from datetime import datetime
formato = "%H:%M:%S"
while True:
	try:
		hhmmss = input('Introducir hora (hh:mm:ss): ')
		if hhmmss == "":
			break
		hhmmss = datetime.strptime(hhmmss, formato)
		horas = hhmmss.hour
		minutos = hhmmss.minute
		segundos = hhmmss.second
		hhmmss_seg = (horas * 60 * 60) + (minutos * 60) + segundos 
		resultado = float(hhmmss_seg / 86400)
		print("Resultado: ", resultado)
	except:
		print('Error en el formato de hora introducido.')
		print('-> Formato válido: hh:mm:ss  ¡Inténtalo de nuevo!')
nuevo(17);
#################################################################
#Clase_fechas_Ej_018
print("Diferencia de dos fechas (date)")
hoy = date.today()
navidad_año_proximo = date(2024, 12, 25)
faltan = navidad_año_proximo - hoy
print ("Hoy:", hoy)
print ("La navidad del 2024", navidad_año_proximo)
print ("Faltan", faltan.days, "días")

print("Expresar una fecha en formato largo")
print("Hoy es...", datetime.ctime(fecha1))
print("A partir de una fecha se obtiene tupla con año, nº semana y día de semana")

print("Fecha", fecha1, 
      "Año, nº sem., día sem.:", 
      datetime.isocalendar(fecha1))
print("A partir de una fecha se obtiene tupla con año, nº semana y día de semana")
print("También, se muestra el día de la semana en letras (abreviado).")

print("Desglose de la fecha", fecha2,":")
tupla_mensajes = ("Año", "Núm. semana", "Núm. día de semana")
tupla_valores = datetime.isocalendar(fecha2)
tupla_diassem = ("Lun", "Mar", "Mié", "Jue","Vie", "Sáb","Dom")
for mensaje,valor in zip(tupla_mensajes, tupla_valores):
 print(mensaje,"-->", valor)
 
print("Día de semana-->", tupla_diassem[tupla_valores[2]-1])
nuevo(18,"inicio");
#################################################################


print("Obtener día de la semana por su número ")
print("La función weekday() devuelve el número de día de la semana a que corresponda la fecha indicada, según los siguientes valores por día:  0-Lunes, 1-Martes, 2-Miércoles, 3-Jueves, 4-Viernes , 5-Sábado y 6-Domingo")

dia_semana = datetime.weekday(fecha1)
print(fecha1, "->", dia_semana,"->", 
      tupla_diassem[dia_semana])

print("Obtener y contar los días que sean martes entre dos fechas")
nuevo(18);
#################################################################
#Clase_fechas_Ej_019
from datetime import datetime, timedelta

formato = "%d/%m/%Y"
contador = 0            
fechadesde = input('Fecha desde (dd/mm/aaaa): ')
fechahasta = input('Fecha hasta (dd/mm/aaaa): ')
if fechadesde == '' or fechahasta == '':
    exit()

try:                    
    fechadesde = datetime.strptime(fechadesde, formato)
    fechahasta = datetime.strptime(fechahasta, formato)    
    if fechadesde > fechahasta:
        print('Fecha desde debe ser menor o igual que hasta')
    
    while fechadesde <= fechahasta:
        if datetime.weekday(fechadesde) == 1: 
            contador +=1
            fechaactual = fechadesde.strftime(formato)
            print(contador, fechaactual, 'es martes')
        fechadesde = fechadesde + timedelta(days=1)
                
except:
	print('Fecha incorrecta')
nuevo(19);
#################################################################
#Clase_fechas_Ej_020
print("La función isoweekday() devuelve el número de día de la semana a que corresponda la fecha indicada, según los siguientes valores por día:  1-Lunes, 2-Martes, 3-Miércoles, 4-Jueves, 5-Viernes, 6-Sábado y 7-Domingo.")

dia_semana = datetime.isoweekday(fecha1)
print(fecha1, "->", dia_semana,"->", 
	tupla_diassem[dia_semana-1])
nuevo(20);
#################################################################
#Clase_fechas_Ej_021
print("Dado el ordinal se obtiene la fecha correspondiente")
print("Si la fecha 01-01-0001 tiene el ordinal 1 entonces...")
for num in range(1,7):
	print("El día", 10 ** num , "se corresponde con", date.fromordinal(10 ** num))
nuevo(21);
#################################################################
#Clase_fechas_Ej_022
print("Dada una fecha se obtiene un ordinal (01-01-0001 -> 1)")

fecha3 = datetime(1, 1, 1, 0, 0, 0)
print("La fecha", fecha3, "tiene el ordinal", date.toordinal(fecha3))
print("La fecha", fecha1, "tiene el ordinal", date.toordinal(fecha1))
nuevo(22);
#################################################################
#Clase_fechas_Ej_023
print("Obtener una tupla a partir de fecha-hora (datetime)")

tupla_fechahora = fecha1.timetuple()
for elemento in tupla_fechahora:
	print(elemento)
nuevo(23);
#################################################################
#Clase_fechas_Ej_024
print("Convertir un ordinal en fecha-hora (fromtimestamp)")
print("El ordinal 0 se corresponde con la fecha -> 1-1-1970 01:00:00")

print("Ordinal 0 -> 1-1-1970 01:00:00")
ordinales_tiempo = (0, 1, 2, 60, 3600)
for elemento in ordinales_tiempo:
    print(elemento, "->" , datetime.fromtimestamp(elemento))

nuevo(24);
#################################################################
#Clase_fechas_Ej_025
print("Obtener calendario del mes actual (calendar.month)")

año = date.today().year 
mes = date.today().month
calendario_mes = calendar.month(año, mes)
print(calendario_mes)

nuevo(25);
#################################################################
#Clase_fechas_Ej_026
print("Obtener calendario del mes actual (calendar.TextCalendar)");
print("Se establece el lunes como primer día de la semana");

calendario = calendar.TextCalendar(calendar.MONDAY)
calendario.prmonth(año, mes)

limpiar();
#################################################################

print("Obtener matriz con calendario de mes actual: (Calendar monthdayscalendar)");

calendario = calendar.Calendar()
for elemento in calendario.monthdayscalendar(año, mes):
    print(elemento)

nuevo(26);
#################################################################
#Clase_fechas_Ej_027
print("Obtener matriz de tuplas con calendario: (Calendar monthdays2calendar)");
print("El primer valor de cada par es el número de día del mes y el segundo valor se corresponde con el número de día de la semana: 0:lunes, 1:martes, 2:miércoles, etc.");

calendario = calendario.monthdays2calendar(año, mes)
for elemento in calendario:
    print(elemento)

print("Calendario completo del año 2018");
print("Día de comienzo: Lunes");

print(calendar.TextCalendar(calendar.MONDAY).formatyear(2018, 2, 1, 1, 2))
nuevo(27);
#################################################################
#Clase_fechas_Ej_028
print("https://steemit.com/spanish/@sethroot/aritmetica-de-fechas-con-python-aprende-a-programar")
from datetime import datetime,timedelta
hoy = datetime.now()#fecha actual

print (hoy)
print (hoy.date())

dias = timedelta(days=5)
hoy_mas_5_dias = hoy + dias # sumamos 5 Dias

print (hoy_mas_5_dias)
print (hoy_mas_5_dias.date())
# Para restar solo debemos cambiar el signo

dias = timedelta(days=15)
hoy_menos_dias = hoy - dias

print (hoy_menos_dias)
print (hoy_menos_dias.date())
nuevo(28);
#################################################################
#Clase_fechas_Ej_029
print ("""
		date          Segundo Apellidoja con Fechas
		datetime      Manipula fechas con Tiempo
		dateutils  	  Manipula meses o años""")
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
#                     espacios sin ceros
fecha = datetime(2019, 4, 4)

month = relativedelta(months=15)
hoy_menos_meses = fecha - month
hoy_mas_meses = fecha + month

print (hoy_menos_meses)
print (hoy_mas_meses)
nuevo(29);
#################################################################
#Clase_fechas_Ej_030
print ("""
Con esto estamos sumando 15 meses a la fecha 2017,04,02 con lo que nos imprime 2016-01-02 00:00:00 
y 2018-07-02 00:00:0 la primera para la resta de 15 meses y la segunda para la suma de 15 meses, 
podríamos agregar un input para agregar manualmente los meses.
""")
fecha = datetime(2019, 4, 4)
years = relativedelta(years=15)
hoy_menos_meses = fecha - years
hoy_mas_meses = fecha + years
print (hoy_menos_meses)
print (hoy_mas_meses)
nuevo(30);
#################################################################
#Clase_fechas_Ej_031
print ("""
Podemos pasarle .date  al final de las variables para obtener solo las fechas:
""")
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

fecha = datetime(2019, 4, 4)
month = relativedelta(months=15)
hoy_menos_meses = fecha - month
hoy_mas_meses = fecha + month

print (hoy_menos_meses.date())
print (hoy_mas_meses.date())

fecha = datetime(2019, 4, 4)
years = relativedelta(years=15)
hoy_menos_meses = fecha - years
hoy_mas_meses = fecha + years

print (hoy_menos_meses.date())
print (hoy_mas_meses.date())
nuevo(31,"fin");
#################################################################

