print("------ Arac Yakıt hesaplama ------")
print("------ Yakıt Litre Fiyatı 8.2 TL varsayılmaktadır -----")
yakıt_litre_fiyati = 8.2

alinan_litre=int(input("Kaç litre yakıt aldınız ? "))
gidilen_mesafe=int(input("Kaç km yol gittiniz ?"))

km_yakıt=(yakıt_litre_fiyati*alinan_litre)/gidilen_mesafe

yüzkm_yakıt_litre=(100*alinan_litre)/gidilen_mesafe
print("--- Aracınız km de {} TL yakıt yakmaktadır.  .   .   ---".format(float(km_yakıt)))
print("--- Aracınız 100 km de {} lt yakıt yakmaktadır.  .   .    -- ".format(float(yüzkm_yakıt_litre)))