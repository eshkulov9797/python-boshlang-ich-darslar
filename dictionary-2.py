# -*- coding: utf-8 -*-
dictionary = {'int':'butun son','for':'takrorlanish sikli','if':'shart operatori','else':'yoki shart operatori','def':'funksiya'}

#for key,value in sorted(dictionary.items()):
#   print(f"{key} - {value}")

davlatlar = {'O\'zbekiston':'Toshkent','Qozog\'iston':'Astana','Qirg\'iziston':'Boku','Tojikiston':'Dushanbe'}

poytaxt = input("Davlatni kiriting kiriting : ")

shart = davlatlar.get(poytaxt)
if shart == None:
    print("kechirasiz bunaqa malumot yoq")
else:
    print(f"{poytaxt.title()} ning poytaxti {shart.title()}")
    
    
    