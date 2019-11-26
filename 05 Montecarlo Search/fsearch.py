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

	try:
		ib = np.min(y) if type == "min" else np.max(y)
		ib = int(ib)
	except :
		ib = np.min(y)[0] if type == "min" else np.max(y)[0]
		ib = int(ib)
		
	return {"index":ib, "sol":sol[ib], "eval":np.min(x) if type == "min" else np.max(x)}

