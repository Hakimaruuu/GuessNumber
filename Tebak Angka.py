# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:16:58 2020

@author: ASUS
"""

import random;

print("Pikirkan angka random dari 1 sampai 1000")
print("Ingat, jangan bohong dosa")

tebak = int(random.randrange(1,1000))
i = 0;
atas = 1000;
bawah = 1;

while (i<10):
    print(" ")
    print("Apakah angka yang dipikirkan ",tebak)
    jawaban = input("Jawaban (up/down/ya) :")
    if jawaban == 'ya':
        print("yess")
        break
    elif jawaban == 'up':
        bawah = tebak;
    elif jawaban == 'down':
        atas = tebak;
        
    tebak = int(random.randrange(bawah,atas))
    if bawah == atas:
        print("boong lu")
        break
    else:
        i=i+1
    
else:
    print("nyerah dah")