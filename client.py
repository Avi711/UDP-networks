from ctypes import sizeof
import socket
import sys


IP = sys.argv[1]
PORT = int(sys.argv[2])
FILE_NAME = sys.argv[3]
file = open(FILE_NAME, 'r')
CONTENT = file.read()

CONTENT = [CONTENT[i: i + 97]
 for i in range(0, len(CONTENT), 97)
 ]



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(6)

pack_num = 0

for pack in CONTENT:
    print("enter to for loop")
    pack = f"{pack_num:03}" + pack
    arr = bytes(pack, 'UTF-8')
    
    s.sendto(arr, (IP, PORT))
    while(True):
        print("before recieve")
        try:
            data, addr = s.recvfrom(1024)
            print("recieved******************************************")

        except socket.timeout:
            print("time out")
            s.sendto(arr, (IP, PORT))
            continue

        
        print("after recieve")
        print("data", data)
        print("arr", arr)
        if (data == arr):
            break
    pack_num += 1



print("OK")
file.close
s.close
