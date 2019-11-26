# !/usr/bin/env python
# -*- coding: utf-8 -*-
 
from hclimbing import * 


N = 1000		#numero de puntos aleatorios en el vecindario
D= [2,15] 		# numero de variables
x = 3			# valor inicial



# funcion a evaluar 
def f1(x):
    return -pow(x,5)+ pow(x,4) + x




a = -2		# limite inferior
b = 4		# limite superior



print("\nF1 min")
for i in range(len(D)):
	S = HillClimbing(x, f1, [a]*D[i], [b]*D[i])
	print("D: {} S: {} f: {}".format(D[i], S["sol"], S["eval"]))
	print(f1(S["sol"])== S["eval"])

print("\nF1 max")
for i in range(len(D)):
	S = HillClimbing(x, f1, [a]*D[i], [b]*D[i],type="max")
	print("D: {} S: {} f: {}".format(D[i], S["sol"], S["eval"]))
	print(f1(S["sol"])== S["eval"])


