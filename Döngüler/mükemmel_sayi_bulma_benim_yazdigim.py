print("""*******************
Mükemmel Sayi Bulma Programı

Programdan çıkmak için '0' ya basın.
*******************""")
while True :
    alinan_sayi=int(input("Sayi:"))
    ilk_liste=list(range(1,alinan_sayi+1))
    yeni_liste=[]
    toplam=0
    if(alinan_sayi==0):
        print("Program sonlandırıldı . . . ! ! !")
        break

    for i in ilk_liste:
        if(alinan_sayi%i==0):
            yeni_liste.append(i)
    for j in yeni_liste:
        toplam += j
    if((toplam-alinan_sayi)==alinan_sayi):
         print("Girdiğiniz Sayi Mükemmel Sayidir . . .  Tebrikler. . . ")
    else:
        print("Girilen Sayı mükemmel Sayi Degildir.......! ! !")





