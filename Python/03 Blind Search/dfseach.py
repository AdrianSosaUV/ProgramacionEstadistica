# !/usr/bin/env python
# -*- coding: utf-8 -*-

from fsearch import *

def dfsearch(dominio, Fx, l=0, b=0, type="min", D=None, x=None, msol=None):
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
		ib = fsearch(dominio, Fx, type)
		return np.min(msol[0]) if ib==1 else x
	else:
		for j in range(len(dominio)):
			x[l-1]= dominio[l-1][j]
			msol = dfsearch(dominio, Fx, l+1, j, type, x=x, msol=msol)	
	return np.min(msol)if type =="min" else np.max(msol)
