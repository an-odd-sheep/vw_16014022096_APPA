import socket
ob = socket.socket()
ob.connect(('localhost', 2301))
print("client is ready to accept the connection")
ob.close()