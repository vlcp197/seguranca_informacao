import os #Importa o módulo ou biblioteca os (integra) 
#os programas e recursos do sistema operacional

print("#"*60) ##Imprimindo # 60 vezes

ip_ou_host = input("Digite o Ip ou host a ser verificado: ")
#Criamos uma variável que vai receber do usuário um IP

print("-"*60) ##Imprimindo - 60 vezes

os.system('ping -c 6 {}'.format(ip_ou_host) )
#Chamando o método system da biblioteca os
#chamando o comando ping
#-c é o numero de pacotes, que serão 6
#formata o ip da variavel ip_ou_host

print("-"*60) ##imprimindo - 60 vezes