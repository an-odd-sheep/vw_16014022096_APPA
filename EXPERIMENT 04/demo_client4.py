import socket


host = '192.168.1.48'
port = 1234

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:

    message = input("Client: ")
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print(f"Server: {data.decode()}")

    if message.lower() == 'exit' or data.decode().lower() == 'exit':
        break

client_socket.close()

