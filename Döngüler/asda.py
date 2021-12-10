

ilk_liste = [12,15,22,55,567,99,32]
ikinci_liste = [13,24,567,87,90,32,15]
son_liste = list()

for i in range(len(ilk_liste)):
    for j in range (len(ikinci_liste)):
        if (ilk_liste[i] == ikinci_liste[j]):
            print("ilk listenin {} . indisi ile İkinci listenin {} . indisi eşittir ".format(i,j))
            son_liste.append(ilk_liste[i]+ikinci_liste[j])


print(son_liste)