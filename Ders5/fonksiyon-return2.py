#dikdörtgenin alanını ve çevresini hesaplayan 2 ayrı
#fonksiyon yazınız. kullanıcıdan aldığınız değere göre
#alanı ve çevreyi ekrana yazdırınız

def alan(a,b):
    return a*b

def cevre(a,b):
    return (a+b)*2

kisa_kenar=int(input("kısa kenar:"))
uzun_kenar=int(input("uzun kenar:"))
print("dikdörtgenin çevresi:",cevre(kisa_kenar,uzun_kenar))
print("dikdörtgenin alanı:",alan(kisa_kenar,uzun_kenar))




