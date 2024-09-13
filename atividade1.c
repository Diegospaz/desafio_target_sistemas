
#include <stdio.h>

int main()
{
    int indice =13, soma =0, k = 0; //Define as variaveis
    
    
    //Loop de iterações
    while(k < indice){
        k = k + 1;
        soma = soma + k;
    }
    
    //Imprime o valor final das minhas iterações
    printf("\nO valor da soma eh: %d\n", soma);

    return 0;
}
