print("""
*******************************
HESAP MAKİNESİ

İŞLEMLER

1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme

*******************************
""")
while(1):
    a = int(input("Birinci Sayi:"))
    b = int(input("İkinci Sayi :"))

    islem = int(input("Lütfen işlem seçiniz :"))
    if (islem == 1):
        print("{} ile {} sayılarının toplamı {} dur...".format(a, b, a + b))
    elif (islem == 2):
        print("{} ile {} sayılarının farkı {} dur...".format(a, b, a - b))
    elif (islem == 3):
        print("{} ile {} sayılarının çarpımı {} dur...".format(a, b, a * b))
    elif (islem == 4):
        print("{} ile {} sayılarının bölümü {} dur...".format(a, b, a / b))
    else:
        print("Geçersiz islem girdiniz...")