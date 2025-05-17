import time 

import random


karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

a = input("Parola hangi uzunlukta olsun : ")

parola = ""


for i in range(int(a)):
    parola += random.choice(karakterler)
print(parola)
