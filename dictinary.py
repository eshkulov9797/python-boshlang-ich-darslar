# -*- coding: utf-8 -*-


otam = {'isim':"Timur",'familiya':"Turdibekov",'sharif':'Doniyorov','yil':1997}
#print(f"{otam['familiya'].title()}")
#print(f"{otam['isim'].title()}")
#print(f"{otam['sharif'].title()}")
#print(f"{otam['yil']} yil")

#lugat = {'int':'butun sonlar','double':'xaqiqiy sonlar','str':'satr qatorlari','bool':'shart operatori','import':'yuklamoq'}
#print(lugat['int'])
#print(lugat['double'])
#print(lugat['str'])
#print(lugat['bool'])

sozlar = {'apple':'olma','water':'suv','mother':'ona','father':'ota','brother':'aka','sister':'opa','yellow':'sariq'}

soz = input("so'zni kiriting : ")

tarjima = sozlar.get(soz)
if tarjima == None:
    print("bunday so'z yo'q!!!")
else:
    print(f"{soz.title()} tarjimasi {tarjima.title()}")
    

