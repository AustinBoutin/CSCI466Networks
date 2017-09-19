import socket

class TestClient:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('153.90.233.50', 80))
    s.send(bytes('hello'))
    data = s.recv(1024)
    s.close()
