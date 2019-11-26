# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
from blind import *

def GridSearch(step, lower, upper, Fx, type="min"):
	D=len(step)	#dimension 
	dominio = [None] * D 	#dominio de valores
	#L = [False]* D 	#vector auxiliar
	for i in range(D):
		dominio[i]= np.arange(lower[i], upper[i], step[i])
		#L[i] = len(dominio[i])
	#LS = np.prod(L)
	#s = np.ndarray(shape=(LS, D)) #espacio de busqueda
	#k=0
	#for i in range(D,0,-1):
	#	for j in range(LS):
	#		for k in range(len(dominio[i])):
	#			E = 1 if i==0 else E*L[i-1]
	#			#print(len(dominio[i]))
	#			#print(len(s[i]))
	#			s[j][i] = dominio[i][k]
	#			#k = 0 if (k+1)==len(dominio[i]) else k+1
	#s = np.matrix(s)
	#print(s)
	#print(dominio)
	#print(len(s))
	#return fsearch(Fx, s, type)	# mejor solucion 
	return dfsearch(dominio, Fx, type=type)
var = 5
upper = [1000]*var
lower = [1]*var
step = [100]*var 

def f(x):
	return pow(x,2)

valor= GridSearch(step, lower, upper, f, "max")
print(valor)
