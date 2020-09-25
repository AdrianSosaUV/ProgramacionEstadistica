# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from Montecarlo import *


def Fx(x):
	return math.exp(-1*x)/ (1 + pow(x-1,2))


Mc = MonteCarlo(Fx, 0, 5, 20000)

print("Aproximación Monte Carlo de F(x): {:2f}".format(Mc["estimation"]))
print("Varianza de la aproximación: {:2f}".format(Mc["variance"]))
print("Error en la aproximación: {:2f}".format(Mc["error"]))

















#### importancia del muestreo 
### determinar el peso optimo de la función
##
### graficar la función
##xs = [float(i/50) for i in range(int(50*math.pi*2))]
##ys = [Fx(x) for x in xs]
##plt.plot(xs,ys)
##plt.title("f(x)")
##plt.show()