toplam=0
while True:
    sayi=input("Sayi Giriniz:")

    if(sayi == "q"):
        break
    sayi=int(sayi)
    toplam+=sayi
print("Girdiginiz Sayilar Toplamı :",toplam)


