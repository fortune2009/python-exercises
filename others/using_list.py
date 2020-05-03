# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:35:51 2020

@author: F.David
"""
import pylab

list_of_ints =[]
for count in range(15):
    list_of_ints.append(count*2)
    
print(list_of_ints)
print(len(list_of_ints))    

pylab.plot(list_of_ints)
pylab.show()
