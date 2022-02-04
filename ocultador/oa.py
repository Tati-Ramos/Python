# ctypes é uma biblioteca de funções externas para Python.
# Ela fornece tipos de dados compatíveis com C e permite funções de chamada em DLLs ou bibliotecas compartilhadas.
#Ela pode ser usada para agrupar essas bibliotecas em Python puro.

import ctypes

pasta = input("Digite o caminho da pasta a ser ocultada ex (C:/pasta): ")

atributo_ocultar = 0x02 #hexadecimal

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")


