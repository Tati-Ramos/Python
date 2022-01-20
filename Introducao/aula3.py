# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é {}'.format(b))
# else:
#     print('o maior número é {}'.format(c))
# print('Final do programa.')
#
# print('-------------------')


# d = int(input('Entre com o primeiro valor: '))
# e = int(input('Entre com o segundo valor: '))
# resto_d = d % 2
# resto_e = e % 2
#
# if resto_d == 0 or resto_e == 0:    # Ou a segunda opção de if
# #if resto_d == 0 or not resto_e > 0:
#     print('foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')


a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('Média: {}'.format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada')