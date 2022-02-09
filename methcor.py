# -*- coding: utf8 -*-

# Lecture des variables requises
nomfichier=str(input("Quel est le nom du fichier d'entrée?\n"))
print("Nom fichier",nomfichier)

# Lecture du fichier de données
fichier=open(nomfichier,"r")
nligne=0
for i in fichier:
    nligne=nligne+1
fichier.close()
print("Nombre de lignes",nligne)

# Lecture du fichier de données
year = [0.0 for i in range(0,nligne)]
month = [0.0 for i in range(0,nligne)]
day = [0.0 for i in range(0,nligne)]
hour = [0.0 for i in range(0,nligne)]
minute = [0.0 for i in range(0,nligne)]
methane = [0.0 for i in range(0,nligne)]

fichier=open(nomfichier,"r")
for i in range(0,nligne):
    fichier2 = fichier.readline().split("\t")
    year[i] = int(fichier2[0])
    month[i] = int(fichier2[1])
    day[i] = int(fichier2[2])
    hour[i] = int(fichier2[3])
    minute[i] = int(fichier2[4])
    methane[i] = float(fichier2[5])*10000 # en ppm
fichier.close()

# Calcul du nombre de minutes comprises dans le fichier de données
classe = [0 for i in range(0,nligne)]
nclasse=1
classe[0]=1
for i in range(1,nligne):
    if (minute[i]==minute[i-1]):
        classe[i]=nclasse
    else:
        nclasse=nclasse+1
        classe[i]=nclasse
    #print(i,minute[i],classe[i])
print("Nombre de minutes (=classe de moyennes)",nclasse)

# Somme des concentrations minute par minute
moy = [0.0 for i in range(0,nclasse)]
nobs = [0.0 for i in range(0,nclasse)]
day2 = [0.0 for i in range(0,nclasse)]
hour2 = [0.0 for i in range(0,nclasse)]
minute2 = [0.0 for i in range(0,nclasse)]

for i in range(0,nligne):
    moy[classe[i]-1]=moy[classe[i]-1]+methane[i]
    nobs[classe[i]-1]=nobs[classe[i]-1]+1
    day2[classe[i]-1]=day[i]
    hour2[classe[i]-1]=hour[i]
    minute2[classe[i]-1]=minute[i]

for k in range(0,nclasse):
    moy[k]=moy[k]/nobs[k]

#Ecriture des données
sortie = open("sortie_prog1.txt","w")
sortie.write("%10s %10s %10s %10s %10s \n" % ("Jour","Heure","Minute","Nobs","Moyenne(ppm)"))
for k in range(0,nclasse):
    sortie.write("%10i %10i %10i %10i %10.0f \n" % (day2[k],hour2[k],minute2[k],nobs[k],moy[k]))
sortie.close()
