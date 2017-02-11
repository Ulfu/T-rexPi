import socket
import sys

class serverSocket:
    def __init__(self, host, port):
        self.Host = host
        self.Port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(1)
        print('Socket listens on port ', port)
    def connect(self):
        self.conn, addr = self.s.accept()
        print('Connected with ', addr[0], ':',  str(addr[1]))

    def recData(self):
        return self.conn.recv(16)

    def getData(self, data, lsb, msb):
        return int.from_bytes(data[lsb:msb], byteorder='little', signed=True)

    def sendData(self, data):
        s.sendall(data)
        
    
