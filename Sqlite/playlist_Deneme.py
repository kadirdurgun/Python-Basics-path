from müzik import *

print("""***********************************
Playlist Programına Hoşgeldiniz.
İşlemler;
1. Sarkıları Göster
2. Sarkı Ekle
3. Sarkı Sil 
4. Toplam Playlist Süresi Göster

Çıkmak için 'q' ya basın.
***********************************""")

playlist = Playlist()

while True:
	islem = input("Yapacağınız İşlem :")

	if (islem == "q") :
		print ("Program Sonlandırılıyor.....")
		print ("Yine bekleriz....")
		break

	elif (islem == "1"):
		playlist.sarkilari_goster()

	elif (islem == "2"):

		isim = input("İsim :")
		sanatci = input("Sanatcı :")
		album = input("Album :")
		produksiyon_sirket = input("Prodüksiyon Şirketi :")
		süre = float(input("Sarkı Süresi :"))

		yeni_sarki = Sarkı(isim,sanatci,album,produksiyon_sirket,süre)

		print ("Sarkı ekleniyor....")
		time.sleep (2)

		playlist.sarki_ekle(yeni_sarki)
		print ("Sarki Eklendi....")

	elif (islem == "3") :
		isim = input ("Hangi sarkıyı silmek istiyorsunuz ?")

		cevap = input ("Emin misiniz ? (E/H)")
		if (cevap == "E") :
			print ("Sarkı Siliniyor...")
			time.sleep (2)
			playlist.sarki_sil (isim)
			print ("Sarkı silindi....")

	elif (islem == "4"):

		playlist.sure_toplam()



	else :
		print ("Geçersiz İşlem...")