#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json
from pathlib import Path

# Função para carregar os dados de faturamento do arquivo JSON
def carregar_dados_arquivo():
    caminho_arquivo = Path('C:/Users/well well/Desktop/TesteGupy/Teste tecnico/faturamento.json')
    with open(caminho_arquivo, 'r') as file:
        content = file.read()
        print(content)
        data = json.loads(content)
    return data["faturamento"]


def calcular_faturamento(faturamentos):
    dias_com_faturamento = [f["valor"] for f in faturamentos if f["valor"] > 0]

    if not dias_com_faturamento:
        return 0, 0, 0, 0

    menor = min(dias_com_faturamento)
    maior = max(dias_com_faturamento)
    media = sum(dias_com_faturamento) / len(dias_com_faturamento)
    acima_media = sum(1 for f in dias_com_faturamento if f > media)

    return menor, maior, media, acima_media

# Carregar os dados do faturamento a partir do arquivo JSON
faturamentos = carregar_dados_arquivo()

# Calcular os valores solicitados
menor, maior, media, acima_media = calcular_faturamento(faturamentos)

# Exibindo os resultados
print(f"Menor faturamento do mês: R${menor:.2f}")
print(f"Maior faturamento do mês: R${maior:.2f}")
print(f"Média mensal de faturamento: R${media:.2f}")
print(f"Número de dias com faturamento superior à média: {acima_media} dias")
