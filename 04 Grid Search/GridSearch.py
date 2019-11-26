# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
import math
from dfsearch import *

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

