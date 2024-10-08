import socket
ob = socket.socket()
ob.bind(('localhost', 2301))
ob.listen(4)
print("server is ready to listen")
clientobject, add=ob.accept()
print("server is ready to accept the connection")
print("connected with this address: ", add)

conn = True
while conn:
    gotmsg = clientobject.recv(1024)
    gotmsg.decode('utf-8')
    print(gotmsg)
    if len(gotmsg) == 0:
        conn = False

ob.close()