import socket

host = '192.168.78.1'
port = 50000
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#mymsg = 'Hello world!'
s.send(('Hello world!').encode())
data = s.recv(size)
s.close()
print('Recieved from server: %s' % data)
