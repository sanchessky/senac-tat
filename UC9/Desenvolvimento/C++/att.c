#include <stdio.h>

int main(){
    int ano1;
    printf("Digite o Algum Ano e tecle Enter: \n");
    scanf("%d", &ano1);
   

    if (ano1 % 4==0){
        printf("O %d é ano bissexto \n", ano1);
    }   
    
    else if (ano1 + 1+1 ){
        printf("O %d é ano não bissexto \n", ano1);

    }

    return 0;

}
