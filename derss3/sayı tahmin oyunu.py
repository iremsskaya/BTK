sayi=3
while True:
    sayi=int(input("tahmininiz:"))
    if sayi<tuttugumsayi:
        print("bilemedin , sayınızı büyütün")
    elif  sayi>tuttugumsayi:
        print("bilemedin,sayınızı küültün")
    else:
        print("tebrikler")
        break