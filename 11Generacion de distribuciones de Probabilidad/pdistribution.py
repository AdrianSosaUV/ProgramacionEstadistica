# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sb 

np.random.seed(2016)
sb.set_palette("deep", desat=.6)
sb.set_context(rc={"figure.figsize": (8, 4)})

class Distribuciones():


	def Histograma(self, data, box=20):
		"""Histograma
		es una representación gráfica de una variable en forma de barras, 
		donde la superficie de cada barra es proporcional a la frecuencia 
		de los valores representado
		"""

		count, box, ignore = plt.hist(data, box)

	def MProbabilidad(self, x, x1, n, n1, p, p1, str='--'):
		"""Función de Masa de Probabilidad
		Asocia a cada punto de su espacio muestral X la probabilidad 
	de que ésta lo asuma.
		"""

		fmp = stats.binom.pmf(x, n, p) # Función de Masa de Probabilidad
		fmp1 = stats.binom.pmf(x1, n1, p1) # Función de Masa de Probabilidad
		plt.plot(x, fmp, str )
		plt.plot(x1, fmp1)
		plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
		plt.vlines(x1, 0, fmp1, colors='g', lw=5, alpha=0.5)

	def DAcumulada(self, x, x1, n, p, str='--'):
		"""Función de Distribución Acumulada
		 Relaciona los valores con su correspondiente percentil; 
		 Describe la probabilidad de que una variable aleatoria X 
		 sujeta a cierta ley de distribución de probabilidad se sitúe 
		 en la zona de valores menores o iguales a x.
		 """

		fda_binom = stats.binom.cdf(x, n, p)			#Función de distribución acumulada binomial
		fda_normal = stats.norm(10, 1.2).cdf(x1)		#Función de distribución acumulada normal
		plt.plot(x, fda_binom, str, label='FDA binomial')
		plt.plot(x1, fda_normal, label='FDA nomal')
		plt.legend(loc=4)

	def DProbabilidad(self, x):
		"""Función de Densidad de Probabilidad
		Derivada de la Función de Distribución Acumulada
		"""
		
		FDP = stats.norm(10, 1.2).pdf(x)
		plt.plot(x, FDP, label='FDP normal')
		
	def Poisson(self, x, fun, str='--'):
		"""Distribución de Poisson
		La Distribución Poisson describe la probabilidad de encontrar exactamente r eventos 
		en un lapso de tiempo si los acontecimientos se producen de forma independiente a 
		una velocidad constante μ.
		"""

		fmp = fun.pmf(x) 
		plt.plot(x, fmp, str)
		plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)

	def Binomial(self, x, fun, str='--'):
		"""Distribución Binomial
		Describe la probabilidad de exactamente 'r' éxitos en 'N' 
		pruebas si la probabilidad de éxito en una sola prueba es 'p'.
		"""

		fmp = fun.pmf(x) 
		plt.plot(x, fmp, str)
		plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)

	def Geometrica(self, x, fun, str='--'):
		"""Distribución Geometrica
		Expresa la probabilidad de tener que esperar exactamente 'r' pruebas
		hasta encontrar el primer éxito si la probabilidad de éxito en una sola prueba es 'p'.
		"""

		fmp = fun.pmf(x) 
		plt.plot(x, fmp, str)
		plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)

	def HGeometrica(self, x, fun, str='--'):
		"""Distribución Hiper Geometrica
		Describe experimentos en donde se seleccionan los elementos al azar sin reemplazo
		(se evita seleccionar el mismo elemento más de una vez).
		"""

		fmp = fun.pmf(x) # Función de Masa de Probabilidad
		plt.plot(x, fmp, str)
		plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)

	def Bernoulli(self, x, fun, str='bo'):
		"""Distribución de Bernoulli
		Describe un experimento probabilístico en donde el ensayo tiene dos posibles resultados, éxito o fracaso.
		"""

		fmp = fun.pmf(x) 
		fig, ax = plt.subplots()
		ax.plot(x, fmp, str)
		ax.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
		ax.set_yticks([0., 0.2, 0.4, 0.6])

	
	def Normal(self, x, fun):
		"""distribución de Normal 
		tambien llamada distribución de Gauss
		"""
		
		fp = fun.pdf(x) # Función de Probabilidad
		plt.plot(x, fp)

	def Uniforme(self, x, fun, str='--'):
		"""Distribución Uniforme"""

		fp = fun.pdf(x) # Función de Probabilidad
		fig, ax = plt.subplots()
		ax.plot(x, fp, str)
		ax.vlines(x, 0, fp, colors='b', lw=5, alpha=0.5)
		ax.set_yticks([0., 0.2, 0.4, 0.6, 0.8, 1., 1.2])

	def LogN(self, x, fun):
		"""Distribución Log-Normal"""

		fp = fun.pdf(x) # Función de Probabilidad
		plt.plot(x, fp)

	def Exponencial(self, x, fun):
		"""Funcion Exponencial"""

		fp = fun.pdf(x) # Función de Probabilidad
		plt.plot(x, fp)

	def Plot(self, title, ylabel, xlabel):
		"""Función complementaria de graficación"""
		plt.ylabel(ylabel)
		plt.xlabel(xlabel)
		plt.title(title)
		plt.grid()	
		plt.show()