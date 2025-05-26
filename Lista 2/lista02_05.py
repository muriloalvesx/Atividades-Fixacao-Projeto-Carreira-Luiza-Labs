'''

5. Dada uma equação de segundo grau:
a * x^2 + b * x + c
onde o usuário informa os valores de a, b e c; calcule suas raízes utilizando a fórmula de
Bhaskara.

'''

import math

def func_inserir_valores():
    valores = {
        'a' : float(input("Insira o valor de 'a': ")),
        'b' : float(input("Insira o valor de 'b': ")),
        'c' : float(input("Insira o valor de 'c': ")) 
    }
    return valores

def func_formula_bhaskara(valores):
    v = valores
    delta = (v['b']**2) - ((4 * v['a']) * v['c'])

    if delta < 0:
        return 'raíz negativa', 'raíz negativa', delta 
    
    raiz_delta = math.sqrt(delta)
    x1 = (-v['b'] + raiz_delta) / (2 * v['a'])
    x2 = (-v['b'] - raiz_delta) / (2 * v['a'])
    return x1, x2

valores = func_inserir_valores()
bhaskara = func_formula_bhaskara(valores)
print(f"A raíz x1 vale: {bhaskara[0]}\nA raíz x2 vale: {bhaskara[1]}")

## Observações de Aprendizado:
# Estudar sobre a biblioteca math
# Dificuldade em lidar com dicinários, tuplas e listas.
# Entender melhor sobre acessar os valores dos dicionários.