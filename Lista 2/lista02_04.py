'''

Estou tentando entender os juros do meu banco. Para isto, ele me informou esta fórmula:
valorFinal = valorEmprestimo + (valorEmprestimo * taxa * tempo)
onde que:
●​ valorEmprestimo: É o valor que pegarei emprestado.
●​ taxa: É o valor da taxa por mês. Por exemplo: se for 4% ao mês, o valor será 0.04.
●​ tempo: Quantidade de meses que irei pagar o empréstimo.
Crie um script que colete cada um destes valores para calcular o valor final que estarei
pagando ao banco.

'''

def func_coletar_dados():
    dados = {
        'valorEmprestimo': float(input("Digite o valor a ser emprestado: ")),
        'taxa': float(input("Digite o percentual da taxa a ser aplicada(ex: 4 para 4%): ")) / 100 ,
        'tempo': int(input("Digite a quantidade de meses do empréstimo: "))
    }
    return dados

def func_valor_final(dados):
    d = dados
    valor_final = d['valorEmprestimo'] + (d['valorEmprestimo'] * d['taxa'] * d['tempo'])
    return valor_final

dados = func_coletar_dados()
calculo = func_valor_final(dados)
print("O valor final que você pegará com o banco é de: ", calculo)

## Observações de Aprendizado:
# Dificuldade em lidar com dicinários, tuplas e listas.
# Entender melhor sobre acessar os valores dos dicionários.
# Solução: Estudar sobre e aplicar.