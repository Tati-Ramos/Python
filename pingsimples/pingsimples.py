import os #importa o módulo ou biblioteca os (integra os programas e recursos do S.O)

print("#" * 60) #imprimindo # 60 vezes

#criamos uma variável que vai receber do usuario um ip
ip_ou_host = input("Digite o Ip ou host a ser verificado: ")

print("-"* 60) #imprimindo - 60 vezes

#chamando system da biblioteca os c- comando ping
#-n é no número de pacotes que serão 6
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-"* 60)