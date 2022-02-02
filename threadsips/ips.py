import ipaddress #calculo de ip / imprimir rede

ip = '192.168.0.1'
ip2 = '192.168.0.0/24'


endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip2, strict=False)

print(endereco + 100)
print(endereco + 257)
print(endereco + 256)
print(endereco + 2000)

print('-----------------')

for ip2 in rede:
    print(ip2)
