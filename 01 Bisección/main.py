# /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
from biseccion import *
import math

def f(x):
	return math.sin(x+5) + pow((x-2),2) - 1.5 *x

if __name__ == '__main__':

	a = -5
	b = 5
	x = np.arange(a,b, 0.01)
	y = [f(k) for k in x]

	try:
		raiz = biseccion(f, a, b)
		print("La raiz es:",raiz)
		plt.title("sin(x+5) + (x-2)^2 -1.5x \n {}".format(raiz))
		plt.annotate('Raiz', xy=(raiz, 0), xytext=(raiz,0.5),
		           arrowprops=dict(facecolor='red'))
		plt.plot(x,y)
		plt.grid()
		plt.show()
	except ValueError as e:
		print(e)


