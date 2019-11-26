# !/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np 

def randnum(min, max):
	range = max-min
	choice = np.random.uniform(0,1)
	return min + range*choice

def sphere(x,n=100):
	suma = 0
	for i in range(n):
		suma += pow(x,2)

	return suma 
