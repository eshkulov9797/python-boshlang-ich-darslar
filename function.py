# -*- coding: utf-8 -*-
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting:")
        baholar[ism] = baho
    return baholar

talabalar = ['ali','vali','sobir','axadjon']
hammasi = {}

hammasi = bahola(talabalar)
print(hammasi)


