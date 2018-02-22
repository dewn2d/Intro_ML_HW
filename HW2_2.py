# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 21:40:07 2018

@author: Dwayne
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

u = [np.array([8,2]),np.array([2,8])]
E = np.array([[4.1,0],[0,2.8]])
Pw1 = .4
Pw = [Pw1,Pw1/4]

def discrim_funct(x,cov,u,Pw,d):
    
    g = (-1/2)*get_mahala(x,u,cov,d)
    a = (d/2)*np.log(2*np.pi)
    b = (1/2)*np.log(np.linalg.det(cov))
    c = np.log(Pw)

    return g-a-b+c 

def get_mahala(x, y, cov, d):
    S_inv = np.linalg.inv(cov)
    a = np.dot((x - y) ,S_inv) * (x - y)
    return a

def Multi_Gauss(x,u,cov,d):
    p = 1.0/(math.pow(2*np.pi,d/2)*math.pow(np.linalg.det(cov),.5))
    e =  np.power( math.e, -0.5*get_mahala(x,u,cov,d))
    return e * p

sample1 = np.zeros(shape=[1000,2])
sample2 = np.zeros(shape=[1000,2])

#sample = np.random.multivariate_normal(u[0],E,1000) #for testing

for i in range(0,1000):
    x = np.random.rand(1,2)*10
    sample1[i] = Multi_Gauss(x,u[0],E,2)*100
    sample2[i] = Multi_Gauss(x,u[1],E,2)*100
    

#3D Plotting
x, y = np.meshgrid(sample1[:,0],sample1[:,1])

pos = np.empty(x.shape + (2,))
pos[:, :, 0] = x; pos[:, :, 1] = y


z = multivariate_normal( mean=u[0], cov=E)


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax = fig.gca(projection='3d')

ax.plot_surface(x, y, z.pdf(pos),cmap='viridis',linewidth=0)

plt.show()

