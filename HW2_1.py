# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:50:34 2018

@author: Dwayne
"""
import numpy as np
import pandas as pd

B = np.array(["x1","x2","x3"])

data1 = np.array([[-5.01,-8.12,-3.68],[-5.43,-3.48,-3.54],[1.08,-5.52,1.66],
     [0.86,-3.78,-4.11],[-2.67,0.63,7.39],[4.94,3.29,2.08],
     [-2.51,2.09,-2.59],[-2.25,-2.13,-6.94],[5.56,2.86,-2.26],
     [1.03,-3.33,4.33]])
data2 = np.array([[-0.91,-0.18,-0.05],[1.30,-2.06,3.53],[-7.75,-4.54,-0.95],
     [-5.47,0.50,3.92],[6.14,5.72,-4.85],[3.60,1.26,4.36],
     [5.37,-4.63,-3.65],[7.18,1.46,-6.66],[-7.39,1.17,6.30],
     [-7.50,-6.32,-0.31]])
data3 = np.array([[5.35,2.26,8.13],[5.12,3.22,-2.66],[-1.34,-5.31,-9.87],
     [4.48,3.42,5.19],[7.11,2.39,9.21],[7.17,4.33,-0.98],
     [5.75,3.97,6.65],[0.77,0.27,2.41],[0.90,-0.43,-8.71],
     [3.52,-0.36,6.43]])

class1 = pd.DataFrame(data1, columns = B)
class2 = pd.DataFrame(data2, columns = B)
class3 = pd.DataFrame(data3, columns = B)

"""
ClsSet:
    a class that holds a fetures data and prior probablity
    
    data: the data set
    cov_mat: the covariance matrix of the class
    prior: the prior probablilty
    mn: means of each class featrue
"""
class ClsSet:
    data = None
    cov_mat = None
    mns = None
    prior = 0
    
    def __init__(self, x, y):
        self.data = x
        self.prior = y
        
    def cls_mean(self, clsSet): 
        mns = []
        ct=0
        for col in self.data.columns:
            #print(cls)
            mean = 0
            for i in range(0, len(self.data.index)):
                mean += self.data[col][i]
            mns.append(round(mean/len(self.data.index),4))
            ct+=1     
        
        self.mns = np.array(mns)
    
    """
    get_cov_mat:
        computes the convariance matrix of a class
    """
    def get_cov_mat(self, clsSet):     
        arr_set = self.data.iloc[:,:].values
        r, c = arr_set.shape
        one = np.ones(shape = [r,1])
        dev = arr_set - np.dot(np.dot(one,one.T),arr_set)*(1/r)
        self.cov_mat = np.dot(dev.T,dev)/r


def get_mahala(x, y, cov, d):
    S_inv = np.linalg.inv(cov)
    a = np.dot((x-y).T,S_inv)
    b = np.dot(a, (x-y))
    return b
    
def discrim_funct(x,cov,u,Pw,d):
    
    g = (-1/2)*get_mahala(x,u,cov,d)
    a = (d/2)*np.log(2*np.pi)
    b = (1/2)*np.log(np.linalg.det(cov))
    c = np.log(Pw)

    return g-a-b+c 

"""
def Multi_Gauss(x,cov,u,d):
    x = np.zeros(shape = [d,1])
    for i in range(0, d):
        x[i] = np.random.rand(0,1)

    f = (1/(np.power(2*np.pi,d/2)*np.power(np.absolute(cov,.5))))
    f = f * np.exp(np.negative(.5*(x-u).T*np.linalg.inv(cov)*(x-u)))
    return f
"""
       
sets = [ClsSet(class1, 0.6),ClsSet(class2, 0.2),ClsSet(class3, 0.2)] # list of the classes

for s in range(0,len(sets)): # creating covariance matrix and mean array
    sets[s].get_cov_mat(sets[s])
    sets[s].cls_mean(sets[s])

""" # for verification
set1.data.mean(axis = 0)
set1.data.var(axis = 0)
set1.data.cov()
"""

tp = [np.array([1,3,2]), np.array([4,6,1]), np.array([7,-1,0]), np.array([-2,6,5])] #array of test points

cls = [] #array that holds classifications
for x in range(0,len(tp)):
    cls.append(0)
    for i in range(0,len(sets)):
        if i == 0:
            g0 = gi = discrim_funct(tp[x],sets[i].cov_mat,sets[i].mns,sets[i].prior,2) #init
        else:
            gi = discrim_funct(tp[x],sets[i].cov_mat,sets[i].mns,sets[i].prior,2)
        
        if gi > g0:
            g0 = gi
            cls[x] = i
        
print(cls)
    
    