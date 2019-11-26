# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
from fsearch import *

def sannealing (S, Fx, upper, lower, W=10, N=1000, maxit=20000, type ="min"):
	
	if (not type == "min" and not type == "max"):
		raise ValueError("Metodo de optimización no valido")

	Fs = fsearch(neighborhood(lower, upper, N), Fx, type) 
	Best = {"sol":S,"eval":Fx(S)}
	l = 0 #contador de iteraciones
	while True:
		if (type == "min" and Fs["eval"] < Best["eval"] and l < maxit):
			for i in range(W):
				if (Fs["eval"] < Best["eval"]):
					Best = Fs
				else:
					Fs = fsearch(neighborhood(lower, upper, N), Fx, type)
				l += 1

		elif (type == "max" and Fs["eval"] > Best["eval"] and l < maxit):
			for i in range(W):
				if (Fs["eval"] > Best["eval"]):

					Best = Fs
				else:
					Fs = fsearch(neighborhood(lower, upper, N), Fx, type)
				l += 1
		else:
			break
	return Best




def neighborhood(lower, upper, N):
	D=len(lower)
	sol = np.zeros((N,D))
	for i in range(N):
		for j in range(D):
			sol[i][j] = np.random.uniform(lower[j],upper[j])
	return sol 
