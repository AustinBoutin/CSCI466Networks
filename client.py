#import requests
import socket
import sys

class Client:
    def __init__(self, master):
        print(sys.argv)
        #sys.argv = [sys.argv[0], ip, port, x, y]
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        print('HERE')
        sock.connect((sys.argv[1], int(sys.argv[2])))
        print(sys.argv[1] + ' ' + sys.argv[2])


    #this might be different with sockets
    def salvo(ip, port, x, y):
        salvo_request = requests.post()
