x = 1 ## Criação da variável x e atribuído o valor inteiro 1
x = 10 * 2 + 5 * 3 ## Atribuição do resultado da equação à variável x
a = input ("Digite algo: ") ## Declaração da variável a e atribuído a entrada do usuário como string
type(a) ## Retorna o tipo da variável a, saída: <class 'str'>
type(a) == str ## Valida se o tipo da variável a é str, saída: True
type(a) is str ## Valida se o tipo da variável a é str, saída: True
_ = 22 ## Criação da variável _ e atribuído o valor inteiro 22
12 = 44 ## SyntaxError: cannot assign to literal. Não é possível atribuir valores a um literal
12 == 44 ## Valida se 12 é igual a 44, saída: False
x = None ## Atribuição do valor None à variável x
x is None or x == None ##V alida se x é None ou X é igual a None, saída: True
x = 12 ## Atribuição do valor inteiro 12 à variável x
x <= 12 + 3 > 4 ## Valida se x é menor ou igual a 12+3 e se 12+3 é maior que 4
4 ** .5 + 3 ## Eleva 4 à potência 0.5 e soma + 3, saída: 5.0
.3 + 1e3 ## Soma 0.3 + a notação científica 1 * 10^3 que é 1000, saída: 1000.3
2j + 1 ## Soma de 1 + 2j que é a parte imaginária do número complexo equivalendo a 0 + 2i, saída: (1+2j)
0.4 + 0.4 + 0.4 == 1.2 ## Valida se a soma de 0.4 + 0.4 + 0.4 é igual a 1.2, saída: True
int(f"1{3}") ## f"1{3}" é uma string formatada, o que está dentro das chaves {3} será inserido na string, saída: "13"
"a,b,c,".split(",") ## Divide a string "a,b,c" em partes com a vírgula separando, saída: ['a', 'b', 'c', '']
set(1,2) ## TypeError: set expected at most 1 argument, got 2. set() espera um iterável, mas foram fornecidos 2 argumentos
set((1,2,2)) ## A função set() converte a tupla em um conjunto, saída: {1, 2}
max([1,5,7]) ## A função max() retorna o maior valor da sequência, saída: 7
any([True, False]) ## A função any() retorna True se qualquer elemento for verdadeiro, saída: True
any([False, False]) ## A função any() retorna True se qualquer elemento for verdadeiro, saída: False
all([True, False]) ## A função all() retorna True se todos os elementos forem verdadeiros, saída: False
all([True, 1]) ## A função all() retorna True se todos os elementos forem verdadeiros, saída: True
x = 1 # + 1 ## O caractere # indica que o restante da linha é um comentário, não faz parte do código, saída: x = 1
y = 2 # * 3 ## x = 1 # + 1 ## O caractere # indica que o restante da linha é um comentário, não faz parte do código, saída: y = 2
sum([x,y]) ## A função sum() faz a soma da lista [x, y] que é 1 + 2, saída: 3
a, b, *_ = ["a", 2.4, True, []] ## Desempacotamento da lista, atribuindo a variável a o primeiro elemento, b o segundo elemento, e _ recebe todos os elementos restantes, saída: a == "a" and b == 2.4 and _ == [True, []]
k = {1,2, 4}.discard(0) ## Cria o conjunto {1,2, 4} e utiliza o método .discard() para remover o elemento 0 do conjunto, como o 0 não está no conjunto o método retorna None, saída: None
p = { 1: 2, 3: 4} ## Cria um dicionário e atribui à variável p, contendo uma chave 1 com valor 2 e uma chave 3 com valor 4
"A" in "abcd" ## Valida se A está presente na string abcd, saída: False
"A" in [1,2, "A" ] ## Valida se A está presente na lista [1,2, "A" ], saída: True
[1,2,3,4,5,6,7,8][2:7:2][:-1][::-1] ## Pega os elementos dos índices 2 a 6 pulando 2 em 2 ([3,5,7]), remove o último ([3,5]) e inverte a lista, saída: [5,3]
{ "a": 2, 2: "a"}["a"] ## Cria um dicionário com chaves "a" e 2 e retorna o valor associado à chave "a", saída: 2
k = { "a": {}, 2: "a" } ## Cria um dicionário k com duas entradas: a chave "a" mapeando para um dicionário vazio {}, e a chave 2 mapeando para a string "a"
x = k["a"] = 3 ## Atribui o valor 3 à chave "a" do dicionário k e também à variável x
help(dict) ## Abre a ajuda do Python com documentação da classe dict, que mostra o que é um dict, como criar, métodos e exemplos
print(f"o valor de x é {x}") ## Imprime na tela uma string formatada (f-string), substituindo {x} pelo valor atual da variável x, saída: 3
lista = list([1,2,3,4]) ## Cria uma nova lista [1, 2, 3, 4] e atribui a variável lista
len(lista) ## Retorna o comprimento atual da lista, saída: 4
lista.extend((2,3,4,5)) ## Adiciona os elementos da tupla (2, 3, 4, 5) ao final da lista, que passa a ser [1, 2, 3, 4, 2, 3, 4, 5]
{ "python: ## SyntaxError: unterminated string literal. Erro de Sintaxe, a string não foi fechada com e o { não foi fechado