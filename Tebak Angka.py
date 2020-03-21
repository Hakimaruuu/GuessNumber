# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:16:58 2020

@author: ASUS
"""

import random;

main = 'y'
start = 1
end = 1000
jawab = 'n'
bawah = start
atas = end

def processing(jawab,atas,bawah,angka):
    if jawab == 'a':
        if angka > bawah :
            bawah = angka + 1;
            
        angka = random.randint(bawah,atas)
        
    if jawab == 'b':
        if angka < atas :
            atas = angka - 1;
        angka = random.randint(bawah,atas)
    
    return angka,atas,bawah;

while main == 'y':
    bawah = start
    atas = end
    angka = random.randint(bawah,atas)
    i = 0
    jawab = 'n'
    
    while jawab != 'y':
        print("")
        print("------------------------------------------------------------------")
        print("")
        print("Iterasi ke-",i+1)
        print("")
        print('Pikirkan angka dari 1 sampai 1000 :',angka)
        jawab = input('Apakah angka anda lebih (a), kurang (b), benar (y) ? : ')
        
        if jawab == 'y':
            break
        
        if atas==bawah or atas-bawah==1 :
            print("")
            print("Angkanya pasti",atas,"atau",bawah,)
            break
        
        if angka==1 :
            print("")
            print("Angkanya pasti",angka,"orang batas bawahnya 1 kok")
            break
        elif angka==999 :
            print("")
            print("Angkanya pasti",angka,"orang batasnya 1000 ga ikutan kok")
            break
        else :
            angka, atas, bawah = processing(jawab,atas,bawah,angka)
        
        i = i + 1;   
    else :
        print("")
        print("Nyerah saya")
    print("")
    print("HAHAHA") 
    main = input("Lanjut? (y/n) :")
