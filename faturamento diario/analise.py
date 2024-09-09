import json

with open('dados.json', 'r') as file: # abrindo o arquivo para leitura
   dados = json.load(file)

# É necessario um for para que leia de acordo com cada analise pedida 
valores = [item['valor'] for item in dados if item['valor'] > 0] # lendo todo valor faturamento maior que 0
diasNulo = [item['dia'] for item in dados if item['valor'] == 0] # tirando os dias que estão com faturamento zerado



if valores :   # calculando os valores solicitados
    menorValor = min(valores )
    maiorValor = max(valores )
    mediaValor = sum(valores ) / len(valores)

    diasAcima = sum(1 for valor in valores if valor > mediaValor) # calculando os dias de maior faturamento

# print com os resultados
print(f'O menor valor de faturamento ocorrido em um dia do mês: {menorValor}')
print(f'O maior valor de faturamento ocorrido em um dia do mês: {maiorValor}')
print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal : {diasAcima}')