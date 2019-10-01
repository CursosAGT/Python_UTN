#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Calcula la Energía Cinética de un objeto
 
print("Este programa calcula la energía cinética para un objeto en movimiento.")

m = float( input("Introduce la masa del objeto en kilogramos: "))
v = float( input("Introduce la velocidad en metros por segundo: "))

e = 0.5 * m * v * v
print("El objeto tiene " + str(e) + " joules de energía.")
