try:
    ilk_sayi = input("Birinci Sayi Giriniz.")
    ikinci_sayi = input("İkinci Sayiyi Giriniz.")
    sonuc = float(ilk_sayi)/float(ikinci_sayi)
    print(sonuc)
except ZeroDivisionError:
    print("İkinci sayi0 dan farklı Giriniz.")
except ValueError:
    print("Harf yerine sayı giriniz.")