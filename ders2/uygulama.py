#kulanıcıdan ad soyad telefon alarak bilgiler adlı listeye atayınız
bilgiler=[] #boş liste tanımlar

isim=input("Adınız:")
print("Hoşgeldin",isim)
soyadı=input("Soyadınız:")
print(soyadı)
telefonnumarası=input("Telefon numaranız:")
print(bilgiler)
bilgiler.append(isim)
bilgiler.append(soyadı)
bilgiler.append(telefonnumarası)
print(bilgiler)
#ilk başta boş bir liste açtık sonra inputu kullanarak gerekli bilgileri istedik bilgiler append yapıp elemanları listenin içine attık
