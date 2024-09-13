#include <stdio.h>
#include <string.h>

int main() {
    // Definir a string
    char str[100];  // Pode definir o tamanho que desejar

    // Receber a string de entrada
    printf("Digite uma string: ");
    fgets(str, sizeof(str), stdin);  // Leitura da string com segurança

    // Remover o '\n' (quebra de linha) ao final da string, se existir
    str[strcspn(str, "\n")] = '\0';

    int length = strlen(str);  // Obter o comprimento da string
    int start = 0;
    int end = length - 1;
    char temp;

    // Lógica para inverter a string
    while (start < end) {
        // Troca os caracteres nas posições start e end
        temp = str[start];
        str[start] = str[end];
        str[end] = temp;

        // Move os índices para o centro
        start++;
        end--;
    }

    // Exibir a string invertida
    printf("String invertida: %s\n", str);

    return 0;
}
