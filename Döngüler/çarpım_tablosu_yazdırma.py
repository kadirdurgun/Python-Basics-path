sayi=int(input("Kaça kadar yazdirilsin :"))

for i in range(1,11):
    print("****************************")
    for j in range(1,sayi+1):
        print("{} x {} = {}".format(i,j,i*j))
