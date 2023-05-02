# Este doc esta para guardar codigos creados que, no necesariamente
# estaban para calcular. Por ejemplo dialogo o wear a las listas.

# Librerias usadas
import numpy as np
#import matplotlib as plt
import math



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




# print(obo)
# print('arriba', obo[0])
# print('abajo', obo[1])
# Esta abominacion del demonio se deberia de encargar de iterar los datos solicitados.
# Recibe la cantidad de datos que le vas a meter por la raja y te pide esa cantidad 
# de veces los datos
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
    