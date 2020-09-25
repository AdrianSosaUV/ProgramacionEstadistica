# !/usr/bin/env python
# -*- coding: utf-8 -*-
 
import math 
from annealing import * 

D= [2,15,30]
x = 3

def f1(x):
    return -pow(x,5)+ pow(x,4) + x

a = -2
b = 4
print("F1 min")
for i in D:
	S = annealing(x,f1,[a]*i, [b]*i)
	print("D: {} S: {} f: {}".format(i, S["sol"], S["eval"]))
	print(f1(S["sol"])== S["eval"])

print("\nF1 max")
for i in D:
	S = annealing(x,f1,[a]*i, [b]*i,type="max")
	print("D: {} S: {} f: {}".format(i, S["sol"], S["eval"]))
	print(f1(S["sol"])== S["eval"])
