fichier=open("data_eco.txt","r")
nligne=0
for a in fichier:
    nligne=nligne+1
print(nligne)
fichier.close()

ncolonne=0
fichier=open("data_eco.txt","r")
for b in range(nligne):
    fichier2=fichier.readline().split(";")
ncolonne=len(fichier2)
print(ncolonne)
fichier.close()

#identification des colonnes

fichier=open("data_eco.txt","r")
nom=[[0] for c in range(nligne)]
id=[[0]for c in range(nligne)]
per=[[0 for d in range(ncolonne-2)]for c in range(nligne)]

for e in range(nligne):
    fichier2=fichier.readline().split(";")
    nom[e]=str(fichier2[0])
    id[e]=int(fichier2[1])
    for x in range (ncolonne-2):
        per[e][x]=float(fichier2[x+2])
        
print(per)

#moyenne
moy=[[0]for f in range(nligne)]
div=6
num=0
for g in range(nligne):
    for h in range(6):
        num=per[g][h]+num

    moy[g]=num/div
    num=0
print(moy)

#minimum
mini=[[0]for i in range(nligne)]
for j in range(nligne):
     mini[j]=min(per[j])
print("Les minima sont",mini)

#maximum
maxi=[[0]for k in range(nligne)]
for l in range(nligne):
    maxi[l]=max(per[l])
print("Les maxima sont",maxi)

#classement par décroissance
m=1
while(m<nligne):
    n=m
    tampon1=id[n]
    tampon2=nom[n]
    tampon3=moy[n]
    tampon4=mini[n]
    tampon5=maxi[n]
    while((n>0) and (tampon3>moy[n-1])):
        moy[n]=moy[n-1]
        id[n]=id[n-1]
        nom[n]=nom[n-1]
        mini[n]=mini[n-1]
        maxi[n]=maxi[n-1]
        n=n-1
    id[n]=tampon1
    nom[n]=tampon2
    moy[n]=tampon3
    mini[n]=tampon4
    maxi[n]=tampon5
    m=m+1
print(id,nom,moy,mini,maxi)