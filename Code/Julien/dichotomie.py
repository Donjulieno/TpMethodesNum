from scipy.misc import derivative
from sympy import *
import scipy
import math
import numpy as np


def dicho( epsilon, a, b):
    f = lambda x: exp(2 * x) - 4 * x - 2
    print(f)
    listeX = [-1]
    listeFX = [f(-1)]
    #N:int =0
    N=int((ln(abs(b-a))-ln(epsilon))/ln(2)+1)
    print("N="+str(N))
    i:int =0
    aa=a
    bb=b
    x=0
    for i in range(N):
        print("------------------------------")
        print("i="+str(i))
        print("aa="+str(aa)+" b="+str(bb))
        print("xn+1="+str((bb+aa)/2))
        fa=f(a)
        fb=f(b)
        #np.append(listeX,float((a+b)/2))
        #np.append(listeFX, float((a+b)/2))
        listeX.append(float((aa+bb)/2))
        listeFX.append(float(f(float((aa+bb)/2))))
        derivee = derivative(f, float((aa+bb)/2))
        print("derivee = "+str(derivee))
        x0 = float((aa + bb) / 2)
        if f(aa)>f(bb):
            if f(x0)>0:
                aa=float((aa+bb)/2)
            elif f(x0)<0:
                bb=float((aa+bb)/2)
        if f(aa)<f(bb):
            if f(x0)>0:
                bb=float((aa+bb)/2)
            elif f(x0)<0:
                aa=float((aa+bb)/2)

    print("Resultat : x="+str(x0))
