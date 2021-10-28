# -*- coding: utf8 -*-

#matrices
#A1=[[0,1,3,0],[8,5,0,6],[0,0,1,1]]
#print(A1)

#B1=[[0,1],[0,0],[3,3],[9,5]]
#print(B1)

#Test autres matrices

A1=[[1,2],[3,4]]
print(A1)

B1=[[1,2,3,4],[5,6,7,8]]
print(B1)

nligneA1=len(A1) 
print("nb de lignesA\n", nligneA1)
ncolonneA1=len(A1[0])
print("nb de colonnesA\n", ncolonneA1)

nligneB1=len(B1)
print("nb de lignesB\n", nligneB1)
ncolonneB1=len(B1[0])
print("nb de colonnesB\n", ncolonneB1)


produit=[[0 for j in range(ncolonneB1)] for i in range(nligneA1)]
print(produit)

for i in range(nligneA1):
    for j in range(ncolonneB1):
        for d in range(ncolonneA1):
            produit[i][j]+=int(A1[i][d]*B1[d][j])
        
print(produit)
expected=[[9,9],[54,38],[12,8]]
print(expected)
        
         