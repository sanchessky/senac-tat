#include <stdio.h>
/* função de cadastro*/
void cadastro(char *nome,char *email ,int *idade,int *telefone){
    FILE *arquivo;
    arquivo = fopen ("files/cad_cli.txt","a");
    fprintf(arquivo,"Nome: %s\n",nome);
    fprintf(arquivo,"Email: %s\n",email);
    fprintf(arquivo,"Idade: %d\n",*idade);
    fprintf(arquivo,"Telefone: %d\n",*telefone);
    fprintf(arquivo,"--------------------------------");
    fclose(arquivo);
}
int main (){
    char nome[30];
    char email [50];
    int idade;
    int telefone;
    printf("Digite o seu nome e tecle Enter:\n");
    scanf("%[^\n]s",nome);
    printf("Digite o seu email e tecle Enter:\n");
    scanf("%s",email);
    printf("Digite a sua idade e tecle Enter:\n");
    scanf("%d",&idade);
    printf("Digite o seu telefone e tecle Enter:\n");
    scanf("%d",&telefone);
    cadastro (nome,email,&idade,&telefone);
    printf ("Cadastrado\n");
    return 0;
}
