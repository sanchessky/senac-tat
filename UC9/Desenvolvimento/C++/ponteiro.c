#include <stdio.h>

int main (){
    /*variavel idade*/
    int idade = 22;
    int *ptr_idade = &idade;
    /*declaração do ponteiro*/
    printf("A idade é %d e está em %p e %p com o valor %p\n", idade, &idade, ptr_idade,*ptr_idade);
    
    
    


    return 0;
}
