# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:16:58 2020

@author: ASUS
"""

import random;

main = 'y'
jawab = 'n'
angka = 1000
coba = 1
run = 0
model = 0
mod = [1000,500,250,125,62,31,15,7,3,1]


def processing(jawab,iterate,angka,run,model):
    if jawab == 'a':
        if angka == 1000:
            angka = angka
        else:
            angka = angka + mod[iterate]
        iterate = iterate + 1
        
        if angka == 1000:
            model = 0
        elif angka == 0:
            model = 2
        elif angka != 0 and angka != 1000:
            model = 1
            
        if coba == 10:
            run = 1
    
    if jawab == 'b':
        if angka == 0:
            angka = angka
        else:
            angka = angka - mod[iterate]
        
        iterate = iterate + 1
        
        if angka == 0:
            model = 2
        elif angka == 0:
            model = 1
        elif angka != 0 and angka != 1000:
            model = 1
                
        if coba == 10:
            run = 1
            
    return angka, iterate, run, model;

while main == 'y':
    i = 1
    angka = 1000
    run = 0
    model = 0
    jawab = 'n'
    
    while i<10 :
        angka, i, run, model = processing(jawab,i,angka,run,model)
        
        print("")
        print("------------------------------------------------------------------")
        print("")
        print("Iterasi ke-",i)
        print("")
        print('Pikirkan angka dari 1 sampai 1000 :',angka)
        print("model : ",model)
        
        
        
        if model == 0:
            jawab = input('Apakah angka anda kurang (b), benar (y) ? : ')
        elif model == 1:
            jawab = input('Apakah angka anda lebih (a), kurang (b), benar (y) ? : ')
        elif model == 2:
            jawab = input('Apakah angka anda lebih (a), benar (y) ? : ')
        
        if model == 0 and jawab == 'a':
            i = i - 1
            angka = 1000
        elif model == 2 and jawab == 'b':
            i = i - 1
            angka = 0
        else:
            i = i
        
        if run == 1:
            break
        if jawab == 'y':
            break
    else :
        print("")
        print("Anda pasti berbohong")
    print("")
    print("HAHAHA") 
    main = input("Lanjut? (y/n) : ")
