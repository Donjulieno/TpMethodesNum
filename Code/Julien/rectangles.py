from scipy.misc import derivative
from sympy import *
import scipy
import math
import numpy as np


def rect(f, a, b):
    i = a
    integ = 0
    while i < b:
        i = i + 1
        integ = integ + (f((i+0.5)))
    print("rectangle :" + str(integ))
