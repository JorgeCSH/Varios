def nice(i=1):
    numero = int(input('Inserte Numero '))
    while not numero == 69:
        return nice(i=i+1)
    else:
        if i == 1:
            print('Te demoraste 1 intentos en darte cuenta de esto, ¡Felicitaciones!... nice')
        else:
            print('Te demoraste ' + str(i) + ' intentos en darte cuenta de esto, nice')


nice()
