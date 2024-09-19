# -*- coding: utf-8 -*-


#kinolar = {'ali':['terminator','batman','yulduzlar jangi'],
 #          'vali':['imperiya','quyosh','saroy'],
  #         'anton':['rus qoshini','parovoz','xarbiy oila']}
#
#for isim,kino in kinolar.items():
 #   print(f"{isim}ning sevimli kinolari : ", end='')
  #  for element in kino:
   #     print(f"{element} ",end='')
    #print("")
    

davlatlar = {'uzbekistan':{'poytaxti':'toshkent','aholisi':'31 mln','pul birligi':'som'},
             'qozogiston':{'poytaxti':'astana','aholisi':'35 mln','pul birligi':'tenge'},
             'turkmaniston':{'poytaxti':'ashgabat','aholisi':'12 mln','pul birligi':'dinor'},
             'Qatar':{'poytaxti':'doha','aholisi':'5 mln','pul birligi':'dinor'}}

davlat = input("Davlat nomini kiriting : ")


for nomi,element in davlatlar.items():
    if davlat == nomi:    
        print(f"{nomi.title()} davlati xaqida batafsil malumot : ")
        print(f"poytaxti : {element['poytaxti']}")
        print(f"aholisi : {element['aholisi']}")
        print(f"pul birligi : {element['pul birligi']}")
        print("--------------------------------------") 
        
    
        
        
    
    