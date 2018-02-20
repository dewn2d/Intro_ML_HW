# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 22:08:43 2018

@author: Dwayne
"""

import pandas as pd
import numpy as np

"""
 preprocessing:
     txt files with data have different number of spaces for negetive numbers 
     so a space needs to be added so they are able to be parsed conrrectly
"""
def add_spc(filen):
    filename = filen + ".txt"
    cpyname = filen + "_cpy" + ".txt"
    file = open(filename, "r", errors = "replace")
    data = []
    spc = 0
    
    for line in file:
        for l in range( 0 , len(line)):
            if line[l] != " " and spc == 2:
                data.append(" ")
                spc = 0
            elif line[l] == " " :
                spc += 1
            if spc == 3:
                spc = 0
            
            data.append(line[l])

    file1 = open(cpyname, "w")   
    for l in range( 0, len(data)):
        file1.write(data[l])
        
    file.close()
    file1.close()

def get_class(filename):
    cls = pd.read_csv(filename, sep=" ", header=None)
    cls = cls.dropna(axis=1, how='all')
    cls = cls.transpose()
    cls.columns = ["feature1","feature2"]
    cls = cls.reset_index(drop=True)
    return cls     
        
add_spc("class1")
add_spc("class2")
add_spc("class3")
add_spc("class4")

class1 = get_class('class1_cpy.txt')
class2 = get_class('class2_cpy.txt')
class3 = get_class('class3_cpy.txt')
class4 = get_class('class4_cpy.txt')

class1.mean(axis=0)
class1.cov()

def cls_mean(cls, col):
    mean = 0
    for i in range(0, len(cls.index)):
        mean += cls[col][i]
    return mean/len(cls.index)
    
def feature_var(cls,col,mean):
    var = 0
    for i in range(0, len(cls.index)):
        var+=np.square((cls[col][i] - mean))
        #print(cls[col][i] - mean )
    return (1/len(cls.index - 1)) * var

def cls_cov( cls, mean1, mean2 ):
    cov = 0
    for i in range(0, len(cls.index)):
        cov += ( cls["feature1"][i] - mean1 ) * ( cls["feature2"][i] - mean2 )
    return (1/len(cls.index - 1)) * cov

"""
get_cov_mat:
    uses above function and returns the convariance matrix
"""
def get_cov_mat(cls):
    ct = 0
    for col in cls.columns:
        #print(cls)
        if ct == 0:
            mn = cls_mean( cls,col) 
            var1 = feature_var( cls, col, mn)
            ct+=1
        
        elif ct == 1:
            mn1 = cls_mean( cls,col)
            var2 = feature_var( cls, col, mn1)
               
    print(mn)
    print(mn1)        
    cov = cls_cov(cls, mn, mn1)
    print(cov)
    return np.array(([var1, cov],[cov, var2])) 

class2.mean() 
    
cov_mat1 = get_cov_mat(class1)
cov_mat2 = get_cov_mat(class2)
cov_mat3 = get_cov_mat(class3)
cov_mat4 = get_cov_mat(class4)

class1.cov()
class2.cov()
class3.cov()
class4.cov()
