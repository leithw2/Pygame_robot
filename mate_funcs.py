#!/usr/bin/env python
import numpy as np

def deg_to_Rect(vec):

    res = [vec[0]*np.cos(vec[1]), vec[0] * np.sin(vec[1])]

    return res

def rect_to_deg(vec):

    res = [magVec(vec),angVec(vec)]

    return res

def rotDeg(vec, deg):

    resx =  vec[0]*np.cos(deg) + vec[1]*np.sin(deg)
    resy = -vec[0]*np.sin(deg) + vec[1]*np.cos(deg)

    return [resx,resy]

def rotRad(vec, rad):

    resx =  vec[0]*np.cos(rad) - vec[1]*np.sin(rad)
    resy =  vec[0]*np.sin(rad) + vec[1]*np.cos(rad)

    return [resx,resy]

def rotRadTas(vec, rad, tras):

    resx =  vec[0]*np.cos(rad) + vec[1]*np.sin(rad) + tras[0]
    resy =  -vec[0]*np.sin(rad) + vec[1]*np.cos(rad) + tras[1]

    return [resx, resy]

def rotRadTas2(vec, rad, tras):

    resx =  vec[0]*np.cos(rad) - vec[1]*np.sin(rad) + tras[0]
    resy =  vec[0]*np.sin(rad) + vec[1]*np.cos(rad) + tras[1]

    return [resx, resy]

def magVec(vec):
    return np.sqrt(vec[0]**2 + vec[1]**2)

def angVec(vec):
    return np.arctan2(vec[1],vec[0])

def dot(mag1, mag2, ang):
    return mag1 * mag2 * np.cos(ang)

def dot2(vec1, vec2):
    return [vec1[0] * vec2[0] + vec1[1] * vec2[1]]

def angBetVec(vec1, vec2):

    top  = dot(vec1,vec2)
    down = magVec(vec1) * magVec(vec2)

    return np.acos( top/down )

def cros():
    return magVec(vec1) * magVec(vec2) * np.cos(ang)

def sumVec(vec1, vec2):
    return [vec1[0] + vec2[0], vec1[1] + vec2[1]]

def scalVec(vec, scal):
    return [vec[0] * scal, vec[1] * scal]

''' -----------------------3D----------------------'''

def RotX(mat, ang):

    Hs =  np.matrix([[1              ,0              ,0              ,0],
                    [0              ,(np.cos(ang)) ,(-np.sin(ang)),0],
                    [0              ,(np.sin(ang)) ,(np.cos(ang)) ,0],
                    [0              ,0              ,0              ,1]])
    return mat.dot(H)

def RotY(mat, ang):

    Hs =  np.matrix([[(np.cos(ang)) ,0              ,(np.sin(ang)) ,0],
                    [0              ,1              ,0              ,0],
                    [(-np.sin(ang)),0              ,(np.cos(ang)) ,0],
                    [0              ,0              ,0              ,1]])
    return mat.dot(H)

def Rotz(mat, ang):

    Hs =  np.matrix([[(np.cos(ang)) ,(-np.sin(ang)),0                ,0],
                     [(np.sin(ang)) ,( np.cos(ang)),0                ,0],
                     [0              ,0            ,1                ,0],
                     [0              ,0            ,0                ,1]])



    return np.transpose(Hs.dot(np.transpose(mat)))

def MatRotZ(ang):

    H =  np.matrix([[(np.cos(ang)) ,(np.sin(ang)),0                ,0],
                    [(-np.sin(ang)) ,( np.cos(ang)),0                ,0],
                    [0              ,0            ,1                ,0],
                    [0              ,0            ,0                ,1]])
    return H

def MatTra(vec):

    H =  np.matrix([[1,0,0,vec[0]],
                     [0,1,0,vec[1]],
                     [0,0,1,vec[2]],
                     [0,0,0,  1   ]])
    return H



def translation(mat, vec):
    Hs =  np.matrix([[1,0,0,vec.item(0)],
                    [0,1,0,vec.item(1)],
                    [0,0,1,vec.item(2)],
                    [0,0,0,  1   ]])

    res = np.transpose(Hs.dot(np.transpose(mat)))
    #print (res)
    return res

def translation2(mat, ang, vec):

    mat = np.transpose(mat)

    Hs =  np.matrix([[(np.cos(ang)) ,(-np.sin(ang)),0                ,0],
                     [(np.sin(ang)) ,( np.cos(ang)),0                ,0],
                     [0              ,0            ,1                ,0],
                     [0              ,0            ,0                ,1]])

    Hs2 = np.matrix([[1,0,0,vec.item(0)],
                     [0,1,0,vec.item(1)],
                     [0,0,1,vec.item(2)],
                     [0,0,0,       1   ]])

    Hs3 = Hs2.dot(Hs)
    #print(Hs3)
    Hs3 = Hs2

    res = np.transpose(Hs3.dot(mat))
    #print (res)
    return res
