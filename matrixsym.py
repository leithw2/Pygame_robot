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
g = sym.Symbol('t1')
h = sym.Symbol('t2')
i = sym.Symbol('t3')

dy = sym.Symbol('dy')
dzfix = sym.Symbol('dzfix')

Ry1 = np.matrix([[ (sym.cos(g)) ,   0  , (sym.sin(g)) , 0  ],
                 [      0    ,   1  ,     0     ,   0],
                 [ (-sym.sin(g)),   0  , (sym.cos(g)) ,   0],
                 [      0    ,   0  ,    0      ,   1]])

T1 = np.matrix([[1,0,0,0],
                [0,1,0,dy],
                [0,0,1,0],
                [0,0,0,1]])

Rz1 = np.matrix([[ (sym.cos(h))   ,    (-sym.sin(h)) ,  0    ,0],
                 [  (-sym.sin(h)) ,   (sym.cos(h))  ,  0    ,0],
                 [0            ,   0           ,  1    ,0],
                 [0            ,   0           ,  0    ,1]])

T2 = np.matrix([[1,0,0,   dzfix*sym.cos(i)],
                [0,1,0,   -dzfix*sym.sin(i)],
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
