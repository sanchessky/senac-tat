#include <stdio.h>

int main() {
    float bruto, transporte, inss, fgts, descontos, liquido;

    // Salário Total
    printf("Digite o Salário Total: \n");
    scanf("%f", &bruto);

    // descontos
    transporte = bruto * 0.06; // 6% de vale transporte
    inss = bruto * 0.07;        // 7% de inss
    fgts = bruto * 0.08;        // 8% de fgts

    // total de descontos e o salário 
    descontos = transporte + inss + fgts;
    liquido = bruto - descontos;

    // resultados
    printf("Total de descontos: %.2f\n", descontos);
    printf("Salário líquido: %.2f\n", liquido);

    return 0;
}
