sayi=int(input("Sayı Giriniz : "))
tek_toplam=0
cift_toplam=0
for i in range(0,sayi+1):
    if (i % 2 != 0 ):
        tek_toplam+=i
    else:
        cift_toplam+=i

print("Teklerin toplamı : ",tek_toplam,"Çiflerin toplamı :",cift_toplam)

