import math

#données
tinterne=26.8
rti=1200
tair=0

#itération
ite=1
pas=0.01
precision=5
tpeau=[0 for i in range(9)]
for i in range(9):
    tair=tair+precision
    ite=1
    while(ite==1):
        num=rti*(tair-tinterne)
        den=rti+1260*(abs(tpeau[i]-tair)**(-0.4))
        tpeaux=tinterne+(num/den)
        diff=tpeaux-tpeau[i]
        if(abs(diff)<pas):
            ite=0
        elif(diff>pas):
            ite=1
            tpeau[i]=tpeau[i]+pas
print(tpeau)

#sortie fichier
sortiedevoir=open("sortiedevoir.txt","w")
for i in range(9):
    sortiedevoir.write("%5.2f\n"%tpeau[i])
sortiedevoir.close()



