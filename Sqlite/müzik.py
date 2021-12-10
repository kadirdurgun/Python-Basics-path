import sqlite3

import time

class Sarkı():

    def __init__(self,isim,sanatci,album,produksiyon_sirket,süre):

        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.produksiyon_sirket = produksiyon_sirket
        self.süre = süre

    def __str__(self):
        return "Sarkı ismi : {}\nSanatci : {}\nAlbum : {}\nProduksiyon Sirketi : {}\nSarki Süresi : {}\n".format(self.isim,self.sanatci,self.album,self.produksiyon_sirket,self.süre)

class Playlist():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur( self ):

        self.baglanti = sqlite3.connect("müzik.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "Create table if not exists sarkılar (isim TEXT,sanatci TEXT,album TEXT,produksiyon_sirket TEXT,süre FLOAT)"
        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def sarkilari_goster( self ):

        sorgu = "Select * from sarkılar"

        self.cursor.execute(sorgu)

        sarkılar = self.cursor.fetchall()

        if (len(sarkılar) == 0):

            print("Liste de sarki bulunamadı..")
        else:
            for i in sarkılar:
                sarkı = Sarkı(i[0],i[1],i[2],i[3],i[4])

                print(sarkı)

    def sarki_ekle( self,sarkı ):

        sorgu = "Insert into sarkılar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(sarkı.isim,sarkı.sanatci,sarkı.album,sarkı.produksiyon_sirket,sarkı.süre))

        self.baglanti.commit()

    def sarki_sil( self,isim ):

        sorgu = "Delete from sarkılar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()

    def sure_toplam( self ):

        sorgu = "Select * from sarkılar"

        self.cursor.execute(sorgu)

        sarkılar = self.cursor.fetchall()

        if (len(sarkılar) == 0):
            print("Listede sarkı bulunamadı . . .")
        else:
            sure = 0
            for rows in range(len(sarkılar)):
                sure += sarkılar[rows][4]
                yenı_sure ='{0:.2f}'.format (sure)
            print ("Playlistin tolam uzunluğu {} dk'dır..".format(yenı_sure))

            self.baglanti.commit ()

























