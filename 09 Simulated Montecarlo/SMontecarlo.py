# !/usr/bin/env python
# -*- coding: utf-8 -*-

from fun import *
import math
def MonteCarlo(Fx, min, max, smp=5000):
	"""
	Esta función realiza el metodo montecarlo puro.
	Args:
	- Fx  : función a evaluar
	- min : valor minimo
	- max : valor maximo
	- smp : numero de muestras
	"""
	suma = 0
	for i in range(smp):
		x = randnum(min, max)
		suma += Fx(x)

	estimacion = (max - min)*float(suma/smp)

	# promedio de cuadrados
	running_total = 0
	for i in range(smp):
		x = randnum(0, max)
		running_total += pow(Fx(x),2)
	sumSqs = running_total*max / smp
	
	# cuadrado del promedio
	running_total = 0
	for i in range(smp):
		x = randnum(0, max)
		running_total = Fx(x)
	sqs_ave = pow((max*running_total/smp),2)
	
	varianza = sumSqs - sqs_ave
	error = math.sqrt(varianza/smp)
	return {"estimation":estimacion,"variance":varianza,"error":error}


