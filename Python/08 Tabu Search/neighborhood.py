# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def neighborhood(lower, upper, N):
	D=len(lower)
	sol = np.zeros((N,D))
	for i in range(N):
		for j in range(D):
			sol[i][j] = np.random.uniform(lower[j],upper[j])
	return sol 
