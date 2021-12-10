from scipy.misc import derivative
from sympy import *
import scipy
import math
import numpy as np
import time


def newton(a, b, epsilon):
    date1=time.time()
    f = lambda x: exp(2 * x) - 4 * x - 2
    listeX = [float(a)]
    listeFX = [float(f(a))]
    i=1
    precision = 100000
    x1=a
    date2 = time.time()
    while precision > epsilon and date2 - date1 < 10:  # critere de limite de temps a 10s
        xmoins1=x1
        x1=float(listeX[i-1])-listeFX[i-1]/derivative(f,float(listeX[i-1]))
        fx1=float(f(x1))
        listeX.append(x1)
        listeFX.append(fx1)
        j=1
        xtemp=0
        xtemp1=0
        while(j<10):
            xtemp = round(x1,j+1)
            xtemp1= round(xmoins1,j+1)
            if(xtemp==xtemp1):
                precision=10**-(j+1)
            j=j+1
        print("x="+str(x1)+" f(x=)"+str(fx1)+" precision : "+str(precision))
        i=i+1
        date2=time.time()