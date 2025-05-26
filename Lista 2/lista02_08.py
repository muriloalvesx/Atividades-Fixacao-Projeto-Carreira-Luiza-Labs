'''

8. Faça um programa para controle de sua poupança. Sua poupança deverá iniciar com
saldo zerado (o script armazena o seu saldo na memória). O programa irá apresentar o
seguinte menu principal de quatro opções:
a. Consultar saldo.
Se escolhermos esta opção, iremos mostrar o saldo da poupança.
E voltaremos a mostrar o menu principal.
b. Sacar
Se o saldo estiver zerado, iremos informar que não é possível sacar e voltaremos
para o menu principal.
Se o saldo não estiver zerado, iremos solicitar o valor a ser sacado.
Se o valor sacado deixar a conta negativa, iremos informar que o valor é inválido e
voltaremos para o menu principal.
Se o valor sacado não deixar a conta negativa; então, iremos retirar o valor do
saldo.
Sempre voltamos a apresentar o menu principal.
c. Depositar
Iremos informar o valor a ser depositado e adicioná-lo ao saldo.
Voltamos a apresentar o menu principal.
d. Sair.
Saímos do programa.

'''

def func_menu_inicial():
    print("Escolha uma opção:\na. Consultar saldo\nb. Sacar\nc. Depositar\nd. Sair")    
    opcao = input()
    return opcao

def func_realizar_operacao_a(poupanca):
    print(poupanca)

def func_realizar_operacao_b(poupanca):
        if poupanca == 0:
            print("Não é possível realizar o saque pois o saldo é 0.")
        if poupanca > 0:
            saque = float(input("Informe o valor a ser sacado: "))
            poupanca = poupanca - saque
            if poupanca < 0:
                print("Valor inválido, tente novamente. ")
            else:
                return poupanca
    
def func_realizar_operacao_c(poupanca):
        deposito = float(input("Informe o valor a ser depositado: "))
        if deposito <= 0:
            print("Valor inválido, tente novamente.")
        else:
            poupanca = poupanca + deposito
            
poupanca = 0

operacao = func_menu_inicial()
if operacao == 'a':
    func_realizar_operacao_a(poupanca)

if operacao == 'b':
    func_realizar_operacao_b(poupanca)
    
if operacao == 'c':
    func_realizar_operacao_c(poupanca)
    
if operacao == 'd':
    exit()

## Oberservações da Aplicação:
# Aplicação não está funcionando como solicitado, ajustar assim que possível
# Implementar salvar os dados em memória e retornar ao menu inicial

## Observações de Aprendizado:
# Analisar if's e else's e verficiar se é possível melhorar a estrutura e lógica
