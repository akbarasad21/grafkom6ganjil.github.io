import numpy as np
import matplotlib.pyplot as plt

x1 = int(input('Masukan x1  : '))
y1 = int(input('Masukan y1  : '))
x2 = int(input('Masukan x2  : '))
y2 = int(input('Masukan y2  : '))


nilaiY = y2 - y1
nilaiX = x2 - x1
N = x2 - x1 + 1

x = x1
y = y1

i = 1


if x1 == x2:
    titikA = []
    titikB = []
    for i in range (1,y2,1):
        plt.plot(titikA,titikB)
        plt.show()
        
        
 elif y1 == y2:
    titikA = []
    titikB = []
    for i in range (1,y2,1):
        plt.plot(titikA,titikB)
        plt.show()
        
 else:
    titikA = []
    titikB = []
    for i in range (0,N,1):
        m = nilaiY / nilaiX
        rumusY = m * (x - x1) + y1
        kordinatY = round(rumusY)
        x+=1
        print('Garis yang di lewati yaitu', x-1,',', kordinatY)
        titikA.append(x-1)
        titikB.append(kordinatY)
