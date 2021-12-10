
def okunusu(sayi):
    birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    yüzler =["","yüz","ikiyüz","üçyüz","dörtyüz","beşyüz","altıyüz","yediyüz","sekizyüz","dokuzyüz"]

    if(sayi<100):
        birler_basamak = sayi % 10
        onlar_basamak = sayi // 10
    else:
        birler_basamak = sayi % 10
        gecici_sayi = sayi // 10
        onlar_basamak = gecici_sayi % 10
        yüzler_basamak = gecici_sayi // 10

    return yüzler[yüzler_basamak]+" "+onlar[onlar_basamak]+" "+birler[birler_basamak]
while True:
    print("*********************Girilen Sayının Okunusunu Yazdıran Program -------- Maximum 3 Basamaklı Sayı Giriniz ********************* ")
    sayi = int(input("Sayi giriniz :"))
    print(okunusu(sayi))

