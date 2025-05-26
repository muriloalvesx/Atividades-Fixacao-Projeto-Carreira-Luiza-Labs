'''

10. Faça um programa em que temos uma função em que recebe duas listas, a primeira
lista refere-se ao nome de n pessoas, e a segunda lista são as n idades das pessoas. Esta
função irá devolver uma lista de dicionários contendo o nome e a idade das junção das duas
listas.

'''

def func_receber_dados():
    qtd_pessoas = int(input("Digite o número de pessoas: "))
    
    nomes_str = input(f"Digite os nomes das {qtd_pessoas} pessoas separados por vírgula: ")
    nomes = [nome.strip() for nome in nomes_str.split(',')]
    
    idades_str = input(f"Digite as idades das {qtd_pessoas} pessoas separadas por vírgula: ")
    idades = [int(idade.strip()) for idade in idades_str.split(',')]
    
    return nomes, idades

def func_juntar_dados(nomes, idades):
    lista = []
    for i in range(len(nomes)):
        pessoa = {
            'nome': nomes[i],
            'idade': idades[i]
        }
        lista.append(pessoa)
    return lista

nomes, idades = func_receber_dados()
lista_pessoas = func_juntar_dados(nomes, idades)
print(lista_pessoas)

## Observações de Aprendizado:
# Entender melhor sobre a função strip()
# Entender melhor a lógica para juntar os dados informados