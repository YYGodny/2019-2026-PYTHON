import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind('bc:f4:d4:b0:31:da', 4)
server.listen(1)

client, addr = server.accept()
