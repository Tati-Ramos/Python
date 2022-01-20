lista = [12, 10, 7, 5]
lista[0] = 30
print(lista)
print(type(lista))

print("------------")
lista.sort()
print(lista)

print("------------")
lista.pop(0)
print(lista)

print("--------")

soma = 0
for x in lista:
    print(x)
    soma += x
print('Soma: ' + str(soma))

    #OU
    
print("--------")
print('Soma: ' + str(sum(lista)))
print("--------")

print(min(lista))
print(max(lista))
print('Quantos elementos tem na lista: ' + str(len(lista)))

print("--------------------------------")
lista_animal = ['cachorro', 'lobo', 'gato', 'elefante', 'arara']
print(lista_animal)
print(lista_animal[1])

lista_animal.append('formiga')
print(lista_animal)
print("-------------------------------------")

lista_animal.sort()
print(lista_animal)
print("-------------------------------------")

lista_animal.reverse()
print(lista_animal)

print("-------------------------------------")
lista_animal.pop()
lista_animal.remove('elefante')
print(lista_animal)

for x in lista_animal:
    print(x)
print("--------------------------------")

print(min(lista_animal))
print(max(lista_animal))
print("-------------------------")

if 'gato' in lista_animal:
    print('Existe um gato na lista')
else:
    print('Não existe um gato na lista')
print("-------------------------")

# nova_lista = lista_animal * 3
# print(nova_lista)

print("Tupla: ")
tupla = (1, 10, 12, 14)
print(tupla[2])
print(len(tupla))
#tupla[0] = 12 #erro
print("-------------------------")

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)

print("-------------------------")
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)


# tuplas são imutáveis

# listas são mutáveis