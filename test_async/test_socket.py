from socketserver import TCPServer
from socketserver import BaseRequestHandler, StreamRequestHandler


class TestTCPHandler(StreamRequestHandler):
    def handle(self):
        print("begin do request")
        self.data = self.request.recv(1024).strip()
        for x in self.client_address:
            print(x)
        print("{} wrote: ".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    host, port = "localhost", 9001
    with TCPServer((host, port), TestTCPHandler) as server:
        print("serving tcp on port: %d" % port)
        server.serve_forever()
