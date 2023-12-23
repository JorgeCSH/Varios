# Archivo creado para calcular prioridad academica ##########################################################
#############################################################################################################
# Imports que pueden ser utilizados #########################################################################
#############################################################################################################
from datetime import date
import matplotlib.pyplot as plt

#############################################################################################################
# Codigo ####################################################################################################
#############################################################################################################

def prioridad(creditos_curso, notas, creditos_aprobados, semestres_cursados, creditos_reprobados):

    if not len(creditos_curso) == len(notas):
        print('Datos qls que pusiste ')

    else:
        def parametro_1(semestres_cursados):
            parametro1num = (1666.7)
            parametro1den = (24*((semestres_cursados)**(1.26)))
            parametro1 = (parametro1num)/(parametro1den)
            return parametro1

        def parametro_2(creditos_curso, notas, creditos_aprobados):
            parametro21 = 0
            for i in range(len(creditos_curso)):
                parametro21 += creditos_curso[i]*notas[i]
            parametro22 = sum(creditos_aprobados)
            parametro2 = parametro21 - parametro22
            return parametro2

        def parametro_3(creditos_aprobados, creditos_inscritos):
            parametro3num = sum(creditos_aprobados)
            parametro3den = creditos_inscritos
            parametro3 = (parametro3num)/(parametro3den)
            return parametro3

        creditos_inscritos = sum(creditos_aprobados) + sum(creditos_reprobados)
        p1 = parametro_1(semestres_cursados)
        p2 = parametro_2(creditos_curso, notas, creditos_aprobados)
        p3 = parametro_3(creditos_aprobados, creditos_inscritos)
        prioridad = p1*p2*p3
        return prioridad


semestres_cursados = 4
primer_semestre = [[6, 6, 6, 6, 3, 3], [4.9, 4.8, 6.3, 6.1, 6.6, 5.5], []]
segundo_semestre = [[6, 6, 6, 6, 3, 3], [5.8, 5.6, 6.1, 5.8, 6.2, 5.6], []]
tercer_semestre = [[6, 6, 6, 6, 6], [4.5, 4.6, 5.2, 5.0, 5.4], []]
cuarto_semestre = [[6, 6, 6, 6, 3 , 3], [6.0, 4.6, 5.4, 5.3, 5.2, 6.6], []]
cr_curso = primer_semestre[0]+segundo_semestre[0]+tercer_semestre[0]+cuarto_semestre[0]
notas = primer_semestre[1]+segundo_semestre[1]+tercer_semestre[1]+cuarto_semestre[1]
cr_aprobados = cr_curso
cr_reprobado = primer_semestre[2]+segundo_semestre[2]+tercer_semestre[2]+cuarto_semestre[2]
print()

prioridad_Final = prioridad(cr_curso, notas, cr_aprobados, semestres_cursados, cr_reprobado)
print('La prioridad por tu rendimiento (flojo ql) esta dada por el siguiente valor para este semestre: '+str(prioridad_Final))


prior1 = prioridad(primer_semestre[0], primer_semestre[1], primer_semestre[0], 1, primer_semestre[2])

prior2 = prioridad(primer_semestre[0]+segundo_semestre[0], primer_semestre[1]+segundo_semestre[1],
                   primer_semestre[0]+segundo_semestre[0], 2, primer_semestre[2]+segundo_semestre[2])

prior3 = prioridad(primer_semestre[0]+segundo_semestre[0]+tercer_semestre[0],
                            primer_semestre[1]+segundo_semestre[1]+tercer_semestre[1],
                   primer_semestre[0]+segundo_semestre[0]+tercer_semestre[0], 3,
                            primer_semestre[2]+segundo_semestre[2]+tercer_semestre[2])

prior4 = prioridad(primer_semestre[0]+segundo_semestre[0]+tercer_semestre[0]+cuarto_semestre[0],
                            primer_semestre[1]+segundo_semestre[1]+tercer_semestre[1]+cuarto_semestre[1],
                   primer_semestre[0]+segundo_semestre[0]+tercer_semestre[0]+cuarto_semestre[0], 4,
                            primer_semestre[2]+segundo_semestre[2]+tercer_semestre[2]+cuarto_semestre[2])

prioridades_por_semestre = [prior1, prior2, prior3, prior4]
semestres = [1, 2, 3, 4]
print()
print('Las proridades que se han tenido en el transcurso de la carrera: ')
print('-> 1er semestre '+str(prioridades_por_semestre[0]))
print('-> 2do semestre '+str(prioridades_por_semestre[1]))
print('-> 3er semestre '+str(prioridades_por_semestre[2]))
print('-> 4er semestre '+str(prioridades_por_semestre[3]))


prioridades_por_semestregraf = [prior1, prior2, prior3, prior4, prior4, prior4, prior4, prior4, prior4, prior4, prior4]
prioridades_por_semestregraf2 = [prior1, prior2, prior3, prior4, 0, 0, 0, 0, 0, 0, 0]
semestresgraf = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
plt.figure(figsize=(6,5))
plt.plot(semestresgraf,prioridades_por_semestregraf, "green",label="Prioridades")
plt.scatter(semestresgraf, prioridades_por_semestregraf2, color = 'black')
plt.xlabel("Semestres sufriendo en esta U")
plt.ylabel("Valor de la prioridad")
plt.title("Prioridad con respecto a la \n cantidad de semestres")
plt.legend()
plt.show()

#############################################################################################################
# Creditos ###################################################################################################
#############################################################################################################
#fecha_actual = date.today()
#fecha_forma_normal = fecha_actual.strftime("%d/%m/%Y")

#print()
#print('Emition date: ', fecha_forma_normal)
#print()
#print('Developer: <Jorge Cummins>')
#print()
#print('Code designed by Jorge Cummins in Santiago, Chile')

