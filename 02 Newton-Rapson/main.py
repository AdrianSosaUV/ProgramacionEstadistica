# !/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np
from newton import *


def f(x):
	"""Funcion a evaluar x^3 +4x^2 -10"""
	return pow((x-7),3)+ pow((2*x-5),2)

def df(x):
	'''Derivada de la funcion, 3x^2 + 8x '''
	return pow((3*x-21),2)+ (4*x-10)


if __name__ == '__main__':

	a = -0
	b = 10
	x = np.arange(a,b, 0.01)
	y = [f(k) for k in x]
	raiz =  newt(f, df, b)
	print(raiz)
	#plt.annotate('Raiz', xy=(raiz, 0), xytext=(raiz,0.5),
	           #arrowprops=dict(facecolor='red'))
	plt.plot(x,y)
	plt.grid()
	plt.show()

