'''
************************************************************************
*        Resolution de systeme lineaire par la methode de Jacobi       *
*                          Par JUSA le 081221                          *
************************************************************************
'''

import numpy as np


def resolution(A, B, E, Nmax):
    D = (np.size(A, 0), np.size(A, 0))
    EpF = (np.size(A, 0), np.size(A, 0))  # EpF=E+F

    D = np.zeros((np.size(A, 0), np.size(A, 0)))
    # Recuperation de la diagonale de A -> dans D
    for i in range(np.size(A, 0)):
        D[i, i] = A[i, i]
    EpF = A - D

    eps = 10000000  # epsilon -> l erreur sur la solution -> valeur tres grande : arbitraire
    i = 0
    #xn = np.array( [[[0],[0],[0]],[[1],[1],[1]], [[2],[2],[2]]] )
    xn = np.ndarray(shape=(3, 1))
    xn.fill(0)
    xntemp = np.ndarray(shape=(3, 1))
    xntemp2 = np.ndarray(shape=(1))
    xntemp.fill(0)
    xntemp[1,0]=1
    xntemp2[0] = xntemp[0]
    xn = np.append(xn,xntemp2,axis=0)
    print(xn[0])
    #xn = np.array( [[0,0,0],[1,1,1],[2,2,2]] )
    while eps > E and i <= Nmax:
        #print(xn[i])
        xnp1 = np.linalg.inv(D)*(B - np.dot(EpF, xn[i]))
        #xn[0].append(xnp1)
        eps = abs(np.linalg.norm(xnp1) - np.linalg.norm(xn[i])) / np.linalg.norm(xn[i])
        i = i + 1