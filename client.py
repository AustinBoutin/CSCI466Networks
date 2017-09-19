#import requests
import socket
import sys

class Client:
    if __name__ == '__main__':
        
        print(sys.argv)
        sys.argv = [sys.argv[0], '153.90.233.55', 3333, 4, 3]
        ip = sys.argv[1]
        port = sys.argv[2]
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        print('HERE')
        sock.connect((ip, port))
        sock.send(bytes(x))
        sock.close()
        print(ip + ' ' + sys.argv[2])


    #this might be different with sockets
    def salvo(ip, port, x, y):
        salvo_request = requests.post()
