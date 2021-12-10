
#Elinizde uzunca bir string olsun.
#"ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
#Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın

string1= "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynbKadirDurgun,asdafsdfadasdada"
frekans = dict()

for harf in string1:
    if(harf in frekans):
        frekans[harf] += 1
    else:
        frekans[harf] = 1
for i,j in frekans.items():
    print(i,":",j)