#include <stdio.h>
 /*void é uma função que não retorna*/
void dados(int *x, int *y){
    int soma = *x + *y;
    printf("X está em %p e Y está em %p \n",x,y);
    printf("Resultado é %d\n",soma);
}



int main (){

    int a = 10;
    int b = 20;
    dados (&a,&b);
    printf("A está em %p e b está em %p\n",&a,&b);
    


    return 0;
}
