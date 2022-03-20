#kullanıcıdan bir sayı girmesi isteyin
#sayı girmediğinde tekrar tekrar girmesini isteyen ,
#sayı girdiğinde ekrana sayının karesini yazdıran program

while True:
    try:
        sayi=int(input("bir sayı giriniz:"))
        print("karesi:",sayi*sayi)
    except ValueError:
        print("sayı giriniz!")


