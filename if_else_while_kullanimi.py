# if else while kullanımı döndüler : dan sonra gelen satıdaki çıkıntıya göre kendine dahil olan ifadeleri belirler.
durum = True
KullaniciAd="evren"
Sifreniz="1234"
i=1
while(durum == True):
 Kullanici=input("Kullanıcı Adı Giriniz:")
 Sifre = input("Sifre Giriniz")
 if (KullaniciAd != Kullanici or Sifreniz != Sifre):
  print("KullaniciAd yada Sifre Yanlış")
 elif(KullaniciAd == Kullanici and Sifre == Sifreniz):
  print("Hoşgeldiniz")
 if(i==2):
      break
 i +=1