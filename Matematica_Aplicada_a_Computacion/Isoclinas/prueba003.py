# Trazar el campo vectorial y las curvas integrales

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sympy import pprint, Symbol, Function, Derivative, dsolve, solve, diff
import sympy as sp
from sympy.interactive import printing

printing.init_printing(use_latex = True)

f = Function('f')
x = Symbol('x')

# ODE model 1
def f1(y, x):
    dydx = 1 + x -y
    return dydx

model = f(x).diff(x) + 1 + x - f(x)
y_general = dsolve(model, f(x))

print('The general solution: ')
pprint(y_general)






