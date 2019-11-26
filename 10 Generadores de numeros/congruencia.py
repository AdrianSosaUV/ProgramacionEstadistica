# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def congruencia(seed, a, c, m):
	"""
	Argumentos:
	seed -	semilla, numero inicial
	a 	 -	multiplicador constante
	c    -	incremento
	m    - 	modulo

	devuelve:
	aleatorio
	"""
	X0 = (a*seed+c) % m
	return X0/m  