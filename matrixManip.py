# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 15:33:27 2014

@author: david
"""
M = 10
zeros = [[i for i in xrange(M)] for j in xrange(M)]

def changeElTo(el):
    for r in range(len(zeros)):
        for c in range(len(zeros[0])):
            if zeros[r][c]%3==0:
                zeros[r][c] = el
    print ""
                
print zeros
changeElTo("#")
print zeros