#include <stdio.h>


int main (){
    int valores[]={7,6,5,4,3,2,1};
    int *ptr_valores= valores;
    printf("%p com valor %d\n",ptr_valores,*ptr_valores);
    ptr_valores++;
    printf("%p com valor %d\n",ptr_valores,*ptr_valores);
    ptr_valores=ptr_valores+2;
    printf("%p com valor %d\n",ptr_valores,*ptr_valores);
    return 0;
}
