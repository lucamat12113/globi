# -*- coding: utf8 -*-

#importer librairie
import math

#lecture fichier
fichier=open("exercice2.txt","r")
nligne=0
for i in(fichier):
    nligne=nligne+1
print(nligne)
fichier.close

#variables
fichier=open("exercice2.txt","r")
age=[[0] for i in range(nligne)]
circ=[[0] for i in range(nligne)]

for i in range(nligne):
    fichier2=fichier.readline().split(" ")
    age[i]=int(fichier2[0])
    circ[i]=float(fichier2[1])
fichier.close

#moyennes
moy1=0
moy2=0
for j in range(nligne):
    moy1=((age[j])/nligne)+moy1
    moy2=((circ[j])/nligne)+moy2
print("Les moyennes sont :",moy1,moy2)

#ecart-types ATTENTION signe sommatoire dans la racine donc il faut mettre la racine hors de la boucle
sigma1=0
sigma2=0
for k in range(nligne):
    sigma1=((age[k]-moy1)**2)+sigma1
    sigma2=((circ[k]-moy2)**2)+sigma2
etp1=math.sqrt(sigma1/nligne)
etp2=math.sqrt(sigma2/nligne)
print("Les écart-types sont :",etp1,etp2)

#régression par les moindres carrés (séparer le num et le dén pour faciliter)

num=0
den=0

for l in range(nligne):
    num=((age[l]-moy1)*(circ[l]-moy2))+num
    den=((circ[l]-moy2)**2)+den
b=num/den
a=moy1-(b*moy2)
print(a,b)
print("y=","%5.2f"%a,"+","%5.2f"%b,".x")
