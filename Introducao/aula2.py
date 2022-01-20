# a = 10
# b = 5

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicao = a * b
divisao = a / b
resto = a % b


print('Soma: ' + str(soma))
print('Subtração: ' + str(subtracao))
print('Multiplicação: ' +str(multiplicao))
print('Divisão: ' + str(divisao))
print('Resto: ' + str(resto))

print('------------------')
resultado = ('Soma: {soma} \nSubtração: {sub}'
      ' \nMultiplicação: {mult}'
      ' \nDivisão: {div}'
      ' \nResto: {rest}'.format(soma=soma,
                                mult=multiplicao,
                                sub=subtracao,
                                div=divisao,
                                rest=resto))
print(resultado)

print('---------------')

print(type(divisao))
print(int(divisao))

print("--------------")

soma = str(soma)
print(type(soma))
print("--------------")

x = '1'
soma2 = int(x) + 1
print(soma2)
print('------------')





