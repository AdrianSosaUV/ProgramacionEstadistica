# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np 
import math

def fsearch(Fx, sol, type="min"):
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
	ib = np.min(y) if type == "min" else np.max(y)
	return ib[0]

def dfsearch(dominio, Fx, l=0, b=1, type="min", D=None, x=None, msol=None):
	"""Método de busqueda ciega completa 
	Halla la solucion de la función Fx en el espacio de busqueda.
	Argumentos
	----------
	Fx - Función
	dominio - Espacio de busqueda, Matrix(MxN)
	l - Nivel del arbol
	b - Rama del arbol
	type (opcional) - Tipo de optimización
	D - Dimensión (numero de variables)
	x - vector de posibles soluciones
	msol - mejor solucion actual 
	
	Devuelve
	--------
	x - Solucion de la funcion Fx en el espacio de busqueda
	"""
	if (not type == "min" and not type == "max"):
		raise ValueError("Metodo de optimización no valido")

	D = len(dominio) if D == None else D
	x = [None]*len(dominio) if x== None else x
	msol = ([None, float('inf')]if type=="min" else [None, float('-inf')]) if msol == None else msol
	if ((l-1)==D):
		f = pd.DataFrame((dominio))
		f = f.apply(Fx)
		fb = msol[1]
		ib = np.min(f) if type == "min" else np.max(f)
		ib = sorted(ib, reverse=True)[0]
		return np.min(msol[0]) if ib==1 else x
	else:
		for j in range(len(dominio)):
			x[l-1]= dominio[l-1][j]
			msol = dfsearch(dominio, Fx, l+1, j, type, x=x, msol=msol)
		return msol

def f(x):
	return pow(x,3)+ 4*pow(x,2)-10
	#return pow((x-7),3)+ pow((2*x-5),2)

def espacio(m, n, r1, r2):
	dat = np.zeros((m,n))
	for i in range(m):
		for j in range(n):
			dat[i][j] = np.random.randint(r1, r2)
	return dat 

a = 0	#limite inferior
b = 9	#limite superior
c = 3	#numero de variables
d = 5	#tamaño del espacio
metodo= dfsearch(espacio(c,d,a,b),f, type="min")
print(sorted(metodo))
print("x: ",sorted(metodo, reverse=True))
print("y: ",f(sorted(metodo, reverse=True)[0]))
