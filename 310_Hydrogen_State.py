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


#R2=(lambda x: ((8/(27*sqrt(6)))*(1-x/6)*x*exp(-x/3))**2)

c1=((64/(27**2))/6)

R2=(lambda x: c1*((3/8)*(711-exp(-(2/3)*x)*(2*x*(x*(2*x*(x+9)+79)+237)+711))))

#R2=(lambda x: c1*((3/4)*(2*x**4+12*x**3+54*x**x+162*x+243)*exp(-(2/3)*x)+(9/8)*(4*x**3+18*x**2+54*x+81)*exp(-(2/3)*x) - (3/4)*(2*x**2+6*x+9)*exp(-(2/3)*x)))

#R2=(lambda x: -(1/24)*(x**2+2*x+2)*exp(-x))

#T2=(lambda x: (3/(4*pi))*(np.cos(x))**2)
T2=(lambda x: (3/(16*pi))*(2*x+np.sin(2*x)))
#P=(lambda x: 1/(sqrt(2)))


fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(0,20000):
    Radius = rand()
    Theta  = rand()
    Phi    = 2*pi*rand()

    r = inversefunc(R2,y_values=Radius)
    th = inversefunc(T2,y_values=Theta)
    phi = 2*pi*rand()

    #th = np.arccos(sqrt(((4*pi)/3*Theta)))
    #th = np.arccos(Theta)

    x = r * np.sin(th)*np.cos(phi)
    y = r * np.sin(th)*np.sin(phi)
    z = r * np.cos(th)

    Psi[0].append(x)
    Psi[1].append(y)
    Psi[2].append(z)


val = np.square(Psi[0]) + np.square(Psi[1]) + np.square(Psi[2])

cmap = matplotlib.cm.get_cmap('gist_rainbow')
normalize = matplotlib.colors.Normalize(vmin=sqrt(min(val)), vmax=sqrt(max(val)))
colors = [cmap(normalize(value)) for value in sqrt(val)]

ax.scatter(Psi[0] , Psi[1], Psi[2], c=colors, marker='o',s=1)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

pl.show()
