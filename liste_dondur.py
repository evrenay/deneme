#Liste döndür

Liste= []
Liste2 = []

Liste.append("Sampiyon")
Liste.append("Bursaspor")
Liste.insert(0,"deneme")
Liste.insert(10,"deneme2")
Liste2.append("test1")
Liste2.append("test2")
Liste2.append("test3")
del Liste [0]
Liste2.remove("test1")
print(Liste2)
for i in Liste:
    print(i)
print(Liste)


print("Listenin Uzunluğu="+str(len(Liste)))

