# !/usr/bin/env python
# -*- coding: utf-8 -*-

class nodo():
	"""la clase nodo nos ayudara guardando las propiedades y estados que deseamos"""

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.estado = False
		self.Gn = 0
		self.Hn = 0
		self.Fn = 0

	def setFn(self):
		self.Fn = self.Gn + self.Hn

class A_star():
	"""clase a* para busqueda ciega profunda"""
	def __init__(self,x = 600, y=400):
		self.path = []
		self.open = []
		self.close = []
		self.targetReached = False
		self.xlim = x
		self.ylim = y

	def distanciaManhattan(self, n1, n2):
		return (abs(n1.x - n2[0]))+ abs(n1.y-n2[1])
	
	def getAdyacentes(self, nod):
			self.adya = []
			for y in range(nod.y):
				for x in range(nod.x):
					if (x >= 0 and x <= self.xlim and y >= 0 and y <= self.ylim):
						p = nodo(x,y)
					if (not p == nod and not self.onClose(p)):
						self.adya.append(p)
			print(len(self.adya))
			print(self.adya)
			return self.adya
	
	def onClose(self, p):
		ans = False
		if(not self.close):
			for n in self.close:
				if n == p:
					ans = True
					break
		return ans

	def onOpen(self, p):
		ans = False
		if(not self.open):
			for n in self.open:
				if n == p:
					ans = True
					break
		return ans 

	def algoritmo(self, target, x, y):
		"""
		Argumentos
		----------
		x - punto x inicial
		y - punto y inicial
		target - objetivo a localizar nodo(x,y)

		Devuelve
		--------
		path - el recorrido de nodos"""
		
		self.n0 = nodo(x,y)
		self.nTarget = (target.x, target.y)
		self.n0.Hn = self.distanciaManhattan(self.n0, self.nTarget)
		self.n0.Gn = 1
		self.n0.setFn()

		self.open.append(self.n0)
		while( self.open and not self.targetReached):
			self.cn = self.open[0]
			if (self.cn == self.nTarget):
				self.targetReached = True
			adyacentes = [self.getAdyacentes(self.cn)]
			print(len(adyacentes))
			if (not adyacentes):    #duda si lleba not o no
				for i in adyacentes:
					i.Gn=1
					i.Hn = self.distanciaManhattan(i, self.nTarget)
					i.setFn()
					print(i)
					if (not self.onOpen(i)):
						self.open.append(i)
			self.close.append(self.cn)
			self.open = self.open.sort()
		if (not self.close):
			for i in self.close:
				self.path.append(i)
				print(self.close)
		return self.path
		print(self.path)

		def __str__(self):
			print("Ruta con {} movimientos:".format(len(self.path)))
			for i in self.path:
				print(i)




				https://classroom.google.com