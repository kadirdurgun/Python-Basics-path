"""#3e ve 5 e bölünen 100 e kadar sayılar
while(True):
    kilo = float(input("Kilonuzu giriniz: "))
    boy = float(input("Boyunuzu giriniz: "))
    a = float(kilo/boy**2)
    if(a <= 15):
        print("Zayıfsın")
    if (a > 15.0 and a <= 25.0):
        print("Fitsin")
    if (a > 25):
        print("Kilolusun")

#100km de yakılan yakıt miktarı

trip = int(input("Kaç kilometrelik bir yolculuk yaptınız: "))

if trip > 100:
    fuelMultiple = 0.19
    tripCost = trip * fuelMultiple

    print("{1} km'lik yolculuğunuzda yakıt tüketiminiz {0} dir".format(tripCost, trip))
elif trip > 50:
    fuelMultiple = 0.29
    tripCost = trip * fuelMultiple

    print("{1} km'lik yolculuğunuzda yakıt tüketiminiz {0} dir".format(tripCost, trip))
elif trip > 20:
    fuelMultiple = 0.39
    tripCost = trip * fuelMultiple

    print("{1} km'lik yolculuğunuzda yakıt tüketiminiz {0} dir".format(tripCost, trip))
else:
    print("Az bir yol katettiniz...")

# girilen 2 sayı arasındaki tek ve çift sayıları yazdıran kod

def kare():
    kenar=int(input("Karenin kenarını giriniz : "))
    alan=kenar**2
    cevre=kenar*4
    return alan,cevre
print("Karenin alanı ve çevresi : ",kare())

#2.cozum
kenar=int(input("Karenin kenarını giriniz : "))
alan=kenar**2
cevre=kenar*4
print("Karenizin alanı : ",alan)
print("Karenizin cevresi : ",cevre)


#ABS--Mutlak değer
print(abs(-90))
#ROUND-- Aşağı yukarı yönlü sayıları yuvarlama fonks.
print(round(12.6))
# ALL FONKSİçindeki değerlere göre false ve true 0 hariç tüm sayılar true
liste=[1,2,3,4]
print(all(liste))
#ANY-Dizi içindeki değerlerden en az bir tanesi True ise true olarak verir.
liste=["ahmet","mehmet",0]
print(any(liste))
#Bir nesnenin ekrana basılabilir halini verir - ascii
a="Python"
print(ascii(a))

a= "Ömür"  #unicod olarak gösterir
print(ascii(a))

#repr --
a= "Ömür"
print(repr(a))
#bool-- b,r nesnenin true veya false olduğunu söyler
a= "Ömür"
print(bool(a))
#bin fonks bir sayının ikili düzendeki  binary karşılığını verir
print(bin(155)) #0b10011011 çıktısı
#bytes
print(bytes(1))
#chr -- kendisine parametre olarak verinen bir tam sayının karakter karşılığını döndürüyor
print(chr(305))
#set fonk - küme ile listeleme
#tuple  farklı veri tiplerini demetlere dönüştürür-('f', 'e', 'r', 'h', 'a', 't')
print(tuple("ferhat"))
#complex karmaşık sayıların pythondaki karşılığı
print(complex(15,3))
#float- sayıları kesirli sayıları dönüştürür.
#int-karakterleri integer ifadelere dönüştürür.
#dict
a=dict(a=1,b=2,c=3)
print(a)
#ord -karakterin karşılık geldiği ondalık sayısı
print(ord("c"))
#oct fonk  sekizli düzendeki karşılığını verir.
print(oct(10))
#hex fonk - 16lık düzende verir
print(hex(10))
#copyright- python haklarını çıkarır.
print(copyright())
#credits - python kurucularına teşekkür mesajı
print(credits())
#help b,lgi almak istedğimiz fonk bilgisini verir
print(help(dir()))
#id nesnelerin kimleğini işleyişlerini bu konuda bilgi alabildiğimiz bir fonk
a=50
print(id(a))

#input kullanıcı ile veri alışverişi girilmek istenen bilgiler
#format bir veriyi biçimlendirmek için kullanılır
#filter - bir verinin içindeki bir karakteri filtrelemek listelemek
a=[400,123,1256,6765,54,7,7899]
for i in range a:
    if i%2==0:
        print(a)

#Filter
def cift(sayı):
    return sayı%2==0
print(*filter(cift,1))

#hash belli türdeki nesnelere karma bir değere veriyor
print(hash("Ferhat"))
#len
print(len("merhaba"))

#map fonk
liste=[1,2,3,4,5]
def topla(x):
    return x+10
sonuc=map(topla,liste)
print(list(sonuc))

#max bir dizi içerisindeki en büyük ögeyi karşımıza verir
liste=[1,2,3,4,5]
liste=["z","b"]
print(max(liste))

#min dizideki en küçük değeri verir
liste=[1,2,3,4,5]
liste=["berk","ferhat"]
print(min(liste,key=(len))) #en fazla veya en az harfli kelime hangisiyse onu verir
#pow fonk kuvvetini alır 3. terim modunu alır
print(pow(2,6)) #64

#reversed ters çevirir
liste=["berk","ferhat"]
reversed(liste)
print(liste)
#
isimler=["Recai","Mesut","Ferhat"]
reversed(isimler)
print(list(reversed(isimler)))

#sorted elemanları belirli bir ölçüye göre sıralıyor
liste=["ışık","berk","ferhat"]
sorted(liste)
print(liste)
#sum toplama
liste=[1,2,3,4,5]
print(sum(liste,3)) #3 sayısınıda ekler
#type fonks.
a=10
print(type(a))

#kullanıcının girdiği bir sayının faktöriyeli bulduran prog

sayi=int(input("Bir sayı giriniz:"))
sayac=1
for i in range(1,sayi+1,1):
    sayac=sayac*i
print(sayac)

# 5 in 7. kuvvetini 2 tabanında yaz
degisken = pow(2,3)
print(bin(degisken))


liste = [1, 2, 3, 4, 5 ]
def toplam(x):
    return sum(liste)
sonuc = map(toplam,liste)
print(list(sonuc))

#girilen sayının rakamları toplamı
#
name_list=[]
new_list=[]
for i in range(3):
    i=input("İsim giriniz:")
    name_list.append(i)
    new_list.append(hash(i))
print(name_list)
print(new_list)
print(sum(new_list))

#Bir liste tanımla ve bu listeye farklı türde
# 10 eleman ekle. Sonra her bir elemanın türünü ekrana yazdır.
liste1=[]
for x in range (1,10):
    input("bir karakter giriniz")
    liste1.append(x)
for a in (liste1):
    print((type(a)))
#
sayı=int(input("bir sayı giriniz"))
toplam=0
for rakam in range (sayı):
    toplam=toplam+(rakam )
print (toplam)

# listedeki sayıların 2 katını al, map kullan
def toplam(n):
    return 2*n
sayilar=[1,2,3,4]
sonuc=map(toplam,sayilar)
print(list(sonuc))
#
x = [10,20,30,40,50,60]
def iki_kati(x):
    return x*2
sonuc = map(iki_kati,x)
print(list(sonuc))

# Çarpım tablosu
for i in range (1,10):
    print(i)
    for n in range (1,10):
        print("{} x {} = {}" .format(n,i, i*n))
        print(bin(i*n))

#
liste = []
def sort():
    sayi =input("Bir sayı giriniz : ")
    for i in sayi:
        liste.append(i)
    print(sorted(liste))
sort()

#bir liste oluştur ekrana tekrar eden karakterlerin kaç kere çıktı gösterdiği
liste = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 5, 5, 5, 5]
a=list(set(liste))
a.sort()
for i in range(len(a)):
    print(a[i],'=',liste.count(a[i]))


#7 ile 15 sayıları arasındaki
list = []
for i in range(7, 16):
    list.append(pow(i, 4))
list.reverse()
print(list)

list1 = []

#
def get_list():
    for i in range(0, 5):
        temp = input("Bir isim giriniz:")
        list1.append(temp)
    return list1
a = get_list()
print(a)
b = a.reverse
print(b)
#
liste=[]
for a in range(5):
    i=int(input("sayi giriniz"))
    liste.append(i)
print(liste)
print(list(reversed(liste)))
print(sorted(liste))

# HATA YAKALAMA

ilk_sayi=input("İlk sayı:")
ikinci _sayi=input("İlk sayı:")
try:
    sayi=int(ilk_sayi)
    sayı2=int(ikinci_sayi)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
except ValueError:
    print("Lütfen sadece sayı girin!")
except ZeroDivisionError:
    print("Lütfen 0 girmeyiniz")

#try except as
ilk_sayi=input("İlk sayı:")
ikinci _sayi=input("İlk sayı:")
try:
    sayi=int(ilk_sayi)
    sayı2=int(ikinci_sayi)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
except ValueError as hata:
    print(hata)

#
try
    bölünen = int(input("Bölünecek sayı:"))
    bölen = int(input("Bölen sayı:"))
except ValueError:
    print("Lütfen sadece sayı girin")
else:
    try:
        print(bölünen/bölen)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemessiniz")
#
try:
    ...bir takım işler..
except bir hata:
    hata alınca yapılacak işlemler
finally:
    hata olsa da olmasada yapılması gerekenler

#lambda fonk
a=lambda a,b,c:a+b+c
print(a(2,3,4))

kare=lambda num:num**2
print(kare(4))
"""
sayi=int(input("Kaça kadar yazdirilsin :"))

for i in range(1):

    for j in range(1,sayi+1):
        print(j * "*"+ "               " + "{} :i  {}  : j".format(i,j))
#        print("i: {} and j: {}".format(i,j))