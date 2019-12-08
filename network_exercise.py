# 服务端
from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = 'localhost'
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
	def handler(self):
		print("-----connected form:{}-----".format(self.client_address))
		self.wfile.write("[{}] {}".format(ctime(),self.rfile.readline()))

def main():
	tcpServ = TCP(ADDR, MyRequestHandler)
	print("-----waiting for connect-----")
	tcpServ.serve_forever()


if __name__ == '__main__':
	main()

####################################
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	data = input("> ")
	if not data:
		break

	tcpCliSock.send("{}\n".format(data).encode())
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print(data.decode().strip())
	tcpCliSock.close()
