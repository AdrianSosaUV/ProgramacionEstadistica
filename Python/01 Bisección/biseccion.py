# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def biseccion(Fx, a, b, method = "tolerance", tol=1.0e-6):
	"""Método de bisección
	Halla una raíz de la función f en el intervalo [a, b] mediante el método
	de bisección.

	Argumentos
	----------
	Fx - Función, debe ser tal que f(a) f(b) < 0
	a - Extremo inferior del intervalo
	b - Extremo superior del intervalo
	tol (opcional) - Cota para el error absoluto de la x
	method - forma de paro "tomerance" o "zero"

	Devuelve
	--------
	x - Raíz de Fx en [a, b]
	"""
	#if a > b:
	#	raise ValueError("Error de segmento")

	x = (a + b)/2
	var = True
	while var:
		if method == "tolerance":
			if b - a < tol:
				return x
				var = False
				# Utilizamos la función signo para evitar errores de precisión
			elif np.sign(Fx(a)) * np.sign(Fx(x)) > 0:
				a = x
			else:
				b = x
			x = (a + b) / 2.0
		elif method == "zero":
			if x == 0:
				return x
				var = False
			else:
				if np.sign(Fx(a)) * np.sign(Fx(x)) > 0:
					a = x
				else:
					b = x
				x = (a + b) / 2.0
		else:
			raise ValueError("Error de metodo")

