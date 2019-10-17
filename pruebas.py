#!/usr/bin/env python3
import pygame
import numpy as np

from pygame import *
from mate_funcs import *

vector1 = [100,100]
vector2 = deg_to_Rect([141.4213,np.pi/4])

# print (sumVec(vector1, vector2))
# print (scalVec(vector1, 2))
#
# print (dot(10, 20, 2))
#
#
# print (dot2(vector1, vector2))

print (vector1)
print (vector2)

print (rotRadTas2(vector1,np.pi*.25, [0,0]))
