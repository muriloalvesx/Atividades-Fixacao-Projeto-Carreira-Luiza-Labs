'''

6. Faça um programa que leia a nota de um aluno. Garanta que a nota seja um valor inteiro
entre zero e 100. Se o valor não estiver dentro desse intervalo, informe que a nota é
inválida. Se a nota for maior que 60, informa que o aluno foi aprovado; caso contrário,
informa que ele foi reprovado.

'''

def func_ler_nota():
    entrada = int(input("Digite a nota do aluno: "))
    if entrada < 0 or entrada > 100:
        resposta = print("Valor inválido, informe um número inteiro entre 0 e 100. ")
    else:
        if entrada < 60:
            resposta = print("O aluno foi reprovado!")
        else:
            resposta = print("O aluno foi aprovado!")
    return resposta

nota = func_ler_nota()

## Sugestões:
# Analisar if's e else's e verficiar se é possível melhorar a estrutura e lógica
