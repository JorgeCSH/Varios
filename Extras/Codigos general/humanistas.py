# Este doc esta para guardar codigos creados que, no necesariamente
# estaban para calcular. Por ejemplo dialogo o wear a las listas.
# Este documento formalmente se encargara de contener todos los codigos
# relacionados desde con interaccion, hasta lenguaje (xd)
########################################################################################################################
########################################################################################################################
# Librerias usadas
import numpy as np
import matplotlib as plt
import math
########################################################################################################################
########################################################################################################################
# Funciones de texto o interaccion

# Funcion que toma lista que deberia ser numero pero estan en str.
# Esta para casos como los inputs, en que solo reciben (y si no los transforman)
# en str.
def racista(lista):
    n = len(lista)
    tetas = []
    i = 0
    while i<n:
        if i == n:
            break
        else: 
            poronga = tetas + [float(lista[i])]
            tetas = poronga
            i = i+1
    return tetas


# Funcion la cual te pide una cantidad "cantDatos" veces un dato
# repetido
def dialogo(cantDatos):
    canWena = int(cantDatos)
    tot = []
    i = 0
    while i<canWena:
        if i == canWena:
            break
        else:
            valori = input('Ingrese Valor ')
            valora = float(valori)
            tota = tot +[valora]
            tot = tota
            i = i+1
        total = tot
    return total
########################################################################################################################
########################################################################################################################