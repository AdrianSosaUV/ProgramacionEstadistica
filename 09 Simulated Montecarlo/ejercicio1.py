from fun import *
from SMontecarlo import *
import matplotlib.pyplot as plt 
import numpy as np 
n = 100
lista = []
for i in range(n):
	lista.append(MonteCarlo(sphere,-5.12,5.12))
lista2=[]
for i in lista:
	lista2.append(i["estimation"])

promedio = np.array(lista2).mean()
print ("Promedio: {}".format(promedio))
plt.plot(lista2)
plt.show()