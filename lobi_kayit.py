import socket
from cryptography.fernet import Fernet

anahtar_dosyasi = open("anahtar.key","r")

anahtar = anahtar_dosyasi.read()

f = Fernet(anahtar)

sahip = input("Sunucu IP : ")
kullanici_adi = input("kullanici adi : ")
sifre = input("Sifre : ")

lobi_port = 8435

lobi_istemci = socket.socket()

def sunucuya_baglanma():
	try:
		lobi_istemci.connect((sahip,lobi_port))
		print("Baglanti saglandi")
		sifreli_bilgiler = ("{}:{}".format(kullanici_adi,sifre)).encode()
		sifreli_bilgiler = f.encrypt(sifreli_bilgiler)
		lobi_istemci.send(sifreli_bilgiler)
		cevap = lobi_istemci.recv(1024)
		print(cevap)
		#lobi_istemci.close()
	except socket.error as hata_kodu:
		print("[hata] ",hata_kodu)

sunucuya_baglanma()
