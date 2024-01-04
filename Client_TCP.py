import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Digite o IP para a conexão: ")

porta = int(input("Digite a porta para a conexão: "))

mensagem_1 = input("Digite a mensagem para o servidor TCP: ")

mensagem1_bytes = mensagem_1.encode("utf-8")

try:
    client.connect((ip, porta))
    client.send(mensagem1_bytes)
    pacotes_recebidos = client.recv(1024).decode()
    print(f"A resposta do servidor foi: {pacotes_recebidos}")
except Exception as error:
    print("Houve um erro ao fazer a conexão")
    print(error)
