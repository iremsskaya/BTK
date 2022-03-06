#BELGE
puan= input("Ortalamanı gir: ")
if int(puan) < 0 or int(puan) > 100:
    print("0 ile 100 arasında bir sayı gir")
elif int(puan) >= 85:
    print("Takdir Aldın.")
elif int(puan) >= 70:
    print("Teşekkür Aldın")
elif int(puan) < 70:
    print("Belge Alamadın")
else:
    print("Lütfen Geçerli Bir Sayı Gir")

