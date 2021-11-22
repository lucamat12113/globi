# -*- coding:utf8 -*-

#données
nligne=int(input("Quel est le nombre de lignes ? \n"))
ncolonne=int(input("Quel est le nombre de colonnes ? \n"))

vache=open("exercice1.txt","r")
poids=[[0] for i in range(nligne)]

for j in range(nligne):
    fichier=vache.readline().split(" ")
    print(fichier)
    poids[i]=float(fichier[1][i])
print(fichier)    
print(poids)
