#include <stdio.h>
    // este programa obtem um numero de usuario e diz se é par ou par, exibindo uma mensagem em tela //

int main() {
    int n;
    printf("Digite um Número e tecle Enter \n");
    scanf("%d",&n);

        
    if (n % 2 ==0){
        printf("O número %d é Par \n");
    }
    // Se n não for divido por 2 o resultado é impar // resto é igual a %
    else{
        printf("O número %d é impar \n");
    }

    return 0;
}
