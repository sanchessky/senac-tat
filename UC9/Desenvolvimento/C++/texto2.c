#include <stdio.h>
int main(){

    char nome[20];
    printf("Coloque o primeiro nome seu e tecle Enter:\n");
    // foi necessario utilizar o colchetes para que o comando scanf receba toda a cadeia de caracteres.
    // o elemento ^(circunflexo) foi usado para indicar onde comeca o primeiro caracter 
    // e comando \n, neste caso, esta sendo usado para ler o espaço aplicado.
    // ao final é utilizado o caracter s (string).
    scanf("%[^\n]",nome);
    printf("Olá, %s. Seja Bem-VIndo\n",nome);
    return 0;
}
