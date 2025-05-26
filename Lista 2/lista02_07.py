'''

7. Crie um script que leia 10 números inteiros positivos e que irá apresentar:
●​ A lista dos valores lidos de forma ordenada.
●​ A contagem de cada item. Por exemplo, se o usuário informou [1,1,1,1,2, 3],
aqui apresentamos:
○​ 1: 4x.
○​ 2: 1x.
○​ 3: 1x.
●​ Uma saída identificando o número, se o número é par e se é primo. Isto será feito
separando por vírgulas: Por exemplo, se informou [1,2,3,6]. Iremos apresentar aqui:
○​ 1,ímpar,não é primo
○​ 2,par,é primo
○​ 3,ímpar,é primo
○​ 6,par,não é primo

'''

def func_receber_numeros():
    numeros = input("Digite 10 números inteiros (ex: 1 2 3 4): ").split()
    numeros = [int(num) for num in numeros]
    return numeros

# Ordenação menor para maior:
def func_lista_ordenada(lista):
    lista = sorted(lista)
    return lista

def func_contagem_numeros(lista):
    for numero in set(lista):
        qtd = lista.count(numero)
        return print(f"{numero}: {qtd}x")

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def func_par_impar_primo(lista):
    print("\nInformações dos números:")
    for numero in lista:
        par_impar = "par" if numero % 2 == 0 else "ímpar"
        primo = "é primo" if eh_primo(numero) else "não é primo"
        return print(f"{numero},{par_impar},{primo}")
    

lista = func_receber_numeros()
lista_ordenada = func_lista_ordenada(lista)
contagem = func_contagem_numeros(lista)
par_impar_primo = func_par_impar_primo(lista_ordenada)

print(lista_ordenada, contagem, par_impar_primo)

## Oberservações da Aplicação:
# Aplicação não está funcionando como solicitado, ajustar assim que possível

## Observações de Aprendizado:
# Entender melhor sobre conversão de string para inteiro
# Entender melhor sobre funções .split() e .sort() e .sorted()
# Entender melhor a lógica disso: linha 21: numeros = [int(num) for num in numeros]
