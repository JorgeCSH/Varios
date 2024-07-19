# El prescente documento fue hecho con el fin de ser
# variables simples de estudio (pese ha que hay
# EDO).
# Especificamente en este caso seria el 4to documento
########################################################################################################################
########################################################################################################################
# Librerias usadas
import numpy as np


########################################################################################################################
########################################################################################################################
# Capacitancias y/o condensadores en circuitos electricos

# Capacitancia: mide la capacitancia en tornoa una medicion
# de voltaje en ti mismo
def capacitancia(carga, diferenciaPoto):
    V = float(diferenciaPoto)
    Q = float(carga)
    moduloQ = abs(Q)
    C = moduloQ/V
    opa = [C, '[F] "Faradias"' ]
    return opa


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

# Clalcula el error






def expresionSatanica(tiempo, resistencia, capacitancia, forma):
    exponente = (-(tiempo)/(resistencia+capacitancia))
    e = np.exp(exponente)
    if forma == 0:
        satanMismo = (1-e)
    elif forma == 1:
        satanMismo = e
    else:
        'Gil '
    return satanMismo


def cargas(t, R, V, C, medicion):
    if medicion == 0:
        carga = C*R*expresionSatanica(t,R,C,forma=0)
    elif medicion == 1:
        carga = (V/R)*expresionSatanica(t,R,C,forma=1)
    elif medicion == 2:
        carga = V*expresionSatanica(t,R,C,forma=0)
    elif medicion == 3:
        carga = V*expresionSatanica(t,R,C,forma=1)
    else: 
        'xd'
    return carga


def descarga(cargaInicial, t, r,c):
    feo = expresionSatanica(t,r,c,forma=1)
    descargat = cargaInicial*feo
    return feo
########################################################################################################################
########################################################################################################################



