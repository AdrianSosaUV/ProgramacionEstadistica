
from fsearch import *
from neighborhood import *

def tabu(x, Fx, lower, upper, L, maxiter=20, N=10, type="min"):

	if (not type == "min" and not type == "max"):
		raise ValueError("Metodo de optimización no valido")

	lista=[]
	i=0
	while i < maxiter:
		for j in range(N):
			S1 = fsearch(neighborhood(lower, upper, 100),Fx, type)
			Clist =[]
			if S1 not in lista:
				Clist.append(S1["sol"])
		S1 = fsearch(Clist,Fx,type)
		S = {"sol":x,"eval":Fx(x)}
		if (type =="min" and S1["eval"]<S["eval"]):
			lista.append(S1)
			while len(lista) > L:
				del lista[0]
			S = S1
		elif (type =="max" and S1["eval"]>S["eval"]):
			lista.append(S1)
			while len(lista) > L:
				del lista[0]
			S = S1
		else:
			break
		i +=1
	return S 