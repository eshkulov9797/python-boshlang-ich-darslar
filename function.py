# -*- coding: utf-8 -*-

def katta_harf(ismlar):
    i = 0
    katta_isim = []
    
    while ismlar:
        katta_isim.append(ismlar[i].title())
        i = i + 1
    
    return katta_isim
    
        
        
    
    
    

ismlar = ['ali','vali','anton','jalil']

ismlar = katta_harf(ismlar)
print(ismlar)
