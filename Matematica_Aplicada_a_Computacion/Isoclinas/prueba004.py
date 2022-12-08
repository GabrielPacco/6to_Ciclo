import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
from sympy import pprint, Symbol, Function, Derivative, dsolve, solve, diff
import sympy as sp
from sympy.interactive import printing
# eigenvalues and eigenvectors
from numpy import linalg as LA

def plotdf(f, xran=[-10, 10], yran=[-10, 10], grid=[21, 21], color='k'):
    """
    lote el campo de dirección para una EDO escrita en la forma 
        x' = F(x,y)
        y' = G(x,y)
    
    The functions F,G are defined in the list of strings f.
    
    Input
    -----
    f:    list of strings ["F(X,Y)", "G(X,Y)"
          F,G are functions of X and Y (capitals).
    xran: list [xmin, xmax] (optional)
    yran: list [ymin, ymax] (optional)
    grid: list [npoints_x, npoints_y] (optional)
          Defines the number of points in the x-y grid.
    color: string (optional)
          Color for the vector field (as color defined in matplotlib)
    """
    x = np.linspace(xran[0], xran[1], grid[0])
    y = np.linspace(yran[0], yran[1], grid[1])
    def dX_dt(X, Y, t=0): return map(eval, f)
    
    X , Y  = np.meshgrid(x, y)  # create a grid
    DX, DY = dX_dt(X, Y)        # compute growth rate on the grid
    M = (np.hypot(DX, DY))      # Norm of the growth rate 
    M[ M == 0] = 1.             # Avoid zero division errors 
    DX = DX/M                   # Normalize each arrows
    DY = DY/M  
      
    plt.quiver(X, Y, DX, DY, pivot='mid', color=color)
    plt.xlim(xran), plt.ylim(yran)
    plt.grid('on')


# Obtener los Autovalores y autovectores
def aut_val_vec(A):
    # Autovalores
    w, v = LA.eig(A)
    print("Autovalores: ", w)
    print("Autovectores: ", v)
    return w, v

## Example
# Plot the direction field for the Lotka-Volterra equations
# x' = 4x + 3y
# y' = x-y
plotdf(["1*X + 2*Y", "2*X + Y"], xran=[-10, 10], yran=[-10, 10], grid=[21, 21], color='k')

A = np.array([[1, 2], [2, 1]])

# Graficar los autovalores y autovectores en el plano
w, v = aut_val_vec(A)
plt.plot([0, v[0,0]], [0, v[1,0]], 'r', lw=2)
plt.plot([0, v[0,1]], [0, v[1,1]], 'r', lw=2)
plt.plot([0, w[0]], [0, w[1]], 'b', lw=2)
plt.plot([0, w[0]], [0, w[1]], 'b', lw=2)


plt.show()
