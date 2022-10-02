import math

import numpy as np
from numpy.random import rand

from sympy import var
from sympy.physics.hydrogen import E_nl
from sympy.physics.hydrogen import Psi_nlm
from sympy import Symbol
from sympy.physics.hydrogen import R_nl

from pynverse import inversefunc

from mpl_toolkits.mplot3d import Axes3D

import matplotlib
from matplotlib import pyplot as pl



r=Symbol("r", real=True, positive=True)
phi=Symbol("phi", real=True)
theta=Symbol("theta", real=True)
Z=Symbol("Z", positive=True, integer=True, nonzero=True)

def sqrt(x):
    return np.sqrt(x)
def exp(x):
    return np.exp(x)

pi = math.pi

Psi = [[],[],[]]

R2=(lambda x: exp(-2*x)/pi) #Solução Estacionária de R100 do Hidrogênio

#T=(lambda x: 1/(sqrt(2*pi))
#P=(lambda x: 1/(sqrt(2)))

fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(0,20000):
    Radius = rand()
    Theta  = rand()
    Phi    = rand()

    r = inversefunc(R2,y_values=Radius) #Inverso da solução estacionária de R(r) para se determinar r

    x = r * np.sin(2*pi*Theta)*np.cos(2*pi*Phi)
    y = r * np.sin(2*pi*Theta)*np.sin(2*pi*Phi)
    z = r * np.cos(2*pi*Theta)

    Psi[0].append(x)
    Psi[1].append(y)
    Psi[2].append(z)

val = np.square(Psi[0]) + np.square(Psi[1]) + np.square(Psi[2]) #Ajuste de cores para que os pontos mais provaveis estejam mais vermelhos

cmap = matplotlib.cm.get_cmap('gist_rainbow')
normalize = matplotlib.colors.Normalize(vmin=sqrt(min(val)), vmax=sqrt(max(val)))
colors = [cmap(normalize(value)) for value in sqrt(val)]

ax.scatter(Psi[0] , Psi[1], Psi[2], c=colors, marker='o',s=1, label="$\Psi_{100}$")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
pl.legend()
pl.show()
