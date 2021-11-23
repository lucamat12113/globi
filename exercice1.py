# -*- coding:utf8 -*-

#données
nligne=int(input("Quel est le nombre de lignes ? \n"))
ncolonne=int(input("Quel est le nombre de colonnes ? \n"))

vache=open("exercice1.txt","r")
poids=[[0] for i in range(nligne)]

for j in range(nligne):
    fichier=vache.readline().split(" ")
    print(fichier)
    poids[j]=float(fichier[1][j])
print(fichier)    
print(poids)


for k in range (nligne):
    if poids[k]>poids[k+1]:
        ite=1
    else:
        ite=0
    poidsmin=poids[k]

print(poidsmin)