#-- coding:utf8 --

#importation librairies
import math

#données
tinterne=26.8
rti=1200
tair=5

#itération

tpeau=[0 for i in range(9)]
ite=1
pas=0.01

while(ite==1):

    while(tair<=45):

        num=rti*(tair-tinterne)
        den=rti+1260*(abs(tpeau-tair)**(-0.4))
        tpeaux=tinterne+(num/den)
        diff=tpeaux-tpeau

        if(abs(diff)<pas):
            ite=0           
            tair+=5
            
        elif(diff>pas):
            ite=1
            tpeau=tpeau+pas



