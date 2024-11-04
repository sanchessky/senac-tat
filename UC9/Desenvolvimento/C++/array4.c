#include <stdio.h>
int main(){
    int n[]= {33,8,7,11,54,77,13,16};
    int p;
        printf("Números pares\n");
        for (p = 1; p <= 8 ; p++){
            if (n[p] % 2 == 0){
                printf("%d\n",n[p]);
            }
        p++;
        }
return 0;
}