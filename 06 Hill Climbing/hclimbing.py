# !/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np 
from fsearch import *


def HillClimbing(x, Fx, lower, upper, N=1000, type="min"):

	if (not type == "min" and not type == "max"):
		raise ValueError("Metodo de optimización no valido")

	D=len(lower)	#definir el numero de variables
	sol = np.zeros((N,D))
	for i in range(N):
		for j in range(D):
			sol[i][j] = np.random.uniform(lower[j],upper[j])

	best = fsearch(sol, Fx, type) 
	best1 = Fx(x)

	if type == "min":
		if (best1 < best["eval"]): 
			return {"sol":x,"eval":best1}
		else:
			test = HillClimbing(best["sol"], Fx, lower, upper, N, type)
			if test:
				return test
			else:
				return {"sol":x,"eval":best1}
	else:
		if (best1 > best["eval"]): 
			return {"sol":x,"eval":best1}
		else:
			test = HillClimbing(best["sol"], Fx, lower, upper, N, type)
			if test:
				return test
			else:
				return {"sol":x,"eval":best1}


		

