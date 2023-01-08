# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


Matrix=[[0,	0,	0,	0,	0],
       	[0,	0,	0,	1,	0],
       	[0,	0,	1,	0,	0],
       	[0,	0,	1,	1,	1],
       	[0,	1,	0,	0,	0],
       	[0,	1,	0,	1,	1],
       	[0,	1,	1,	0,	1],
       	[0,	1,	1,	1,	0],
       	[1,	0,	0,	0,	0],
       	[1,	0,	0,	1,	1],
       	[1,	0,	1,	0,	1],
       	[1,	0,	1,	1,	0],
       	[1,	1,	0,	0,	1],
       	[1,	1,	0,	1,	0],
       	[1,	1,	1,	0,	0],
       	[1,	1,	1,	1,	0]]

for Vector in Matrix:
    A=bool(Vector[0])
    B=bool(Vector[1])
    C=bool(Vector[2])
    D=bool(Vector[3])
    F=(((not A) and (not B) and C and D) or 
      ((not A) and B and (not C) and D) or 
      ((not A) and B and C and (not D)) or 
      (A and (not B) and (not C) and D) or 
      (A and (not B) and C and (not D)) or 
      (A and B and (not C) and (not D)))
    print(Vector[0],Vector[1],Vector[2],Vector[3],"|",int(F))
    