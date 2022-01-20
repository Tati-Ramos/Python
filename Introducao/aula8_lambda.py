contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(10, 5))

calculadora = { # dicionário
    'soma': lambda a, b: a + b,
    'subtração': lambda a, b: a - b,
    'multiplicação': lambda a, b: a * b,
    'divisão': lambda a, b: a / b,
}

print(type(calculadora)) #dicionário
soma = calculadora['soma']
multiplicacao = calculadora['multiplicação']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação: {}'.format(multiplicacao(10, 2)))