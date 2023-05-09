# Este es una linea de codigo provisional que cree para el lab de metodos de condensadores...
# Puede que tambien haya creado uno en EXCEL porque me quede estudiando EDO y me di cuenta a las 1 am xd.
# Por ende escribi esto rapido para no dormirme a la hora del ñauque, todo con inspiracion del piano de Cynthia en
# 4ta generacion para tener inspiracion. 

# Librerias usadas
import numpy as np
import matplotlib as plt
import math


def capacitancia(carga, diferenciaPoto):
    V = float(diferenciaPoto)
    Q = float(carga)
    moduloQ = abs(Q)
    C = moduloQ/V
    opa = [C, '[F] "Faradias"' ]
    return opa



