import socket
ob = socket.socket()
ob.bind(('localhost', 2301))
ob.listen(4)
print("server is ready to listen")
clientobject, add=ob.accept()
print("server is ready to accept the connection")
print("connected with this address: ", add)
ob.close()