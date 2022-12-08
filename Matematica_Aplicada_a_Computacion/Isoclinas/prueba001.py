# Graficas de campo de pendientes python

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sympy import pprint, Symbol, Function, Derivative, dsolve, solve, diff
import sympy as sp
from sympy.interactive import printing


# Función para graficar el campo de pendientes de una función
def graficar_campo_pendientes(f, x, y):
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    plt.figure()
    plt.contour(X, Y, Z)
    plt.show()
def campo_pendientes(f, x, y):
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    return X, Y, Z 

def f1(x, y):
    return 2*y/x


# Datos de entrada
x = np.linspace(-10, 10, 100)
Y = x
X,Y = np.meshgrid(x,Y)

U = 1
V = f1(X,Y)
M = np.sqrt(U**2+V**2)
U2, V2 = U/M, V/M

# Graficar
plt.figure()
plt.quiver(X, Y, U2, V2, M, pivot='mid', cmap=plt.cm.jet)
plt.show()
