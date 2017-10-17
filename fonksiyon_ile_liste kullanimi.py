
Liste=[]
minimum = 0;
def TakeNumber():
    for i in range(1, 6):
      number = int(input(str(i)+". sayiyi giriniz ?"))
      Liste.append(number)
    return Liste



def OrtalamaAl():
    toplam=0
    sayac=0
    for i in range(1,6):
     eleman = Liste.pop(0)
     toplam = eleman+ toplam
     sayac = sayac+1
    return toplam/sayac

print(str(TakeNumber()))
print("ortalama= "+str(OrtalamaAl()))
