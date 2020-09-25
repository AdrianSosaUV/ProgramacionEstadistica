# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np 

def fsearch(sol, Fx, type="min"):
	"""Método de busqueda ciega
	Halla la solucion de la función Fx en el espacio de busqueda.
	Argumentos
	----------
	Fx - Función
	sol - Espacio de busqueda, Matrix(MxN)
	type (opcional) - Tipo de optimización

	Devuelve
	--------
	x - Solucion de la funcion Fx en el espacio de busqueda
	"""
	if (not type == "min" and not type == "max"):
		raise ValueError("Metodo de optimización no valido")

	x = pd.DataFrame((sol))
	y = x.apply(Fx,1)

	ib = y.min() if type == "min" else y.max()
	ic = sorted(ib) if type == "min" else sorted(ib, reverse=True)

	cont = 0
	for i in ib:
		if not i == ic[0]:
			cont += 1
		else:
			break

	row = y[cont].idxmin() if type == "min" else y[cont].idxmax()
	return {"index":(cont, row), "sol":x[cont][row], "eval":y[cont][row]}

