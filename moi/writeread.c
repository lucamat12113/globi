# include <stdio.h>
# include <stdlib.h>

int main(){

char num[1000];
FILE *fptr=fopen("/home/luca/Burea/globi/moi/washington.pbm","r");

    if(fptr == NULL){
        printf("erreur à l'ouverture");

        return -1;
    }//fin if fptr

fscanf(fptr,"%c", &num);
printf("%c", num);



fclose(fptr);







return 0;
}// fin main