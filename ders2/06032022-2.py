liste=[] #boş bir liste tanımlar
liste=["elma","Armut",20] #artık listenin elemanları değişti
sayiler=[15,19,2,3,8,25,6]
isimler=["ali","veli","ahmet","zehra","hatice"]
gunler=["Pazartesi","Salı","Çarşamba"]
print(gunler)
print("0. indeksdeki eleman:",gunler[0])
print(gunler[1])
print(gunler[2])
gunler.append("Perşembe") #append: yeni eleman ekler
print(gunler)
print("Eleman sayısı:",len(gunler)) #len: listenin eleman sayısını verir
gunler.pop() #hiçbirşey yazmadığında listenin son elemanını çıkarır
gunler.pop(0) #0. indeksteki elemanı siler
print(gunler)
print(sayiler)
sayiler.sort() #varsayılan(default) olarak küçükten büyüğe sıralar
print(sayiler)
sayiler.sort(reverse=True) #büyükten küçüğe doğru sıralar
print(sayiler)
isimler.sort()
print(isimler)
