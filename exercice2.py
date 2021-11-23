# -*- coding:utf8 -*-

#données
nligne=int(input("Quel est le nombre de lignes? \n"))
ncolonne=int(input("Quel est le nombre de colonnes? \n"))

fichier=open("exercice1.txt","r")

poids=[[0] for i in range(nligne)]
for k in range(nligne):
    fichier2=fichier.readline().split(" ")
    poids[k]=float(fichier2[1])
print(poids)

j=1

while(j <= nligne-1):
    
    i = j
    clé=poids[i]
    
    while((i>0) and (poids[i-1]>clé)):
        poids[i]=poids[i-1]
        
        i=i-1
    poids[i]=clé
    j=j+1
print(poids)
