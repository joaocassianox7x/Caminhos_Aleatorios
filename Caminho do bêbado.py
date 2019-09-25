#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:48:41 2019

@author: joao
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import numpy.random as R

matplotlib.rcParams.update({'font.size': 12})


N=100 #Número de Bêbados
M=1000 #Número de Passos
X=R.uniform(low=-0.0, high=+1.0, size=(N,M))
Y=R.uniform(low=-1.0, high=+1.0, size=(N,M))

plt.figure(111)
plt.xlabel('X Final')
plt.ylabel('Y Final')


for i in range(N):
    Xn,Yn=[],[]
    xn,yn=0,0
    for j in range(M):
        x,y= X[i][j], Y[i][j]
        Xn=np.cumsum(X[i][:])
        Yn=np.cumsum(Y[i][:])
    plt.plot(Xn,Yn, ls='-')
plt.savefig('andar.pdf')
    
plt.figure(112)
Xf=np.sum(X,0)/M
Yf=np.sum(Y,0)/M
plt.ylabel('Y')
plt.xlabel('X')
plt.hist2d(Xf,Yf,bins=np.sqrt(N))
plt.savefig('andar_hist_2d.pdf')
plt.tight_layout()
plt.show()