# -*- coding: utf8 -*-

#import librairie
import math

# Lecture des variables
nligne = int(input("Quel est le nombre de lignes du fichier? \n"))
nomfichier=str(input("Quel est le nom du fichier? \n"))

print("Nom fichier",nomfichier)
print("Nombre de lignes",nligne)

# Lire le fichier de données
fichier=open(nomfichier,"r")
A =[[0.0]*2 for i in range(nligne)]
for i in range(nligne):
    fichier2=fichier.readline().split(" ")
    A[i][0] = float(fichier2[0])
    A[i][1] = float(fichier2[1])
fichier.close()
print(A)

# Calcul de la moyenne et de l'écart-type
moyenne=[0.0 for i in range(2)]
ecartype=[0.0 for i in range(2)]
nrecord=[0 for i in range(2)]

for j in range(2):
    for i in range(nligne):
        moyenne[j]=moyenne[j]+A[i][j]
        ecartype[j]=ecartype[j]+A[i][j]**2
        nrecord[j]=nrecord[j]+1
    ecartype[j]=math.sqrt((ecartype[j]-((moyenne[j]**2)/nrecord[j]))/(nrecord[j]-1))
    moyenne[j]=moyenne[j]/nligne

print("La moyenne est",moyenne)
print("L'ecart-type est",ecartype)

# Régression linéaire par la méthode des moindres carrés avec origine
som1=0
som2=0
for i in range(nligne):
    som1 = som1 + ((A[i][0]-moyenne[0])*(A[i][1]-moyenne[1]))
    som2 = som2 + (A[i][1]-moyenne[1])**2
bcoeff=som1/som2
acoeff=moyenne[0]-(bcoeff*moyenne[1])

print("La regreesion est: age=",acoeff,"+",bcoeff,"*circonference")

# Régression par la méthode des moindres carrés sans origine
som1=0
som2=0
for i in range(nligne):
    som1 = som1 + (A[i][0]*A[i][1])
    som2 = som2 + (A[i][1]**2)
bcoeff=som1/som2
acoeff=0

print("La regreesion est: age=",acoeff,"+",bcoeff,"*circonference")

# Régression linéaire par itération
iter=1
b=0
pas=0.001
nround=0
while(iter==1):
    moydiff1=0
    moydiff2=0
    moydiff3=0

    # erreur ==> y = a +bx + e ==> y = bx + e ==> e = y - bx
    for i in range(nligne):
        erreur=(A[i][0]-(b*A[i][1]))**2
        moydiff1=moydiff1+erreur

        erreur=(A[i][0]-((b-pas)*A[i][1]))**2
        moydiff2=moydiff2+erreur

        erreur=(A[i][0]-((b+pas)*A[i][1]))**2
        moydiff3=moydiff3+erreur

    moydiff1=moydiff1/nligne
    moydiff2=moydiff2/nligne
    moydiff3=moydiff3/nligne

    if ((moydiff1<=moydiff2) and (moydiff1>moydiff3)):
        b=b+pas
        iter=1
        nround=nround+1
    elif ((moydiff1>moydiff2) and (moydiff1<=moydiff3)):
        b=b-pas
        iter=1
        nround=nround+1
    elif ((moydiff1<=moydiff2) and (moydiff1<=moydiff3)):
        iter=0

    #print("Tour",nround,"valeur b",b)

acoeff=0
print("La regreesion est: age=",acoeff,"+",b,"*circonference")

# Données prédites
pred=[[0.0]*2 for i in range(nligne)]
for i in range(nligne):
    pred[i][0]=acoeff+(b*A[i][1]) #iterative
    pred[i][1]=acoeff+(bcoeff*A[i][1])

# Calcul moyenne et écart-type
moypred=0
SDpred=0

for i in range(nligne):
    moypred=moypred+pred[i][0]
    SDpred=SDpred+pred[i][0]**2
SDpred=math.sqrt((SDpred-((moypred**2)/nligne))/(nligne-1))
moypred=moypred/nligne

print("Moyenne prédite",moypred)
print("SD prédit",SDpred)