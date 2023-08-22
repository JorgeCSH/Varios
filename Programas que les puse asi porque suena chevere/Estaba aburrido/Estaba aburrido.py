# Estaba aburrido y decidi programar algunas weas #########################################################
###########################################################################################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp



def f(xij):
    a = float(np.random.uniform(-10, 10, 1))
    b = float(np.random.uniform(-10, 10, 1))
    x = xij[0]
    y = xij[1]
    parametroxy = (y**2)-(x**3)
    parametrocte = (a*x)+b
    f = (parametroxy-parametrocte)*(np.sin(x+y))
    return f



x = np.linspace(-1,1,101)
y = np.linspace(-1,1,101)
XX,YY = np.meshgrid(x, y)
Z=np.zeros((101,101))
Z2=np.zeros((101,101))
dimplanoX = len(XX)
dimplanoY = len(YY)
plano = range(dimplanoX)
planoL = []
k = 0

# Definir un espacio
while k < len(XX):
      planox = planoL + [k]
      planoL = planox
      k = k + 1
planoR = planoL


for i in planoR :
    for j in planoR:
        xij=[XX[i,j],YY[i,j]]
        Z[i,j]=f(xij)
ax = plt.axes(projection='3d')
ax.plot_surface(XX,YY,Z, cmap='prism')
ax.set_title('Esto lo hice solo para dar un paro cardiaco \n Ecuacion: $f(x,y) = (y^{2}-x^{2}-ax-b)\sin(x+y)$+crayones ')
ax.set_xlabel('OX')
ax.set_ylabel('OY')
ax.set_zlabel('OZ')
plt.show()


