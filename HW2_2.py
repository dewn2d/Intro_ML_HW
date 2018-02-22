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

def Multi_Gauss(x,u,cov,d):
    S_inv = np.linalg.inv(cov)
    p = 1.0/(math.pow(2*np.pi,d/2)*math.pow(np.linalg.det(cov),.5))
    e =  np.power( math.e, -0.5*np.einsum('...k,kl,...l->...', x-u, S_inv, x-u))
    return e * p

sample1 = np.zeros(shape=[1000,2])
sample2 = np.zeros(shape=[1000,2])

#for part b an c but did not get to
"""
def dec_bound(z,z2,eq):
    if eq == 1:
    else:
"""

#3D Plotting
def plot_3d(cov, u, cov2, u2, d):
    N = 1000
    X = np.linspace(-20, 20, N)
    Y = np.linspace(-20, 20, N)
    X, Y = np.meshgrid(X, Y)

    pos = np.empty(X.shape + (d,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y

    z = Multi_Gauss(pos, u, cov, d)
    #print (z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax = fig.gca(projection='3d')

    ax.plot_surface(X, Y, z,cmap='viridis',linewidth=0)
    
    z2 =  Multi_Gauss(pos, u2, cov2, d)
    ax.plot_surface(X, Y, z2,cmap='viridis',linewidth=0)

    plt.show()

plot_3d(E, u[0], E, u[1], 2)

Ed = np.array([[4.1,0.4],[0.4,2.8]])
    
plot_3d(Ed, u[0], Ed, u[1], 2)

Ee= np.array([[[2.1,1.5],[1.5,3.8]] ,[[4.1,0.4],[0.4,2.8]]])
    
plot_3d(Ee[0], u[0], Ee[1], u[1], 2)
