from scipy.misc import derivative
from sympy import *
import scipy
import math
import numpy as np
import time


def simpson(f,a,b,h):
    #x=np.arange(a,b,h)
    integ=f(a)
    i=0
    while i<b:
        i=i+h
        integ=integ+4*f(i)+2*f(i+0.5*h)
    integ =integ+ f(b)
    print("Simson de f entre "+str(a)+" et "+str(b)+" = "+str(float(h*integ/6)))