# Este es una linea de codigo provisional que cree para el lab de metodos de condensadores...
# Puede que tambien haya creado uno en EXCEL porque me quede estudiando EDO y me di cuenta a las 1 am xd.
# Por ende escribi esto rapido para no dormirme a la hora del ñauque, todo con inspiracion del piano de Cynthia en
# 4ta generacion para tener inspiracion. 

# Librerias usadas
import numpy as np
import matplotlib as plt
import math
import humanistas as lenguaje
import tocomple as italiano

####################################################################################################################

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

####################################################################################################################

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

#valores = lenguaje.dialogo(5)
#tipo = input('Tipo de conexion ')
#panconpebre = capacitanciaEq(valores,tipo)
#print(panconpebre)
#print(capacitanciaEq(['2', '44', '3', '5', '3'], '0'))

####################################################################################################################

# Clalcula el error
def calculadorError(valores):
    valorNoerr = italiano.media(valores)
    error = italiano.desvEstandar(valores, 0)
    valorYerror = np.array([valorNoerr, error])
    return valorYerror

#cANTdATos = input('Cuantos datos le meteras? ')
#print('La cantidad de operaciones son: ', cANTdATos)
#iterando = lenguaje.dialogo(cANTdATos)
#johnnyBravo = calculadorError(iterando)
#print('Los valores que ingresaste, con su error tendran un error aproximado de')
#print(johnnyBravo)

####################################################################################################################

# Opera entre Errores
def operadorError(valor1, valor2, operacion):                                                          
    a = valor1[1]                                                                      
    b = valor2[1]                                                                 
    aa = valor1[0]                                                                      
    bb = valor2[0]                                                                        
    cateto1 = (a)**2                                                                     
    cateto2 = (b)**2                                                                        
    cateta1 = (a/aa)**2                                                                    
    cateta2 = (b/bb)**2                                                                   
    operro1 = np.sqrt(cateto1 + cateto2)                                                    
    operro2 = np.sqrt(cateta1 + cateta2)                                                    
    matraca = lenguaje.erroropera(aa, bb, operro1, operro2, operacion)                      
    return matraca  

#print('Las operaciones son: ')
#print('1 = Suma')
#print('2 = Resta')
#print('3 = Multiplicacion')
#print('4 = Division')
#cacho11 = float(input('Inserte primer valor que operara (sin error) '))
#cacho12 = float(input('Inserte error del caso anterior'))
#cacho1 = np.array([cacho11, cacho12])
#cacho21 = float(input('Inserte segundo valor que operara (sin error) '))
#cacho22 = float(input('Nuevamente, inserte error del caso anterior'))
#cacho2 = np.array([cacho21, cacho22])
#pichulearCacho = int(input('Operacion que se realizara ')) 
#momentoMatraca = operadorError(cacho1, cacho2, pichulearCacho)
#print('El resultado seria:')
#print(momentoMatraca)

####################################################################################################################

#cantidadDatos = int(input('Cantidad de datos '))
#datos = lenguaje.dialogo(cantidadDatos)
#datosPeroCheveres = lenguaje.racista(datos)
#promedio = italiano.media(datos)
#print('media de datos es ', promedio)

#desviacion = italiano.desvEstandar(datos, purgador=0)
#print('La desviacion seria:', desviacion)

####################################################################################################################

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
        
# Las formad: 0 para  forma general, 1 para corriente, 2 para caida voltaje condensador, 3 caida caida voltaje resistencia
formomoa = int(input('medicion que satanica deseada '))
ts = float(input('ingrese tiempo '))
rs = float(input('ingrese resistencia'))
vs = float(input('ingrese voltaje '))
cs = float(input('ingrese capacitancia '))
cargaxconchoclo = cargas(ts, rs, vs, cs, formomoa)
print('carga seria', cargaxconchoclo)


def descarga(cargaInicial, t, r,c):
    feo = expresionSatanica(t,r,c,forma=1)
    descargat = cargaInicial*feo
    return feo

tss = float(input('ingrese tiempo '))
rss = float(input('ingrese resistencia'))
aaa = float(input('ingrese capacitancia '))
caca = float(input('ingrese carga inicial '))
descargaso = descarga(caca, tss, rss, aaa)
print('la descarga en tiempo t seria ', descargaso)

