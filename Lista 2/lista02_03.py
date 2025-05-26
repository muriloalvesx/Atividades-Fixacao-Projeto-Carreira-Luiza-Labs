'''

Neste script, você irá coletar o nome e a idade de três pessoas e informar ao final:
●​ O nome da pessoa mais velha.
●​ O nome da pessoa mais nova.
●​ A média das idades.

'''

def coletar_dados():
    pessoas = []
    for i in range(3):
        nome = input(f"Digite o nome da pessoa {i + 1}: ")
        idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
        pessoas.append({'nome': nome, 'idade': idade})
    return pessoas

def calcular_media(pessoas):
    soma = 0
    for pessoa in pessoas:
        soma += pessoa['idade']
    return soma / len(pessoas)


def encontrar_mais_velha(pessoas):
    mais_velha = pessoas[0]
    for pessoa in pessoas:
        if pessoa['idade'] > mais_velha['idade']:
            mais_velha = pessoa
    return mais_velha['nome']


def encontrar_mais_nova(pessoas):
    mais_nova = pessoas[0]
    for pessoa in pessoas:
        if pessoa['idade'] < mais_nova['idade']:
            mais_nova = pessoa
    return mais_nova['nome']

pessoas = coletar_dados()

mais_velha = print("O nome da pessoa mais velha é: ", encontrar_mais_velha(pessoas))
mais_nova = print("O nome da pessoa mais nova é: ", encontrar_mais_nova(pessoas))
media = print("A média das idades é: ", calcular_media(pessoas))

## Observações de Aprendizado:
# Dificuldade em lidar com dicinários, tuplas e listas.