import socket
import threading

# Função para receber mensagens do amigo
def receive_messages(connection):
    while True:
        data = connection.recv(2).decode()
        print(f"Amigo: {data}")

def main():
    host = input("digite o endereço ip: ")  # Endereço IP local
    port = input("digite a porta de comunicação desejada: ")       # Porta para comunicação

    # Configurar o socket para receber conexões
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, int(port)))
    server.listen(1)

    print("Aguardando conexão do amigo...")
    connection, address = server.accept()  # Aceitar conexão do amigo
    print(f"Conectado a {address}")

    # Iniciar uma thread para receber mensagens do amigo
    receive_thread = threading.Thread(target=receive_messages, args=(connection,))
    receive_thread.start()
    flag = True;

    while flag == True:
        message = input("Você: ")        # Obter mensagem do usuário
        if message == "exit":
            flag = False
        connection.send(message.encode())  # Enviar mensagem para o amigo

    connection.close()  # Fechar a conexão

if __name__ == "__main__":
    main()
