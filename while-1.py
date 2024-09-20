# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:15:00 2024

@author: Root
"""

taklif = "Salom xush kelibsiz bizning muzeyimizga !!!"
shart = True

while shart:
    print(taklif)
    yosh = input("yoshingizni kiriting : ")
    if yosh == 'exit' or yosh == 'quite':
        break
    else:
        yosh = int(yosh)
    
        
    if yosh >= 0 and yosh < 7:
        print(f"Sizning yoshingiz {yosh} sizning kirishingiz uchun 2000 so'm chipta narxi")
    elif yosh>=7 and yosh < 18:
        print(f"Sizning yoshingiz {yosh} sizning kirishingiz uchun 3000 so'm chipta narxi")
    elif yosh>=18 and yosh < 65:
        print(f"Sizning yoshingiz {yosh} sizning kirishingiz uchun 10000 so'm chipta narxi")
    elif yosh>=65:
        print(f"Sizning yoshingiz {yosh} siz bepul kirishingiz mumkin !!!")
    
    