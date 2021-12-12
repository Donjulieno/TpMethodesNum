#Fichier entêtes
import math
from sympy import *

#Fonctions
def simson (f, a, b, h):

    n = 1/h
    res = f(a) + f(b)
    i = a


    while i < b:

        xr = f(i)
        m = f(i+(h/2))

    
        res = res + 2 * xr + 4 * m
        i = i + h
    I = (h*res/6)
    
    return I


#déclaration des variables
h = 0.25

a = 0

b = 1

eq = lambda x: exp(-1*math.pow(x,2)/2)

################################################################################
###                             début programme                             ####
################################################################################

res = simson (eq, a, b, h)

print(res)






