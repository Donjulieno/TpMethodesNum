from scipy.misc import derivative
from sympy import *
import scipy
import math
import numpy as np


def gl(f, a, b, n):
    xi = [[0],[-float(sqrt(3)/3),float(sqrt(3)/3)],[-float(sqrt(3/5)),0,float(sqrt(3/5))]]
    i=0
    integ=0
    while i<len(xi[n-1]):
        integ = integ+xi[n][i]
        i=i+1
    print(integ)