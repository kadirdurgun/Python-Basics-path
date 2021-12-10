

class PC():
    def __init__(self,pc_durum="Kapalı",pc_ses=0,pc_parola="12345"):
        self.pc_durum = pc_durum
        self.pc_ses = pc_ses
        self.pc_parola = pc_parola

    def pc_ac(self):
        if (self.pc_durum == "Açık"):
            print("Bilgisayar zaten açık....")
        else:
            sifre=input("Bilgisayar Parolası Giriniz :")
            if(sifre == self.pc_parola):
                self.pc_durum = "Açık"
                print(" Tebrikler Doğru Şifre girdiniz .. ")
            else:
                print("Hatalı Şifre Girdiniz..")


    def pc_kapat(self):

        if (self.pc_durum == "Kapalı"):
            print("Bilgisayar Zaten Kapalı..")
        else:
            print("Bilgisayar Kapanıyor....")
            self.pc_durum = "Kapalı"


    def pc_sesayar(self):
        while True:

            ses_cevap = input("Sesi artır : '+'\nSesi azalt : '-'\nÇıkıs : 'cıkıs'")
            if (ses_cevap == "+" and self.pc_durum == "Açık"):

                if (self.pc_ses <= 31):
                    self.pc_ses += 1
                    print("Ses Seviyesi :",self.pc_ses)


            elif (ses_cevap == "-" and self.pc_durum == "Açık"):
                if (self.pc_ses != 0):
                    self.pc_ses -= 1
                    print("Ses Seviyesi :",self.pc_ses)


            else:
                print("Ses Güncellendi :", self.pc_ses)
                break


    def pc_denetim(self):
        if (self.pc_durum == "Açık"):
            print("Yapmak istadiğiniz işlemi Seciniz ..\n1 - Parola değiştirme\n2 - Parola Sıfırlama\n ")
            denetim_cevap=input("İşlem :")
            print("Denetim masasına erişmek için parola girmelisiniz .. ")
            temp_parola=input("Parola : ")

            if(temp_parola==self.pc_parola and denetim_cevap == "1"):
                yeni_parola=input("Yeni Parola Giriniz :")
                self.pc_parola=yeni_parola
            elif(temp_parola==self.pc_parola and denetim_cevap == "2"):

                self.pc_parola=""
                print("Parola Basarıyla Sıfırlandı..")
            else:
                print("Hatalı Parola Girdiniz ...")
        else:
            print("Bilgisayarın açık olduğundan emin olun...")




    def __str__(self):
        return "Pc Durumu: {}\n".format(self.pc_durum)





bilgisayar=PC()

print("""
    Bilgisayar Uygulaması
    1. Pc Aç
    2. Pc Kapat
    3. Pc Durumu Kontrol
    4. Pc Ses Ayarı
    5. Denetim Masası
    

    Çıkmak için 'q' ya basın.
    """)

while True:

    secim = input("Secim Yapınız :")

    if(secim == "q"):
        break

    elif(secim == "1"):
        bilgisayar.pc_ac()

    elif(secim == "2"):
        bilgisayar.pc_kapat()

    elif(secim == "3"):
        print(bilgisayar)

    elif(secim == "4"):
        print("Ses Ayarının Yapılabilmesi için Bilgisayarın Açık olduğundan emin olunuz ... ! ! ! ")
        bilgisayar.pc_sesayar()

    elif (secim == "5"):
        bilgisayar.pc_denetim()

    else:
        print("Geçersiz Seçim...")

