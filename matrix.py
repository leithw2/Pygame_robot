#!/usr/bin/env python3
import pygame
import numpy as np
import sympy as sym
import math
from pylab import *
import matplotlib as plt
from pygame import *
from mate_funcs import *

def RotY(Mat, ang):

    H = [[cos(ang) ,   0  ,sin(ang)],
         [    0    ,   1  ,   0    ],
         [-sin(ang),   0  ,cos(ang)]]
v = np.matrix([[0,0,0],
                [0,0,0],
                [0,0,0]])
g = np.pi/2
h = np.pi/4

Ry1 = np.matrix([[round(sym.cos(g)) ,   0  ,round(sym.sin(g)) , 0  ],
                 [      0    ,   1  ,     0     ,   0],
                 [round(-sym.sin(g)),   0  ,round(sym.cos(g)) ,   0],
                 [      0    ,   0  ,    0      ,   1]])

T1 = np.matrix([[1,0,0,0],
                [0,1,0,7],
                [0,0,1,0],
                [0,0,0,1]])

Rz1 = np.matrix([[round(sym.cos(h))   ,   round(-sym.sin(h)) ,  0    ,0],
                 [ round(-sym.sin(h)) ,  round(sym.cos(h))  ,  0    ,0],
                 [0            ,   0           ,  1    ,0],
                 [0            ,   0           ,  0    ,1]])

T2 = np.matrix([[1,0,0,   5*cos(np.pi/4)],
                [0,1,0,   -5*sin(np.pi/4)],
                [0,0,1,             0],
                [0,0,0,             1]])

F1 = Ry1

F2 = F1.dot(T1)

F3 = F2.dot(Rz1)

F4 = F3.dot(T2)

print (Ry1)
print (T1)
print (Rz1)
print (T2)

print ("---------")


print (F1)
print (F2)
print (F3)
print (F4)
