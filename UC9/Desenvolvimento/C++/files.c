#include <stdio.h>

int main(){
    FILE *arquivo;
    arquivo=fopen("files/verdade.txt","a"); /*w-> write, r->read, a->append*/
    fprintf(arquivo,"add\n");
    fclose(arquivo);
    printf("é\n");
    return 0;

}
