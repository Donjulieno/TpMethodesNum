import math
import numpy as np

A = np.array([[9,-2,1],
              [-1,5,-1],
              [1,-2,9]])

b = np.array([[13],        
              [9],
              [-11,]])

def M_jacobi (M,b,e,Limite):

    #Initialisation des variables de la fonction
    F = np.zeros((np.shape(M)[0],np.shape(M)[1]))
    X_0 = np.zeros((np.shape(M)[0],1))
    X_n1 = np.zeros((np.shape(M)[0],1))
    diff = np.zeros((np.shape(M)[0],1))
    compteur = 0

    #boucle qui créer la matrice F pour prendre seulment les valeurs du triangle supperieur
    for i in range (0,np.shape(M)[0],1):
        for a in range (i+1, np.shape(M)[0],1):

            F[i][a] = M[i][a]

    X_n = X_0 #avant de commancer le calcule nous definissons le premier Xn
                        
    #Boucle qui va trouver Xn avec la présision demandée
    boucle = True                   #idicateur de la fonction 

    while boucle == True:           #si l'indicateur est égale à False alors la boucle s'arrête

        compteur = compteur + 1     #chaque tour nous allons augmenter le compteur (lien avec la limite)
        verif = 0                   #nous remettons à zeros la variable à chaque tour (lien avec la précision)
        #nous allons créer la matrice E à chauqye boucle car nous allons la modifier par la suite
        E = np.zeros((np.shape(M)[0],np.shape(M)[1]))
        #cette double boucle permet de faire le pivot de gauss en déssante (triangle inferieur)
        for i in range (0,np.shape(M)[0],1):
            for a in range (i, np.shape(M)[0],1):
        #nous mettons les valeurs du trangle inferieur de M dans E
                E[a][i] = M[a][i]

        #calcule de b - F * Xn
        S = b - F.dot(X_n)
        #nous allons résoudre E * X = S, nous réutilisons la double boucle
        for i in range (0, np.shape(M)[0]-1,1): 
            for a in range (i+1, np.shape(M)[0],1):
                #nous faisons la résolution d'une ligne
                S[a] = S[a]*E[i][i] - S[i]*E[a][i]
                E[a] = E[a]*E[i][i] - E[i]*E[a][i]

        for i in range (0, np.shape(E)[0],1):
            #cette boucle permet d'avoir la valeur de 1x et non Ex avec x une variable de la résolution de gauss
            S[i] = S[i] / E[i][i]
            #avec cette boucle nous verifions si la précision est bonne sur toutes les valeur de Xn+1
            if abs(S[i] - X_n[i]) <= e:
                verif = verif + 1   #si c'est le cas verif prend +1
        #si vérif est aussi grand qu'il y as de valeur dans X alors nous finnisons la boucle
        if verif == np.shape(M)[0]:
            boucle = False
            print("La solution est X",compteur," = \n",X_n)   #message de résolution
        #si le compteur à attein la limite que nous avons donnée alors nous finnisons la boucle
        if compteur == Limite:
            boucle = False
            print("Erreur pas de solution pour cette précision") #nous mettons un message pour signaler l'érreur
        X_n = S
        
    return S,compteur


M_jacobi (A,b,0.001,1000)
