import math
import numpy as np

A = np.array([[9,-2,1], 
              [-1,5,-1],
              [1,-2,9]])

b = np.array([[13],        
              [9],
              [-11,]])


def M_gauss (M,S):
    #cette boucle fait le pivot de Gauss sur le triangle inferieur de M -> la decente
    for i in range (0, np.shape(M)[0]-1,1): 
        for a in range (i+1, np.shape(M)[0],1):
            #nous faisons la résolution d'une ligne
            S[a] = S[a]*M[i][i] - S[i]*M[a][i]
            M[a] = M[a]*M[i][i] - M[i]*M[a][i]

    #cette boucle fait le pivot de Gauss sur le triangle supperieur de M -> la remontée
    for i in range (np.shape(M)[0]-1,0,-1): 
        for a in range (i-1,-1,-1):
            #nous faisons la résolution d'une ligne
            S[a] = S[a]*M[i][i] - S[i]*M[a][i]
            M[a] = M[a]*M[i][i] - M[i]*M[a][i]

    
    for i in range (0, np.shape(M)[0],1):
        #Nous divons la S par la Diagonal de M pour obtenir nos résultat
        S[i] = S[i] / M[i][i]
        M[i][i] = 1
    #Nous affichons le résultat
    print("La solution du pivot de Gauss est :",S,)
    return S


x= M_gauss(A,b)
