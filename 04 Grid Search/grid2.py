# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
import math
from blind import *

def GridSearch(step, lower, upper, Fx, type="min"):
	"""	Metodo estandar de busqueda en malla
	Argumentos
	----------
	step - vector con tamaño de paso para cada dimensión D
	lower - vector con valores más bajos para cada dimensión
	upper - vector con valores más altos para cada dimensión
	Fx - Función a evaluar
	type (opcional) - Tipo de optimización 
	
	Devuelve
	--------
	x - Solucion de la funcion Fx en el espacio de busqueda
	"""
	D=len(step)	#dimension 
	dominio = [None] * D 	#dominio de valores
	for i in range(D):
		dominio[i]= np.arange(lower[i], upper[i], step[i])
	return dfsearch(dominio, Fx, type=type)


var = 5
upper = [1000]*var
lower = [1]*var
step = [50]*var 

def f(x):
	return -pow(x,5)+ pow(x,4) + x

#rastrigin = lambda x: np.array([(math.pow(x[i],2)-(10*math.cos(2*math.pi*x[i]))+10)for i in range(len(x))]).sum()


valor= GridSearch(step, lower, upper, f, "min")
print(valor)

#resultDO EQ f1
#None
#
#resutlado eq f2
#8888