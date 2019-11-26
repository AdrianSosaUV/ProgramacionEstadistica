# !/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
from biseccion import *
import math

def f(x):
	"""Funcion a evaluar x^3 +4x^2 -10"""
	#return pow(x,5)+ 4*pow(x,2)-10
	#return pow((x-7),3)+ pow((2*x-5),2)
	#return -math.cos(x) + math.sin(x)
	return math.sin(x+5) + pow((x-2),2) - 1.5 *x
	#return 1/x
	#return math.sin(x) + 2*x - 1

if __name__ == '__main__':

	a = -5
	b = 5
	x = np.arange(a,b, 0.01)
	y = [f(k) for k in x]

	try:
		raiz = biseccion(f, a, b)
		print(raiz)
		plt.annotate('Raiz', xy=(raiz, 0), xytext=(raiz,0.5),
		           arrowprops=dict(facecolor='red'))
		plt.plot(x,y)
		plt.grid()
		plt.show()
	except ValueError as e:
		print(e)



plt.figure()
plt.title("Newton")
plt.subplot(331)
plt.plot(x1,y1)
plt.annotate('Raiz', xy=(raiz1, 0), xytext=(raiz1,0.5),
		           arrowprops=dict(facecolor='red'))
plt.title("-x^5 + x^4 + x \n {}".format(raiz1))
plt.grid(True)

plt.subplot(332)
plt.plot(x2,y2)
plt.annotate('Raiz', xy=(raiz2, 0), xytext=(raiz2,0.5),
		           arrowprops=dict(facecolor='red'))
plt.title("x^3 + x^3 - 10 \n {}".format(raiz2))
plt.grid(True)

plt.subplot(333)
plt.plot(x3,y3)
plt.annotate('Raiz', xy=(raiz3, 0), xytext=(raiz3,0.5),
		           arrowprops=dict(facecolor='red'))
plt.title("-x^2 + 10x - 2 \n {}".format(raiz3))
plt.grid(True)

plt.subplot(334)
plt.plot(x4,y4)
plt.annotate('Raiz', xy=(raiz4, 0), xytext=(raiz4,0.5),
		           arrowprops=dict(facecolor='red'))
plt.title("x^4 + 4x^2 -10 \n {}".format(raiz4))
plt.grid(True)

plt.subplot(335)
plt.plot(x5,y5)
plt.annotate('Raiz', xy=(raiz5, 0), xytext=(raiz5,0.5),
		           arrowprops=dict(facecolor='red'))
plt.title("sin(x+5) + (x-2)^2 - 1.5x \n {}".format(raiz5))
plt.grid(True)

plt.subplot(336)
plt.plot(x6,y6)
plt.annotate('Raiz', xy=(raiz6, 0), xytext=(raiz6,0.5),
		           arrowprops=dict(facecolor='red'))
plt.title("-sin(x) + 2x \n {}".format(raiz6))
plt.grid(True)


plt.subplot(337)
plt.plot(x7,y7)
plt.annotate('Raiz', xy=(raiz7, 0), xytext=(raiz7,0.5),
		           arrowprops=dict(facecolor='red'))
plt.title("-cos(x) + sin(x) \n {}".format(raiz7))
plt.grid(True)


plt.subplot(338)
plt.plot(x8,y8)
plt.annotate('Raiz', xy=(raiz8, 0), xytext=(raiz8,0.5),
		           arrowprops=dict(facecolor='red'))
plt.title("(x-7)^3 + (2x-5)^2 \n {}".format(raiz8))
plt.grid(True)
