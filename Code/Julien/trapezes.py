from scipy.misc import derivative
from sympy import *
import scipy
import math
import numpy as np


def trapeze(f, a, b):
    i=a
    integ=0
    while i<b:
        i=i+1
        integ=integ+0.5 * (f(i) + f(i+1))
    print("trapeze :" +str(integ))