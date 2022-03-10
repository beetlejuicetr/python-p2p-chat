import socket

host = socket.gethostname()
port = 3113

try:
	cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cli.connect((host,port))
	print("servere baglanildi")
except socket.error as bildirim:
	print("hata",bildirim)
