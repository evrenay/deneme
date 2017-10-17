sozluk={}
sayac=1
while(sayac==1):
    kelime= input("sözlüge bir kelime ekleyiniz?")
    keys=input("sözlüğe bir değer girin")
    sozluk[keys]=kelime
    for i in sozluk:
        print(i + "\t :"+ sozluk[i])
