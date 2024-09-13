import json

# Se o arquivo de dados estiver na sua maquina so substituir com o endereço do arquivo
file_path = 'dados.json'

# Carregar os dados do arquivo JSON
with open(file_path, 'r') as file:
    faturamento_mensal = json.load(file)

# Filtrar os dias com faturamento (ignorando dias sem faturamento)
faturamento_valido = [dia['valor'] for dia in faturamento_mensal if dia['valor'] > 0]

# Verificar se há faturamento válido
if faturamento_valido:
    # Calcular o menor e o maior valor de faturamento
    menor_valor = min(faturamento_valido)
    maior_valor = max(faturamento_valido)

    # Calcular a média mensal (apenas com dias que tiveram faturamento)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    # Calcular o número de dias com faturamento acima da média
    dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_mensal])

    # Exibir os resultados
    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
else:
    print("Nenhum faturamento válido encontrado.")
