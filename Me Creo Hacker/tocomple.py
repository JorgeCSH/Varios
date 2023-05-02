# Este doc es maomeno similar al anterior, lo unico que hace es contener funciones que 
# no tienen nada que ver, webean mucho, deterioran el orden o en casos mas brigidos, 
# me creo hacker y queria usar la opcion Import 

# Librerias usadas
import numpy as np
#import matplotlib as plt
import math
import humanistas as lenguaje



# Funcion encargada de realizar la operacion final cuando se tratan variables con error asociado
# "noerroa y noerrob" son las variables sin contar su error asociado
# "erro1 y erro2" son el error asociado
# "operacion" es la operacion a realizar {1, 2, 3, 4} son {suma, resta, mult, div}
def erroropera(noerroa, noerrob, erro1, erro2, operacion):
    if operacion==1:
        final = noerroa + noerrob
        valors = np.array([final, erro1])
        return valors
    elif operacion == 2:
        final = noerroa - noerrob
        valorr = np.array([final, erro1])
        return valorr
    elif operacion == 3:
        final = noerroa*noerrob
        valorp = np.array([final, final*erro2])
        return valorp
    elif operacion == 4:
        final = noerroa/noerrob
        valord = np.array([final, final*erro2])
        return valord
    else:
        return 'soi weon o te haci?'
    


# Funcion que saca la media de una lista de datos
# Recibe una lista, cuenta la cantidad de datos, suma los datos y los divide
# Debe haber otra, pero preferi irme a la segura 
# "datos" es la lista de datos que se quiere obtener la media
def media(datos):
    cantDatos = len(datos)
    sumaDatos = 0
    i = 0
    while i < cantDatos:
        if i == cantDatos:
            break
        else:
            sumat = sumaDatos + datos[i]
            sumaDatos = sumat
            i = i+1
        media = sumaDatos/cantDatos
    return media    



# Funcion que calcula la desviacon estandar para cada una lista de valores. 
# Dependiendo de que se este estudiando, se debe seleccionar de que tipo de 
# datos se habla. 
# "datos" es la lista de datos a operar
# "purgador" es el tipo de muestra que se esta tratando. estas serian
# 0, si es poblacion (T O D O  EL ESPACIO) y 1, si es una muestra del espacio
def desvEstandar(datos, purgador):
    promedio = media(datos)
    cantDatos = len(datos) 
    suma = 0
    i = 0
    while i<cantDatos:
        if i == cantDatos:
            break 
        else: 
            operatoria = (datos[i]-promedio)**2
            sumat = suma + operatoria
            suma = sumat
            i = i+1
    if purgador == 0:
        total = cantDatos
        megaPromedio = sumat/(total)
        desviacion = np.sqrt(megaPromedio)
    elif purgador == 1:
        total = cantDatos - 1
        megaPromedio = sumat/(total)
        desviacion = np.sqrt(megaPromedio)
    else: 
        desviacion = 'agilao'
    return desviacion 



def regresion(OX, OY):
    cantidad = len(OX)
    xo = lenguaje.racista(OX)
    xocuadrado = []
    yo = lenguaje.racista(OY)
    sumaxy = [] 
    xi = sum(xo)
    yi = sum(yo)
    i = 0
    j = 0
    while i <len(xo):
        if i == len(xo):
            break
        else:
            oxo = xocuadrado + [xo[i]**2]
            xocuadrado = oxo
        xo2 = xocuadrado
    while j <len(xo):
        if j == len(xo):
            break
        else:
            oxy = sumaxy + [(xo[j])*(yo[j])]
            sumaxy = oxy
        xy = sumaxy           
    numa = xi*yi - cantidad*(sum(xy))
    dena = ((xi)**2) - (cantidad*(sum(xo2)))
    a = numa/dena
    numb = yi - a*xi
    denb = cantidad
    b = numb/denb
    ajuste = np.array([a, b])
    return ajuste

ejex = ['14.222', '17.493', '21.477', '26.104', '27.611', '33.506', '41.188', '40.953']
ejey = ['95.065', '113.860', '138.663', '155.955', '172.485', '196.024', '220.230', '254.771']
popo = regresion(ejex, ejey)
aa = popo
print(popo)
         
