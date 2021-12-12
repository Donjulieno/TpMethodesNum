from sympy import *
from math import *
import numpy as np
from matplotlib.pylab import *
from scipy.integrate import odeint
from scipy.integrate import solve_ivp


def Chebycheff (F,n):

    #y_calc = np.zeros((interval,1))
    #print(y_calc)
    sol = float(0)
    for i in range (0,n+1):

        z = cos((2*i+1))*(math.pi/2)/n
        sol = sol + (math.pi)/(n+1) * F(z)

    print(sol)


x = symbols('x')
f = symbols('f',cls=Function)

F = lambda x: math.sqrt(abs(1-x*x))

Chebycheff (F,30)
