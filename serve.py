import socket

host = socket.gethostname()
port = 3113

try:
	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	print("soket {} nolu portu baglandi".format(port))
	s.listen(5)
	print("soket dinleniyor...")
except socket.error as bildirim:
	print("hata ",bildirim)
	
while True: 

   # Client ile bağlantı kurulursa 
   c, addr = s.accept()#Gelen  istekleri kabul eden methodu çağırdık....      
   print('Gelen bağlantı:', addr)

   # Bağlanan client a mesaj gönderelim.  
   mesaj = 'Bağlantı Başarılı :)'
   c.send(mesaj.encode('utf-8')) 

   # Bağlantıyı sonlandıralım 
   c.close()
