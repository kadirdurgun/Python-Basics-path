def cift_kontrol(sayi):
    if (sayi % 2 == 0):
        return sayi
    else:
        raise ValueError
liste = [24,68,69,53,25,27,15698,22,10,8]

for i in liste:
    try:
        print(cift_kontrol(i))
    except ValueError:
        pass