# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 18:46:12 2018

@author: Dwayne
"""

import numpy as np

    
    
pa = np.array( [0.25,0.25,0.25,0.25])
pb = np.array( [0.6,0.4])
pxab = np.array( [[[0.5,0.6,0.4,0.2],[0.7,0.8,0.1,0.3]],
                [[0.5,0.4,0.6,0.8],[0.3,0.2,0.9,0.7]]])
pcx = np.array( [[0.6,0.2,0.1],[0.2,0.3,0.5]])
pdx = np.array( [[0.3,0.7],[0.6,0.4]])
    
def scaninput(**kwargs):
    
    giv = 0
    prev = None
    send = None
    a = ['winter','spring','summer','fall']
    b = ['north','south']
    x = ['salmon','bass']
    c = ['light','medium','dark']
    d = ['wide','thin']
    good = ["a1","a2","a3","a4",
            "b1","b2",
            "x1","x2",
            "c1","c2","c3","c4",
            "d1","d2"]

    args = {}
    
    for key in kwargs:
        if kwargs[key] not in good:
            if key == "a":
                args["a"] = ( "a" + str(a.index(kwargs[key])+1))
            elif key == "b":
                args["b"] = ( "b" + str(b.index(kwargs[key])+1))
            elif key == "x":
                args["x"] = ( "x" + str(x.index(kwargs[key])+1))
            elif key == "c":
                args["c"] = ( "c" + str(c.index(kwargs[key])+1))
            elif key == "d":
                args["d"] = ( "d" + str(d.index(kwargs[key])+1))
            elif key == "giv":
                if kwargs[key] == "|":
                    giv += 1
                    send = prev
                args["giv"] = kwargs[key] 
        else:
            if key == "a":
                args["a"] = kwargs[key]
            elif key == "b":
                args["b"] = kwargs[key]
            elif key == "x":
                args["x"] = kwargs[key] 
            elif key == "c":
                args["c"] = kwargs[key]
            elif key == "d":
                args["d"] = kwargs[key]
        prev = key

             
    return (send,giv, args)

def pabxcd_cond_abxcd(**kwargs):    
    recv, giv, kwargs = scaninput(**kwargs)
    if giv != 0:
        del kwargs['giv']
    global pa, pb, pxab, pcx, pdx
    fill ={"a":None,"b":None,"x":None,"c":None,"d":None}
    fill.update(kwargs)
    #print(fill)
    args = tuple(fill.values())
    fill[recv] = None
    args2 = tuple(fill.values())  
    
    if giv == 0:
        return pabxcd(*args)
    else:
        return (pabxcd(*args)/pabxcd(*args2))

def pabxcd(a,b,x,c,d):
    
    ans =1
    
    if a != None:
        ans *= pa[int(a[1])-1]
    elif a == None and x != None and b != None:    
        sum1 = 0
        for i in range(0,len(pa)):
             sum1 += pa[i] * pxab[int(x[1])-1,int(b[1])-1,i]
        ans *= sum1
        
        
    if b != None:    
        ans *= pb[int(b[1])-1]
    elif b == None and x != None and a != None:    
        sum1 = 0
        for i in range(0,len(pb)):
             sum1 += pb[int(a[1])-1] * pxab[int(x[1])-1,i,int(a[1])-1]
        ans *= sum1
       
        
    if a == None and b == None and x != None:
        sum1 = 0
        for i in range(0, len(pa)-1):
            for j in range(0, len(pb)-1):
                sum1 += pa[i] * pb[j] * pxab[int(x[1])-1,i,j]
        ans *= sum1
         
        
    if x != None and a != None and b != None:
        ans *= pxab[int(x[1])-1,int(b[1])-1,int(a[1])-1]
        
        
    if c != None and x != None:
        ans*=pcx[int(x[1])-1,int(c[1])-1]
    elif x == None and c != None:
        ans *= sum(pcx[:,int(c[1])-1])
        
        
    if d != None and x != None:   
        ans *= pdx[int(x[1])-1,int(d[1])-1]
    elif d != None and x == None:
        ans *= sum(pdx[:,int(d[1])-1])
    elif x == None and d == None:
        ans *= sum(pdx[:,int(d[1])-1])
        
    print("")
    return ans
    
    
print(pabxcd_cond_abxcd(x="x2",giv='|',c="c1",b="b2"))


    
print(pabxcd_cond_abxcd(x="salmon",giv='|',a="winter",c="light",b="south",d = "thin"))
print(pabxcd_cond_abxcd(a="winter",giv='|',c="dark",b="south",d = "thin"))
print(pabxcd_cond_abxcd(b="north",giv='|',a="summer",d="wide",c = "dark"))
