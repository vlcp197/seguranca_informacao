import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()
    print("Socket criado com sucesso")

    host_alvo = input("Digite o Host ou IP a ser conectado: ") 
    porta_alvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print("Cliente TCP conectado com Sucesso no Host: " + host_alvo + "e na porta: " + porta_alvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no host: " + host_alvo +"- "+ porta_alvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()

    




