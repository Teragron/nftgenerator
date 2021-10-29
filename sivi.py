# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:33:47 2021

@author: ahmet
"""

from PIL import Image
import numpy as np
from os import listdir
from os.path import isfile, join
import glob
import itertools


arkas = "subs/arkaplan"
vucuts = "subs/vucut"
kafas = "subs/kafa"
agizs= "subs/agiz"



arkalar = []
vucutlar = []
kafalar = []
agizlar = []
total = []



arka = [i for i in listdir(arkas) if isfile(join(arkas, i))]
vucut = [j for j in listdir(vucuts) if isfile(join(vucuts, j))]
kafa = [k for k in listdir(kafas) if isfile(join(kafas, k))]
agiz = [ag for ag in listdir(agizs) if isfile(join(agizs, ag))]


for l in arka:
    arkalar.append(Image.open("subs/arkaplan/{}".format(l)))

for m in vucut:
    vucutlar.append(Image.open("subs/vucut/{}".format(m)))
    
for n in kafa:
    kafalar.append(Image.open("subs/kafa/{}".format(n)))
for o in agiz:
    agizlar.append(Image.open("subs/agiz/{}".format(o)))


total.append(arkalar)
total.append(vucutlar)
total.append(kafalar)
total.append(agizlar)

iterasyon = list(itertools.product(*total))

for idx, sayi1 in enumerate(iterasyon):
    sayi1[0].paste(sayi1[1], (0,0), sayi1[1])
    sayi1[0].paste(sayi1[2], (0,0), sayi1[2])
    sayi1[0].paste(sayi1[3], (1,1), sayi1[3])
    sayi1[0].save("generated/{}.png".format(idx+1),"PNG")

# gorsel = "1.png"
# yuz = "a1.png"
# x = Image.open(gorsel)
# z = Image.open(yuz)
# x.paste(z, (0,0), z)
# x.save("deneme.png", "png")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# alt = [o for o in listdir(alt) if isfile(join(alt, o))]

# for p in alt:
#     altlar.append(Image.open("altlar/{}".format(p)))
    

# iterasyon2 = list(itertools.product(altlar, kafalar))

# for idx2, sayi2 in enumerate(altlar):
#     for idx3, sayi3 in enumerate(kafalar):
#         sayi2.paste(sayi3, (0,0), sayi3)
#         sayi2.save("generated/{}.png".format(idx2*idx3+1),"PNG")
        
#         #sayi2.show()
    



#iterasyon2 = list(itertools.product(*t2))
    





