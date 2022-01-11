# -*- coding:utf8 -*-

#données
fichier=open("text_data.txt","r")
nligne=0
for a in fichier:
    nligne=nligne+1
print(nligne)
fichier.close()

fichier=open("text_data.txt","r")
for b in range(nligne):
    fichier2=fichier.readline().split(" ")
ncolonne=len(fichier2)
print(ncolonne)
fichier.close()

fichier=open("text_data.txt","r")
annees=[[0]for c in range(nligne)]
debit=[[0]for d in range(nligne)]
for e in range(nligne):
    fichier2=fichier.readline().split(" ")
    annees[e]=int(fichier2[2])
    debit[e]=float(fichier2[3])


nbannees=2004-1978

#calcul moyennes
moy=[[0 for h in range(2)]for i in range(nbannees)]
somme=debit[0]
nbvar=1
f=1
g=0
while(f<nligne):
    if((annees[f]!=annees[f-1]) or (f==nligne-1)):
        moy[g][0]=annees[f-1]
        moy[g][1]=somme/nbvar
        somme=debit[f]
        nbvar=1
        g=g+1
        
    else:
        if(debit[f]>0):
            somme=somme+debit[f]
            nbvar=nbvar+1
    f=f+1


#ordre décroissant
h=1
while(h<nbannees):
    i=h
    tampon=moy[i][1]
    tampon2=moy[i][0]
    while((i>0) and (tampon>moy[i-1][1])):
        moy[i][1]=moy[i-1][1]
        moy[i][0]=moy[i-1][0]
        i=i-1
    moy[i][1]=tampon
    moy[i][0]=tampon2
    h=h+1
print(moy)

#écriture des données
sortie=open("sortie.txt","w")
for j in range(nbannees):
    sortie.write("%4i %5.2f\n"%(moy[j][0],moy[j][1]))
sortie.close()