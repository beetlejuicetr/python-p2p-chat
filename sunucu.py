import socket

import threading





sahip = socket.gethostbyname(socket.gethostname())
port = 8436
baglantilar = []

print("""
                                                  
                    %@@@,,,*@@@                   
              @@@@@@@@%,,,,,*@@@@@@@@*            Red Arrow ağına hoşgeldiniz...
          /@@@@@@@@@@#,,,,,,,/@@@@@@@@@@@         
        @@@@@@@@@@@@#,,,,,,,,,,@@@@@@@@@@@@       
      @@@@@@@@@@@@@,,,,,,,,,,,,,@@@@@@@@@@@@@     
     @@@@@@@@@@@@@,,,,,,,,,,,,,,,@@@@@@@@@@@@@#   
   .@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,@@@@@@@@@@@@@%  
   @@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,@@@@@@@@@@@@@  
  *@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,@@@@@@@@@@@@@ 
  @@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,@@@@@@@@@@@@ 
  @@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,@@@@@@@@@@@ 
   @@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@@@@@@* 
   *@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@@@@@  
    /@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@@@   
      @@@,,,,,,,,,,,,,,,@@@,,,,,,,,,,,,,,,@@@     
       .,,,,,,,,,,,,@@@@@@@@@@@,,,,,,,,,,,,@      
       ,,,,,,,,,&@@@@@@@@@@@@@@@@@(,,,,,,,,,      
      ,,,,,,,&@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,     
     ,,,,         #@@@@@@@@@@@@@&        .,,,.

     Devam etmek için 'ENTER' bas.    	

	""")

hosgeldin_mesaji = "Kırmızı Ok'a hoşgeldiniz...\n Sunucu bağlantınız başarıyla kuruldu!"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((sahip,port))

onayli_ipler = []


def sunucuyu_baslat(TH):
	global kullanici_baglandi
	try:
		kullanici_sayisi = input("Maksimum kullanici sayisi: ")
		s.listen(int(kullanici_sayisi))
	except socket.error as bildirim:
		print("Bir hata oluştu: ",bildirim)
	print(TH)


def baglanti_bekle(TH):
	print(TH)
	while True:
		global onayli_ipler

		client,addr = s.accept()

		onayli_ipler_dosya = open("onayli_ipler.txt","r")
		veri = onayli_ipler_dosya.read()

		for ip in veri.split("\n"):
			if ip in onayli_ipler:
				pass
			else:
				onayli_ipler.append(ip)
				print("kayit bulundu:",ip)
				print(addr)
		onayli_ipler_dosya.close()

		if addr[0] in onayli_ipler:
			print("okey!",onayli_ipler)
			baglantilar.append(client)
			client.send(hosgeldin_mesaji.encode())
			print("<Yeni kullanici> ",addr)
			for i in baglantilar:
				try:
					i.send(str(("<Yeni kullanici> ",addr)).encode('utf-8'))
				except socket.error as hata_kodu:
					print("[hata]",hata_kodu)
					baglantilar.remove(i)
					break
		pass

def mesaj_bekleme(TH):
	print(TH)
	while True:
		if baglantilar != []:
			for i in baglantilar:
				try:
					i.settimeout(0.1)
					veri = i.recv(256)

					if veri.decode() != "":
						print(veri.decode())
						for k in baglantilar:
							try:
								k.send(veri)
							except:
								baglantilar.remove(k)
								print("kullanici Ayrildi!")
				except socket.timeout as hata_kodu:
					pass
			

t1 = threading.Thread(target=baglanti_bekle, args = ("Baglanti bekleme aktif !", ))
t2 = threading.Thread(target=mesaj_bekleme, args = ("Mesaj bekleniyor...",))
sunucuyu_baslat("Sunucu Başlatıldı...")
t1.start()
t2.start()