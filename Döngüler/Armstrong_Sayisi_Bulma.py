alinan_sayi=input("Sayi :")
basamak_sayisi=len(alinan_sayi)
print("Alinan sayi:",alinan_sayi,"Basamak Sayisi : ",basamak_sayisi)
alinan_sayi=int(alinan_sayi)
basamak=0
toplam=0
gecici_sayi=alinan_sayi
while(gecici_sayi>0):
    basamak=gecici_sayi%10
    toplam += basamak ** basamak_sayisi
    gecici_sayi//= 10
    print("Toplam : ",toplam)
if (toplam==alinan_sayi):
    print("Girdiginiz Sayi bir Armstrong Sayisidir ... Tebrikler . . . ")
else:
    print("Malesef Girilen Sayi Armstrong Sayisi DEĞİLDİR ! ! !. . . ")


