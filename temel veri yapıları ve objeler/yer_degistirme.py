while(1):
    print("--------- Sayıların Yerini Degistirme Uygulaması----------")

    ilk_alinan=int(input("Birinci Sayiyi giriniz : "))
    ikinci_alinan =int(input("İkinci Sayiyi giriniz :"))

    print("Girdiginiz ilk sayi : {} , ikinci sayi : {} ".format(ilk_alinan,ikinci_alinan))
    ilk_alinan,ikinci_alinan =ikinci_alinan,ilk_alinan
    print("Değişimden sonra Birinci Sayı = {} , İkinci Sayi = {}".format(ilk_alinan,ikinci_alinan))