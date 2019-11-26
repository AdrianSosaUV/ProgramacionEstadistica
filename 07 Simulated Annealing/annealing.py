# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd 
from fsearch import *

def annealing(x, Fx, lower, upper, N=1000, W=10, maxiter=20000, type="min"):

	if (not type == "min" and not type == "max"):
		raise ValueError("Metodo de optimización no valido")

	S = fsearch(neighborhood(lower, upper, N), Fx, type)
	Best = {"sol":x,"eval":Fx(x)}
	l = 0
	while True:
		if(type=="min" and S["eval"] < Best["eval"] and l < maxiter):
			for i in range(W):
				if S["eval"] < Best["eval"]:
					Best = S 
				else:
					S = fsearch(neighborhood(lower, upper, N), Fx, type)
				l += 1
		elif (type=="max" and S["eval"] > Best["eval"] and l < maxiter):
			for i in range(W):
				if S["eval"] > Best["eval"]:
					Best = S 
				else:
					S = fsearch(neighborhood(lower, upper, N), Fx, type)
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



