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

g = sym.Symbol('t2')
h = sym.Symbol('h')
i = sym.Symbol('t1')


Ry1 = np.matrix([[(sym.cos(g)) ,   0  ,(sym.sin(g)) , 0  ],
                 [      0    ,   1  ,     0     ,   0],
                 [(-sym.sin(g)),   0  ,(sym.cos(g)) ,   0],
                 [      0    ,   0  ,    0      ,   1]])

T1 = np.matrix([[1,0,0,0],
                [0,1,0,7],
                [0,0,1,0],
                [0,0,0,1]])

Rz1 = np.matrix([[(sym.cos(h))   ,   (-sym.sin(h)) ,  0    ,0],
                 [ (-sym.sin(h)) ,  (sym.cos(h))  ,  0    ,0],
                 [0            ,   0           ,  1    ,0],
                 [0            ,   0           ,  0    ,1]])


Rx1 = np.matrix([[ 1           , 0                   ,  0                     ,0],
                 [ 0           , (sym.cos(i))   ,  (-sym.sin(i))    ,0],
                 [0            , (sym.sin(i))   , (sym.cos(i))      ,0],
                 [0            ,   0                 ,  0                     ,1]])

T2 = np.matrix([[1,0,0,5*cos(np.pi/4)],
                [0,1,0,5*sin(np.pi/4)],
                [0,0,1,             0],
                [0,0,0,             1]])

F1 = Rx1

F2 = F1.dot(Ry1)

print (Rx1)
print (Ry1)


print ("---------")


print (F2)
