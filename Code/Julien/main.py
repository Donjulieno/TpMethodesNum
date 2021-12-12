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
import cheby
import simsonKellian

a=0
b=1
h=0.1
epsilon = 0.0000001
#f=lambda x: x ** 2 - 3 - math.sqrt(3)
f=lambda x: x*math.exp(-x)
#f = lambda x: math.exp(-(x ** 2) / 2)
#dichotomie.dicho(epsilon, a, b)
#Newton.newton(f, a, epsilon)
#secante.secante(a, b, epsilon)

#Simpson.simpson(f,a,b,h)
simsonKellian.simson(f,a,b,h)
#GaussLegendre.gl(f,a,b,2)
#rectangles.rect(f,a,b)
#trapezes.trapeze(f,a,b)

#A=np.array([[4,3,-5],[-4,-5,7],[8,6,-8]])
#B=np.array([[2],[-4],[6]])
#A=np.array([[4,3,-5],[-4,-5,7],[8,6,-8]])
#B=np.array([2,-4,6])
A=np.array([[2,1],[5,7]])
B=np.array([11,13])
#A=np.array([[1,2,3],[4,5,6],[7,8,9]])
#B=np.array([14,32,50])
#Jacobi.resolution(A,B,0.000001,1)

#F = lambda x: math.exp(2*x)
#cheby.Chebycheff (F,30)




























