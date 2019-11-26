# !/usr/bin/env python
# -*- coding: utf-8 -*-


def MontecarloSearch(N, lower, upper, Fx, type="min"):

	if (not type == "min" and not type == "max"):
		raise ValueError("Metodo de optimización no valido")

	D = len(lower)

	s = np.zeros((N, D))
	for i in range(N):
		for j in range(D):
			s[N][D]: np.random.randint(lower[D], upper[D])

	return fsearch(s, Fx, type)
