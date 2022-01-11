# -*- coding: utf8 -*-

# Importer librairie
import math

# Nom du fichier
nomfichier=str(input("Quel est le nom du fichier d'entrée?\n"))
print("Nom fichier",nomfichier)

# Nombre de lignes dans le fichier
fichier=open(nomfichier,"r")
nligne=0
for i in fichier:
    nligne=nligne+1
fichier.close()
print("Nombre de lignes",nligne)

# Lecture du fichier de données
sem = [0.0 for i in range(0,nligne)]
dat = [0.0 for i in range(0,nligne)]
ville = [0.0 for i in range(0,nligne)]
nomtech = [0.0 for i in range(0,nligne)]
occup = [0.0 for i in range(0,nligne)]
quadra = [0.0 for i in range(0,nligne)]
nmet = [0.0 for i in range(0,nligne)]
naph = [0.0 for i in range(0,nligne)]

fichier=open(nomfichier,"r")
for i in range(0,nligne):
    fichier2 = fichier.readline().split("\t") #\t pour la tabulation
    #print("ligne",i,fichier2)
    sem[i] = int(fichier2[0])
    dat[i] = str(fichier2[1])
    ville[i] = str(fichier2[2])
    nomtech[i] = str(fichier2[3])
    occup[i] = str(fichier2[4])
    quadra[i] = int(fichier2[5])
    nmet[i] = float(fichier2[6])
    naph[i] = float(fichier2[7])
fichier.close()

# Moyenne et écart-type
## Sommation

sommet2=0
somaph2=0
moymet=0
moyaph=0
ETmet=0
ETaph=0

for i in range(0,nligne):
    moymet=moymet+nmet[i]
    moyaph=moyaph+naph[i]
    sommet2=sommet2+nmet[i]**2
    somaph2=somaph2+naph[i]**2

##Ecart-type
etmet=math.sqrt((sommet2-((moymet**2)/nligne))/(nligne-1.0))
etaph=math.sqrt((somaph2-((moyaph**2)/nligne))/(nligne-1.0))
print("Ecart-types",etmet,etaph)

## Moyennes
moymet=moymet/nligne
moyaph=moyaph/nligne
print("Moyennes",moymet,moyaph)

# Min-Max
minmet=nmet[1]
maxmet=nmet[1]
minaph=naph[1]
maxaph=naph[1]

## minmet et maxmet
for i in range(0,nligne):
    if (nmet[i] <= minmet):
        minmet=nmet[i]
    elif (nmet[i] >= maxmet):
        maxmet=nmet[i]

for i in range(0,nligne):
    if (naph[i] <= minaph):
        minaph=naph[i]
    elif (naph[i] >= maxaph):
        maxaph=naph[i]

# Ecriture des premiers resultats
sortie = open("resultat.txt","w")
sortie.write("%s \n" % ("						Metopolophium	  Aphis"))
sortie.write("%25s %8.3f %12.3f \n" % ("Moyenne:",moymet,moyaph))
sortie.write("%25s %8.3f %12.3f \n" % ("Ecart-type:",etmet,etaph))
sortie.write("%25s %8.3f %12.3f \n" % ("Minimum:",minmet,minaph))
sortie.write("%25s %8.3f %12.3f \n" % ("Maximum:",maxmet,maxaph))
sortie.close()

# Nombre de combinaisons
date = [0.0 for i in range(0,200)]
occupation = [0.0 for i in range(0,200)]
combi=0

for i in range(0,nligne):
    win = 0
    j=0 # python commence à 0
    while(win==0):
        if ((date[j]==dat[i]) & (occupation[j]==occup[i])):
            win = 1
        elif ((date[j]==0.0) & (occupation[j]==0.0)):
            date[j]=dat[i]
            occupation[j]=occup[i]
            win=1
            combi=combi+1
        else:
            win=0
            j=j+1
print("Nombre de combinaisons",combi)

# Moyennes journalières par culture et édition.
moypocmet = [0.0 for i in range(0,combi)]
moypocaph = [0.0 for i in range(0,combi)]
obspoc = [0.0 for i in range(0,combi)]

## Calcul du nombre d'individus et d'occurence
for i in range(0,nligne):
    for j in range(0,combi):
        if ((date[j]==dat[i]) & (occupation[j]==occup[i])):
            moypocmet[j]=moypocmet[j]+nmet[i]
            moypocaph[j]=moypocaph[j]+naph[i]
            obspoc[j]=obspoc[j]+1
print(obspoc)
for q in range(0,combi):
    moypocmet[q]=moypocmet[q]/obspoc[q]
    moypocaph[q]=moypocaph[q]/obspoc[q]

# Ecriture du fichier combinaison
sortie2 = open("combinaisons.txt","w")
for i in range(0,combi):
    sortie2.write("%10i %10s %10s %10.2f %10.2f \n" % ((i+1),date[i],occupation[i],moypocmet[i],moypocaph[i]))
sortie2.close()

# Classement des données pour metopolophium
for i in range(1,combi):
    moyclass=moypocmet[i]
    dateclass=date[i]
    occupclass=occupation[i]
    j=i-1
    while((j > 0) & (moypocmet[j] > moyclass)):
        moypocmet[j+1]=moypocmet[j]
        date[j+1]=date[j]
        occupation[j+1]=occupation[j]
        moypocmet[j]=moyclass
        date[j]=dateclass
        occupation[j]=occupclass
        j=j-1

# Ecriture des données classées
sortie3 = open("classement.txt","w")
for i in range(0,combi):
    sortie3.write("%10s %10s %10.3f \n" % (date[i],occupation[i],moypocmet[i]))
sortie3.close()


