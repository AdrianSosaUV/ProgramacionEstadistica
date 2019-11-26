# !/usr/bin/env python
# -*- coding: utf-8 -*-

from tabu import * 


N = 1000		# numero de puntos aleatorios en el vecindario
D = [2,15] 		# numero de variables
x = 3

a = -2
b = 4

def f1(x):
    return -pow(x,5)+ pow(x,4) + x

print("\nF1 min")
for i in range(len(D)):
	S = tabu(x, f1, [a]*D[i], [b]*D[i], 10)
	print("D: {} S: {} f: {}".format(D[i], S["sol"], S["eval"]))
	print(f1(S["sol"])== S["eval"])

print("\nF1 max")
for i in range(len(D)):
	S = tabu(x, f1, [a]*D[i], [b]*D[i], 10, type="max")
	print("D: {} S: {} f: {}".format(D[i], S["sol"], S["eval"]))
	print(f1(S["sol"])== S["eval"])

