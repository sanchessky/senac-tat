#include <stdio.h> /*intersecção*/
int main (){
    int a1[]={10,2,6,8,45,78}; /*contém 5 elementos*/
    int a2[]={6,78,2,15,7,122,16,17,5}; /*contém 8 elementos*/
    int p, s;
    for(p = 0 ; p <= 5 ; p++){
        for(s = 0 ; s <= 8 ; s++){
            if(a1[p] == a2[s]){                 /*estrutura de repetição*/ 
                printf("%d\n",a1[p]);
                break;
            }
        }
        
    }
return 0;
}