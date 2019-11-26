# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from dfseach import *


def espacio(m, n, r1, r2):
	dat = np.zeros((m,n))
	for i in range(m):
		for j in range(n):
			dat[i][j] = np.random.randint(r1, r2)
	return dat


a = 0	#limite inferior
b = 9	#limite superior
c = 3	#numero de variables
d = 5	#tamaño del espacio
def f1(x):
    return 3*pow(x,2) + 2*x

metodo= dfsearch(espacio(c,d,a,b),f1, type="min")


print("x: ",metodo)
print("y: ",f1(metodo))

metodo= dfsearch(espacio(c,d,a,b),f1, type="max")


print("x: ",metodo)
print("y: ",f1(metodo))
