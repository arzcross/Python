import socket

host = '192.168.78.1'
port = 50000
backlog = 5
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        print('data: %s' % data)
        msg = 'Got your message!'
        client.send(msg.encode())
    client.close()
