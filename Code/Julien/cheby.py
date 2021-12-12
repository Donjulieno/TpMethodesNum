import sympy as sp
from math import *
import numpy as np
from matplotlib.pylab import *
from scipy.integrate import odeint
from scipy.integrate import solve_ivp


def Chebycheff (F,n):

    #y_calc = np.zeros((interval,1))
    #print(y_calc)
    sol = []
    for i in range (0,n+1):

        z = cos((2*i+1))*(math.pi/2)/n
        sol = sol + (math.pi)/(n+1) * F(z)

    print(sol)
