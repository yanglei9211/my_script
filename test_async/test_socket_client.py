import socket
import sys

host, port = "localhost", 9001
# print(sys.argv)
data = " ".join(sys.argv[1:])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    sock.sendall(bytes(data + "\n", "utf-8"))
    rec = str(sock.recv(1024), "utf-8")
print("Sent: %s" % data)
print("Rec:  %s" % rec)

