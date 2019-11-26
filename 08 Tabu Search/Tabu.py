# !/usr/bin/env python
# -*- coding: utf-8 -*-

from fsearch import *
from neighborhood import *

def tabuSearch(x, Fx, lower, upper, L, maxit=20, N=10, type="min"):
	"""
	x - solucion inicial
	Fx - funcion a evaluar
	lower - vector con valores minimos
	upper - vector con valores maximos
	L - longitud de la lista tabu
	maxit - numero maximo de iteraciones
	N - numero de vecinos

	"""
	lista = []	# lista tabu
	i = 0 		# contador 

	while i < maxit:
		for j in range (N):
			S1 = fsearch(neighborhood(lower, upper, 100), Fx, type)
			Clist = []
			if S1 not in lista:
				Clist.append(S1["sol"])
		S = {"sol":x, "eval": Fx(x)}
		S1 = fsearch(Clist, Fx, type)

		if (type == "min" and S1["eval"]< S["eval"]) :
			lista.append(S1)
			while len(lista)> L :
				del lista[-1]
			S = S1
		elif(type == "max" and S1["eval"]> S["eval"]) :
			lista.append(S1)
			while len(lista)> L :
				del lista[-1]
			S = S1
		else:
			break
		i += 1
	return S


