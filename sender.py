import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
recv_addr=("127.0.0.1",9999)
user_data=input("enter your message: ")
newdata=user_data.encode('ascii')
s.sendto(newdata, recv_addr)
print("your message has been sent ....")
