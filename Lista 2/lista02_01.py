'''

Crie um script que irá calcular a área de um quadrado. Peça para a pessoa informar a
medida numérica
de um lado do quadrado. E depois informe-lhe o valor da área do
quadrado.

'''

def calcular_area_do_quadrado():
    lado = int(input("Informe a medida númerica de um lado do quadrado: "))
    resultado = lado*lado
    return resultado

area = calcular_area_do_quadrado()
print("O valor da área do quadrado é: ", area)