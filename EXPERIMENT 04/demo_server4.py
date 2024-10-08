import socket


host = 'localhost'
port = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(4)
print(f"server listening on {host} : {port} ")
client_socket, add = server_socket.accept()
print(f"connected by {add}")

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"client :  {data.decode()}")

    msg = input("Server: ")
    client_socket.sendall(msg.encode())

server_socket.close()
client_socket.close()




