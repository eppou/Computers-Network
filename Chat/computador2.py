import socket
import threading

def receive_messages(connection):
    while True:
        data = connection.recv(1024).decode()
        print(f"Amigo: {data}")

def main():
    host = input("digite o endereço ip: ")  # Endereço IP local
    port = input("digite a porta de comunicação desejada: ")       # Porta para comunicação

    # Conectar ao amigo
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, int(port)))

    # Iniciar uma thread para receber mensagens do amigo
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input("Você: ")        # Obter mensagem do usuário
        client.send(message.encode())     # Enviar mensagem para o amigo

    client.close()  # Fechar a conexão

if __name__ == "__main__":
    main()