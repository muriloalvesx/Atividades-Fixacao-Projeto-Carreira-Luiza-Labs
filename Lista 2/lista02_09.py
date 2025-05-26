'''

9. O pessoal de procura de clientes, trabalha com ligações para números aleatórios. Eles
recebem uma lista com vários intervalos de números para eles ligarem. Na lista recebida,
você tem o prefixo do telefone, o primeiro sufixo e o último sufixo. Crie um script que liste
todos os números dos telefones, ao serem informados, o prefixo e os sufixos. Por exemplo,
suponha que o prefixo seja “3232” e que o primeiro prefixo seja “0001” e o último sufixo seja
“0005”; logo o programa irá imprimir:
Seus números de telefone são:
​
● 3232-0001
● 3232-0002
● 3232-0003
● 3232-0004
● 3232-0005

'''

def func_receber_intervalo():
    prefixo = int(input("Digite o prefixo desejado: "))
    intervalo_sufixo = input("Digite o intervalo de sufixo desejado (ex: 0001 0005): ").split()

    intervalo = {
        'prefixo': prefixo,
        'dif_sufixo': int(intervalo_sufixo[1]) - int(intervalo_sufixo[0]),
        'sufixo_inicio' : int(intervalo_sufixo[0]),
        'sufixo_fim' : int(intervalo_sufixo[1])
    }

    return intervalo

def func_gerar_lista(intervalo):
    lista = []
    inicio = intervalo['sufixo_inicio']
    fim = intervalo['sufixo_fim']
    for i in range(inicio, fim + 1):
        sufixo_formatado = str(i).zfill(4)
        telefone = f"● {intervalo['prefixo']}-{sufixo_formatado}"
        lista.append(telefone)
    return lista

def func_exibir_telefones(lista):
    print("\nSeus números de telefone são:")
    for telefone in lista:
        print(telefone)

intervalo = func_receber_intervalo()
lista = func_gerar_lista(intervalo)
func_exibir_telefones(lista)

## Observações de Aprendizado:
# Estudar sobre a biblioteca math
# Dificuldade em lidar com dicinários, tuplas e listas.
# Entender melhor a lógica disso: linha 37: sufixo_formatado = str(i).zfill(4)
# Entender melhor a lógica disso: linha 38: telefone = f"● {intervalo['prefixo']}-{sufixo_formatado}"
# Entender melhor o funcionamento da aplicação com caracteres especiais, ex: ● 