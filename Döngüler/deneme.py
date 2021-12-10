#Kullanıcıdan alınan iki sayının arasındaki çift sayıların ortalamasının bulunması

sayi1=int(input("1. Sayıyı giriniz: "))
sayi2=int(input("2. Sayıyı giriniz: "))
sayi_adet=0

if ((sayi2-sayi1) % 2 == 0):
    sayi_adet = ((sayi2 - sayi1) / 2) - 1
else:
    sayi_adet = ((sayi2-sayi1)-1) / 2

def f(sayi1,sayi2):
    toplam = 0
    for sayı in range(sayi1+1,sayi2):
        if (sayı % 2 == 0):
            toplam +=sayı

    return (toplam/sayi_adet)

print("sayı adet",sayi_adet)

print("Çift sayıların ortalaması : ",f(sayi1,sayi2))