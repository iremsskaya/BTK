import os
while True:
    print("1-klasör oluştur")
    print("2-klasör sil")
    secim=input("seçiminiz:")
    if secim=="1":
        ad=input("oluşturmak istediğiniz klasor adı giriniz:")
        for i in range(1, 11):
            os.mkdir("elma" + str(i))
    elif secim=="2":
        ad=input("silinecek klasör adını giriniz:")
        for i in range(1, 11):
            os.rmdir("elma" + str(i))
