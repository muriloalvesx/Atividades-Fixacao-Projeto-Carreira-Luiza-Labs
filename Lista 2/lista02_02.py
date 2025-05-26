'''

Crie um script que leia um número inteiro. Se o número for positivo, irá determinar se o
número é par ou ímpar; caso contrário, informará que o número é inválido.

'''

def valida_numero_positivo(numero):
    if numero < 0:
        print("Seu número é inválido. Digite um número positivo")
        return exit()
    else:
        return True

def valida_numero_par(numero):
    if numero % 2 != 0:
        return print("Seu número é ímpar.")
    else:
        return print("Seu número é par")

numero = int(input("Insira um número: "))
valida_positivo = valida_numero_positivo(numero)
valida_par = valida_numero_par(numero)

## Sugestões: 
# antes de acessar a função valida_par
# verificar se o retorno da função 
# valida_numero_positivo é TRUE, 
# neste caso não foi necessário porque
# se o número não for positivo já 
# executa a função exit(), encerrando o programa.