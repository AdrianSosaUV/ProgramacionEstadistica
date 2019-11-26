# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np
from newton import *


def f(x):
	"""Funcion a evaluar (x-7)^3 +(2x-5)^2"""
	return pow((x-7),3)+ pow((2*x-5),2)

def df(x):
	'''Derivada de la funcion 3(x-7)^2 +(4x-10) '''
	return pow((3*x-21),2)+ (4*x-10)


if __name__ == '__main__':

	a = -0
	b = 10
	x = np.arange(a,b, 0.01)
	y = [f(k) for k in x]
	raiz =  newton(f, df, b)
	print("La raiz es:",raiz)
	plt.title("(x-7)^3 +(2x-5)^2 \n {}".format(raiz))
	plt.annotate('Raiz', xy=(raiz, 0), xytext=(raiz,0.5),
	           arrowprops=dict(facecolor='red'))
	plt.plot(x,y)
	plt.grid()
	plt.show()

