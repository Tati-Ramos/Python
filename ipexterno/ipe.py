#Operações com expressões regulares
import re

# Codificador e decodificador JSON
import json

#O módulo urllib.request define funções e classes que ajudam a abrir URLs (principalmente HTTP) em um mundo complexo — autenticação básica ou por digest, redirecionamentos, cookies e muito mais.
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do Ip externo\n')
print('IP: {4}\nRegião: {1}\nPaís: {2}\Cidade: {3}\nOrg.: {0}'.format(org, regiao, pais, cid, ip))
