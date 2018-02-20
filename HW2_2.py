# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 21:40:07 2018

@author: Dwayne
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = [np.array([[8],[2]]),np.array([[2],[8]])]
E = np.array([[4.1,0],[0,2.8]])
Pw1 = .4
Pw = [Pw1,Pw1/4]

def Multi_Gauss(x,cov,u,Pw,d):  
    f = np.dot((x-u).T,np.linalg.inv(cov))
    g = (-1/2)*np.dot(f,(x-u))
    a = (d/2)*np.log(2*np.pi)
    b = (1/2)*np.log(np.linalg.det(cov))
    c = np.log(Pw)

    return g-a-b-c
      
sample = np.zeros(shape = [1000,2])

for i in range(0,1000):
    x = np.random.rand(2,1)
    for j in range(0,2):
        sample[i,j] = Multi_Gauss(x,E,u[j],Pw[j],2)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
x, y = np.meshgrid(sample[:,0],sample[:,1])
z = np.sin(x+y)

ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

plt.show()
