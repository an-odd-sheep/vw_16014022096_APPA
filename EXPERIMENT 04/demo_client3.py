import socket
ob = socket.socket()
ob.connect(('localhost', 2301))
print("client is ready to send data")

conn = True
while conn:
    msg = input("enter your message: ")
    if msg == 'no':
        conn = False
    else:
        ob.send(msg.encode('utf-8'))


ob.close()

