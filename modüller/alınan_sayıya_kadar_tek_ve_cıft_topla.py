sayi=int(input("Sayı Giriniz : "))
tek_toplam=0
cift_toplam=0
tek_list=list()
cift_list=list()

for i in range(0,sayi+1):
    if (i % 2 != 0 ):
        tek_list.append(i)
    else:
        cift_list.append(i)
for j in tek_list:
    tek_toplam+=j
for k in cift_list:
    cift_toplam+=k
print(tek_list)
print(cift_list)
print("Teklerin toplamı : ",tek_toplam,"Çiflerin toplamı :",cift_toplam)


