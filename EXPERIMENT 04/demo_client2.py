import socket
ob = socket.socket()
ob.connect(('localhost', 2301))
print("client is ready to accept the connection")
msg = 'hello dazai san here'
ob.send(msg.encode('utf-8'))
ob.close()