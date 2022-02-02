import random, string

tamanho = int(input('Digite o tamanho de senha que você deseja: '))

chars = string.ascii_letters + string.digits + 'ç!@#$%*()-=+,.;:/?'
chars2 = string.ascii_lowercase + string.digits + 'ç!@#$%*()-=+,.;:/?'
chars3 = string.ascii_uppercase + string.digits + 'ç!@#$%*()-=+,.;:/?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
print(''.join(rnd.choice(chars2) for i in range(tamanho)))
print(''.join(rnd.choice(chars3) for i in range(tamanho)))
