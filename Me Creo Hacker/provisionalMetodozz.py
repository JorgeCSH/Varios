# Este es una linea de codigo provisional que cree para el lab de metodos de condensadores...
# Puede que tambien haya creado uno en EXCEL porque me quede estudiando EDO y me di cuenta a las 1 am xd.
# Por ende escribi esto rapido para no dormirme a la hora del ñauque, todo con inspiracion del piano de Cynthia en
# 4ta generacion para tener inspiracion. 

# Librerias usadas
import numpy as np
import matplotlib as plt
import math
import humanistas as lenguaje


def capacitancia(carga, diferenciaPoto):
    V = float(diferenciaPoto)
    Q = float(carga)
    moduloQ = abs(Q)
    C = moduloQ/V
    opa = [C, '[F] "Faradias"' ]
    return opa

#x = input('Ingrese Capacitancia ')
#d = input ('Ingrese Diferencia de potencial ')
#motodozzzzzzz = capacitancia(x, d)
#print(motodozzzzzzz)



# Tipo es si serie paralelo o que wea sea..... 
# 0 si es en serie, 1 si es en paralelo
def capacitanciaEq(totalcapac, tipox, i=0):
    tipo = int(float(tipox)//1)
    if tipo == 0: 
        largo = len(totalcapac)
        sixsixsixthenumberofthebeast = []
        while i < largo:
            if i == largo: 
                break
            else: 
                valor = float(totalcapac[i])
                valorMatraca = 1/valor
                runtothehills = sixsixsixthenumberofthebeast + [valorMatraca]
                sixsixsixthenumberofthebeast = runtothehills
                i = i+1
            cs = sixsixsixthenumberofthebeast
    elif tipo == 1: 
        largo = len(totalcapac)
        ironMan = []
        while i < largo:
            if i == largo: 
                break
            else: 
                valor = float(totalcapac[i])
                nib = ironMan + [valor] 
                ironMan = nib
                i = i+1
            cs = ironMan
    equivalente = sum(cs)
    if tipo == 0:
        ceq = 1/equivalente
        return ceq
    elif tipo == 1:
        ceq = equivalente 
        return ceq
    else: 
        return 'momento xd'

valores = lenguaje.dialogo(5)
tipo = input('Tipo de conexion ')
panconpebre = capacitanciaEq(valores,tipo)
print(panconpebre)
#print(capacitanciaEq(['2', '44', '3', '5', '3'], '0'))







