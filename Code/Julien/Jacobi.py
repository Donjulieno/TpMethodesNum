'''
************************************************************************
*        Resolution de systeme lineaire par la methode de Jacobi       *
*                          Par JUSA le 081221                          *
*                        derniere modif 111221                         *
************************************************************************
'''

import numpy as np
import time


def resolution(A, B, E, tmax):
    t1 = time.time()
    t2 = time.time()

    eps = 10000000  # epsilon -> l erreur sur la solution -> valeur tres grande : arbitraire
    i = 0
    xn = np.zeros(len(A))
    D = np.diag(A)
    EpF = A - np.diagflat(D)
    i = 0
    while eps > E and t2 - t1 < tmax:
        xmoins1=xn
        xn = (B - np.dot(EpF, xn)) / D
        # calcul de l erreur
        eps=np.linalg.norm(xn-xmoins1)
        t2 = time.time()
        i = i + 1
    print("------------- Resultat -------------")
    print(xn)
    return xn


























