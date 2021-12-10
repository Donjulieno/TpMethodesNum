# fichier cree le 151121 par JUSA
# cours de maths outils num

import math
import numpy as np

import dichotomie
import Newton
import secante
import Simpson
import GaussLegendre
import rectangles
import trapezes
import Jacobi

a=-1
b=10
h=0.2
epsilon = 0.001
f = lambda x: math.exp(-(x ** 2) / 2)
#dichotomie.dicho(epsilon, a, b)
#Newton.newton(a, b, epsilon)
#secante.secante(a, b, epsilon)

#Simpson.simpson(f,a,b,h)
#GaussLegendre.gl(f,a,b,2)
#rectangles.rect(f,a,b)
#trapezes.trapeze(f,a,b)

A=np.array([[4,3,-5],[-4,-5,7],[8,6,-8]])
B=np.array([[2],[-4],[6]])
Jacobi.resolution(A,B,0.001,100)