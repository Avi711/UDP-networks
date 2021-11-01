import socket
import sys


PORT = int(sys.argv[1])

current = -1
previous = 0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', PORT))

while True:
    previous = current
    data, addr = s.recvfrom(1024)
    pack_num = data[:3]
    data_only = data[3:-2]
    current = pack_num
    if (int(current) > int(previous)):
        print(str(data_only),end ="")
    #    print(pack_num)
    #    print(str(data_only), addr)
    s.sendto(data, addr)
