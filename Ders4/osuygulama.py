import os
try:
    os.mkdir("elma") #klasor oluşturur
except FileExistsError:
    print("aynı adla klasor var")

