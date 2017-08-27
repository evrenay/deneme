#fonksiyonun içindeki yerel bi değişkeni global tipiyle tanımlarsak fonsiyon içinde o değişkene yapılacak
#herhangi bir değişiklikte yerelde değil globalde değişim olur.
a=10
def fonksiyo():
    global a
    a=2
    print(a)

fonksiyo()
print(a)