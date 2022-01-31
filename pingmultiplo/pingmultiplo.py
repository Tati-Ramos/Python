import os
import time #tempo de execução

with open('hosts.txt') as file:
    dump = file.read() # leia o arquivo
    dump = dump.splitlines() # dump em linhas separadas

    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)