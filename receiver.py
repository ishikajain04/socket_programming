import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("0.0.0.0",9999))

while True:
    data_recv= s.recvfrom(100)
    print(data_recv)
    reply=("thanks for connecting....")
    s.sendto(reply.encode('ascii'),data_recv[1])