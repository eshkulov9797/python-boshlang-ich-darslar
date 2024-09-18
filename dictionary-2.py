# -*- coding: utf-8 -*-
mahsulot = {'olma':10000,'behi':15000,'sabzi':3000,'guruch':14000,'olcha':5000}


royxat = ['sabzi','guruch','olcha']

for narsa in mahsulot:
    if narsa in royxat:
        print(f"{narsa.title()} {mahsulot[narsa]}")
        