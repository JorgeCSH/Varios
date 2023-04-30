# Este doc es maomeno similar al anterior, lo unico que hace es contener funciones que 
# no tienen nada que ver, webean mucho, deterioran el orden o en casos mas brigidos, 
# me creo hacker y queria usar la opcion Import 

# Librerias usadas
import numpy as np
#import matplotlib as plt
import math



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
    
