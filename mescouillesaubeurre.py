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

#ecart-types
sigma1=0
sigma2=0
for k in range(nligne):
    sigma1=math.sqrt(((age[k]-moy1)**2)/nligne)+sigma1
    sigma2=math.sqrt(((circ[k]-moy2)**2)/nligne)+sigma2
print("Les écart-types sont :",sigma1,sigma2)

#régression par les moindres carrés
x=age
y=circ
b=0
a=0

for l in range(nligne):
    b=((x[l]-moy1)*(y[l]-moy2))/((x[l]-moy1)**2)+b
    a=moy2-(b*moy1)+a
print(a,b)
print("y=","%5.2f"%a,"%5.2f"%b,".x")