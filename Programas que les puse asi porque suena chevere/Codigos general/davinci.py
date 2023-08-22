# Codigo hecho para tener una forma mas rapida de graficar
#################################################################################################################
# Librerias importadas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#################################################################################################################
#################################################################################################################
# Funciones que fui usando para hacer pruebas
def f(x):
    return np.sin(x)
def g(x,y):
    return np.sin(x)*np.cos(y)
def Ha(x):
    if x<0:
        return 0
    elif x>=0:
        return 1
    else:
        print('OONGA BOONGA ')
#################################################################################################################
def DaVinci(datos1, datos2, datos3, dimension, letras):
    # Inicialmente, como no sabe que vas a pedir, va pidiendo info
    # Primera funcion racista del dia
    assert type(dimension) == int

    # Caso en que le des dimensiones qls feas
    if not 0 < dimension < 3:
        print('Error en dimension, solo puede ser 1, 2 o 3 en este caso fue: '+str(dimension))
        la_parca = input('Desea continuar? ')
        if la_parca == 'si':
            DaVinci(datos1, datos2, datos3, dimension, letras)
        else:
            return None

    # Caso dimension que ingresaste sea 1, aun no hecha
    elif dimension == 1:
        pass

    # Caso dimension sea 2
    elif dimension == 2:
        modo = int(input('Que modo desea? '))
        # Pedira valores
        if modo == 0:
            titulo = letras[0]

        # Valores dados
        elif modo == 1:
            OX = datos1
            OY = datos2
            input('Ahora se va a empezar a planear el titulo, asi que atento a lo que escribas. Presiona '
                  '"Enter" para continuar ')


    # Ahora hay que empezar a definir ejes xd


    pass















#################################################################################################################
def forme():
    # Este es el codigo para un grafo en 2D
    plt.figure('Tamano')
    plt.plot('Funcion que se quiere graficar')
    plt.xlabel('Nombre Eje x')
    plt.ylabel('Nombre Eje y')
    plt.title('Titulo del grafico')
    plt.legend('Caption del grafico')
    plt.show()
    # Caso 3D
    plt.figure('tamaño')
    ax = plt.axes(projection='3d')
    ax.plot('Puntos que se van a graficar')
    ax.set_title('Titulo del grafico')
    ax.set_xlabel('Titulo del eje x')
    ax.set_ylabel('Titulo del eje y')
    ax.set_zlabel('Titulo del eje z')
    plt.show()
    pass


