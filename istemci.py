import socket
import threading
sahip = input("Sunucu Ip: ")
#'100.83.105.219'
#socket.gethostbyname(socket.gethostname())
port = 8436
kullanici_adi = "user"
istemci = socket.socket()
def sunucuya_baglanma():
	global kullanici_adi
	kullanici_adi = input("kullanici adi : ")
	try:
		istemci.connect((sahip,port))
		#veri = istemci.recv(1024)
		#print(veri.decode())
		#istemci.send(kullanici_adi.encode('utf-8'))

	except socket.error as bildirim:
		print("Bir hata oluştu: ",bildirim)



def mesaj_bekleme():
	print("mesaj ilk")
	while True:
		try:
			veri = istemci.recv(1024)
			if veri.decode() != "" and veri.decode() != None:
				print(veri.decode())
		except Exception as hata_kodu:
			istemci.close()
			break


def mesaj_atma():
	print("mesaj at iki")
	while True:
		#istemci.send("".encode('utf-8'))
		mesaj = input()
		if mesaj != " " and mesaj != "" and mesaj != None:
			try:
				istemci.send(str('< {} > '.format(kullanici_adi)+mesaj).encode('utf-8'))
			except Exception as hata_kodu:
				istemci.close()
				break

t1 = threading.Thread(target=mesaj_bekleme)
t2 = threading.Thread(target=mesaj_atma)
sunucuya_baglanma()

t1.start()
t2.start()


