import numpy as np
import sympy as sp
from sympy.utilities.lambdify import lambdify
from graphIt import graphIt


def rotateX(equation, radialDisplacement, x1, x2, y1, y2, z1, z2, axis):
    x = sp.symbols('x')
    equation_func = lambdify(x, equation, 'numpy')

    if equation.has(sp.sqrt):
        x_vals = np.linspace(max(0, x1), x2, 100)
    else:
        x_vals = np.linspace(x1, x2, 100)

    theta_vals = np.linspace(0, 2 * np.pi, 100) # a 3d revolution (2pi representing all 360 degrees) -> the math stolen from desmos
    X, Theta = np.meshgrid(x_vals, theta_vals)

    Y = equation_func(X)
    Y = np.clip(Y, y1, y2)


    Y = np.nan_to_num(Y, nan=0.0)

    # Rotated coordinates of the stuff
    W = (X - radialDisplacement) * np.cos(Theta) + radialDisplacement
    Z = (X - radialDisplacement) * np.sin(Theta) + radialDisplacement

    graphIt(equation, radialDisplacement, x1, x2, y1, y2, z1, z2, Y, W, Z, axis)



def rotateY(equation, radialDisplacement, x1, x2, y1, y2, z1, z2, axis):
    x = sp.symbols('x')
    equation_func = lambdify(x, equation - radialDisplacement, 'numpy')

    if equation.has(sp.sqrt): # cuz no negatives, we don't wanna deal with that
        x_vals = np.linspace(max(0, x1), x2, 100)
    else:
        x_vals = np.linspace(x1, x2, 100)

    theta_vals = np.linspace(0, 2 * np.pi, 100)
    X, Theta = np.meshgrid(x_vals, theta_vals)

    Y_raw = equation_func(X)
    Y_raw = np.nan_to_num(Y_raw, nan=0.0)
    Y_raw = np.clip(Y_raw, y1, y2)

    W = X
    Y = Y_raw * np.cos(Theta)
    Z = Y_raw * np.sin(Theta)


    graphIt(equation, radialDisplacement, x1, x2, y1, y2, z1, z2, Y, W, Z, axis)
