import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Digite o IP para a conexão: ")

porta = int(input("Digite a porta para a conexão: "))

try:
    
    client.connect((ip, porta))

    while True:

        mensagem = input("Mensagem do Cliente: ") + "\n"
        client.send(mensagem.encode()) 
        
        if mensagem == "tchau\n":
            print("Fim da conexão")
            break
        
        pacotes_recebidos = client.recv(100000).decode()
        print(f"Mensagem do Servidor: {pacotes_recebidos}")
        
        if pacotes_recebidos == "tchau\n":
            print("Fim da conexão")
            break
    client.close()

except Exception as error:
    print("Houve um erro ao fazer a conexão")
    print(error)
