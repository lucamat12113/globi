# -*- coding: utf8 -*-

# Importer librairie
import math

# Lecture du fichier
fichier = open("vache.txt","r")
nligne=0
for k in fichier:
	nligne=nligne+1
	print(nligne)
print("nombre de lignes",nligne)
fichier.close()

fichier = open("vache.txt","r")

identification=[['0'] for i in range(nligne)]
nlact=[[0] for i in range(nligne)]
PLmax=[[0] for i in range(nligne)]
semL=[[0] for i in range(nligne)]#fbfsjddhfusddldqsldjgkh
semG=[[0] for i in range(nligne)]

for w in range(nligne):
    fichier2=fichier.readline().split(";")
    print(fichier2)
    identification[w]=str(fichier2[0])
    nlact[w]=int(fichier2[1])
    PLmax[w]=float(fichier2[2])
    semL[w]=int(fichier2[3])
    semG[w]=int(fichier2[4])
        
print(fichier2)

ncolonne=len(fichier2)
print("Nombre de colonnes",ncolonne)

#Production laitière

PL=[[0] for i in range(nligne)]

for i in range(nligne):
    PL[i]= PLmax[i]*(1.084-(0.7*math.exp(-0.46*semL[i]))-(0.009*semL[i])-(0.69*math.exp(-0.16*(45-semG[i]))))

print(PL)

#Ecriture
sortie = open("sortie.txt","w")
for i in range(nligne):
    sortie.write("%s;%10.2f \n" % (identification[i],PL[i]))
sortie.close()


