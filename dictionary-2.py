# -*- coding: utf-8 -*-
royxat = {'osh':15000,'shashlik':24000,'manti':20000,'shorva':12000}
zakaz = []

for taom in range(3):
    zakaz.append(input("Taomni kiriting:"))

i = 0

for sq in zakaz:
    if sq in royxat:
        print(f"{sq}ning narxi {royxat[sq]}")
        