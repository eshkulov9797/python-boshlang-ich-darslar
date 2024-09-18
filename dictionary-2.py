# -*- coding: utf-8 -*-
dictionary = {'int':'butun son','for':'takrorlanish sikli','if':'shart operatori','else':'yoki shart operatori','def':'funksiya'}

#for key,value in sorted(dictionary.items()):
#   print(f"{key} - {value}")

davlatlar = {'O\'zbekiston':'Toshkent','Qozog\'iston':'Astana','Qirg\'iziston':'Boku','Tojikiston':'Dushanbe'}

print("\n Davlat nomlari :::\n")
for key in davlatlar.keys():
    print(key)

print("\nPoytaxtlar:::\n")
for poytaxt in davlatlar.values():
    print(poytaxt)