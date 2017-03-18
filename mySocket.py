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

    def makefile(self):
        return self.conn.makefile('VideoStream')
        
    def connect(self):
        self.conn, self.addr = self.s.accept()
        print('Connected with ', self.addr[0], ':',  str(self.addr[1]))

    def recData(self):
        try:
            return self.conn.recv(16)
        except socket.timeout:
            raise timeOut('Timeout on ', self.conn)

    def getData(self, data, lsb, msb):
        return int.from_bytes(data[lsb:msb], byteorder='little', signed=True)

    def sendData(self, data):
        try:
            self.conn.send(data)
        except socket.timeout:
            raise timeOut('Timeout on ', self.conn)
        
    def setTimeOut(self):
        self.s.settimeout(5)

    def end(self):
        self.conn.close()
        self.s.close()
