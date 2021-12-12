from scipy.misc import derivative
from sympy import *
import scipy
import math
import numpy as np
import time


def secante(a, b, epsilon):
    date1 = time.time()
    f = lambda x: exp(2 * x) - 4 * x - 2
    listeX = [float(a)]
    listeFX = [float(f(a))]
    i = 1
    precision = 100000
    xn = a
    xp1 = b
    date2 = time.time()
    while precision > epsilon and date2 - date1 < 10:  # critere de limite de temps a 10s
        xmoins1 = xn
        xn = float((xn * f(xp1) - xp1 * f(xn)) / (f(xp1) - f(xn)))
        fx1 = float(f(xn))
        listeX.append(xn)
        listeFX.append(f(xn))
        precision = abs(xn - xmoins1)
        print("x=" + str(xn) + " f(x=)" + str(fx1) + " precision : " + str(precision))
        i = i + 1
        date2 = time.time()
