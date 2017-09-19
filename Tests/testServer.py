import socket

class TestServer:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 80))
    s.listen(1)

    conn, addr = s.accept()
    data = conn.recv(1024)
    conn.send(data)
    conn.close()
    
