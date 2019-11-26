# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
import time
from aEstrella import nodo, A_star

state = ["Busqueda", "NuevaBusqueda", "IrBateria", "Recargar", "Muerto", "Aleatorio"]
class Objeto():
	def __init__(self,state, x, y):
		self.state=state
		self.x = x
		self.y = y

class Maquina():
	"""
	Clase para definir una maquina virtual
	"""

	def __init__(self, n, x=320, y=240):
		self.State = state[1]
		self.x = x
		self.y = y
		self.objets = np.array((n))
		self.index = -1
		self.indexPath = 0
		self.energy = 800
		self.isDead = False
		self.path = []
		self.Astar = A_star()

	def Inicializa(self, objetos, bateria):
		self.objets = objetos
		self.bateria = bateria
		print("Inicializando Maquina")
		print("-> Robot")
		print("x: {}".format(self.x))
		print("y: {}".format(self.y))
		for i in self.objets:
			print("Objeto: {}".format(self.objets.index(i)))
			print("x: {}".format(i.x))
			print("y: {}".format(i.y))
		print("-> Bateria")
		print("x: {}".format(bateria.x))
		print("y: {}".format(bateria.y))
		print("---------------------")

	def Search(self):
		self.x = self.path[self.indexPath].x
		self.y = self.path[self.indexPath].y
		self.indexPath += 1
		self.energy -= 1
		print("Robot (buscando) {}, {} -> {} ".format(self.x,self.y, self.energy))

	def NewSearch(self):
		print("== NUEVA BUSQUEDA ==")
		self.index = -1
		for n in range(len(self.objets)):
			if self.objets[n].state:
				self.index = n
				break
		if self.index > -1:
			self.path = self.Astar.algoritmo(self.objets[self.index], self.x, self.y)
			self.indexPath = 0

	def Aleatorio(self):
		ny = np.random.randint(0,3)
		nx = np.random.randint(0,3)

		self.x += nx -1
		self.y += ny -1

		self.energy -= 1
		print("-> Robot(Aleatorio) {}, {} -> {}}".format(self.x, self.y, self.energy))
		
	def GoBatery(self):
		self.x = self.path[self.indexPath].x
		self.y = self.path[self.indexPath].y
		self.indexPath += 1
		self.energy -= 1
		print("-> Robot(IrBateria) {}, {} -> {}}".format(self.x, self.y, self.energy))

	def Reload(self):
		print("==Recargar==")
		self.energy = 800
		if self.index > -1:
			self.path = Astar.algoritmo(x,y, self.objets[self.index])
			self.indexPath = 0

	def Dead(self):
		print("==Muerto==")
		self.isDead = True

	def Run(self):
		"""este metodo se corre en un hilo paralelo"""

		while not self.isDead:
			if self.State == state[0]:
				self.Search()
				if self.x == self.objets[self.index].x and self.y==self.objets[self.index].y:
					self.objets[self.index].state = False
					self.State = state[1]
				else:
					if self.energy < 400:
						self.State = state[2]
						self.path = self.A_star.algoritmo(self.x, self.y, self.bateria)
						self.indexPath = 0
						break
						
			elif self.State == state[1]:
				self.NewSearch()
				self.State = state[5] if self.index < 0 else state[0]
				break

			elif self.State == state[2]:
				self.GoBatery()
				if (self.x == self.bateria.x and self.y == self.bateria.y):
					self.State = state[3]
				if self.energy == 0:
					self.State = state[4]
				break

			elif self.State == state[3]:
				self.Reload()
				self.State = state[0]

			elif self.State == state[4]:
				self.Dead()
				break

			elif self.State == state[5]:
				self.Aleatorio()
				if self.energy == 0:
					self.State = state[4]
					break

			else:
				pass

			try:
				time.sleep(50)
			except Exception as e:
				pritn(e)
