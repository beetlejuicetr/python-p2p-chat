
import socket
from cryptography.fernet import Fernet
import threading


anahtar_dosyasi = open("anahtar.key","r")

anahtar = anahtar_dosyasi.read()

f = Fernet(anahtar)







sahip = socket.gethostbyname(socket.gethostname())
port = 8435

sunucu_port = 8436


lobi = socket.socket()
lobi.bind((sahip,port))
lobi.listen(10)

baglantilar = []


kayitli_hesaplar = []
def kayitli_hesap_cek():
	global kayitli_hesaplar
	dosya = open("hesaplar.txt","r")
	dosya_veri = dosya.read()
	dosya.close()
	for i in dosya_veri.split("\n"):
		kayitli_hesaplar.append(i)
		print(i)
	print(kayitli_hesaplar)
	pass



def baglanti_bekle(TH):
	while True:
		baglanti_izni = False
		istemci,addr = lobi.accept()
		print("mesaj bekleniyo")
		veri = istemci.recv(1024)
		print("mesaj bekleniyo2")
		print(veri)
		veri = f.decrypt(veri)
		veri = veri.decode()
		print(veri)

		for i in kayitli_hesaplar:
			if i == veri and veri != "":
				print("Bu hesap kayıtlı!")
				baglanti_izni = True
		if baglanti_izni:
			baglantilar.append(addr[0])
			print("Basarili!")
			print(baglantilar)
			istemci.send("Kaydınız başarılı!".encode())
			onayli_ipler = open("onayli_ipler.txt","a")
			onayli_ipler.write(addr[0])
			onayli_ipler.write("\n")
			onayli_ipler.close()
			#istemci.close()
		else:
			istemci.send("Kayıt Gerceklesmedi!".encode())
			print("olumsuz!")
			istemci.close()


kayitli_hesap_cek()
t1 = threading.Thread(target=baglanti_bekle, args= ("Thread-1",))
#baglanti_bekle("TH")

t1.start()
