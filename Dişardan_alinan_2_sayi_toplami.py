# dışarıdan alınan 2 sayının toplamı
ilksayi = int(input("1. sayiyi giriniz = "))
ikincisayi = int(input("2. sayiyi giriniz = "))

def topla(birinci,ikinci):
    sonuc = birinci+ikinci
    return sonuc

sonuc = topla(ilksayi,ikincisayi)
print(sonuc)