# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def fibonachi(a=0, b=1, N=10, lim=float("inf")):
    """ Generador de numeros de Fibonachi
    a   -	Numero inicial 
    b   -	Numero secuencial 
    N   -	Longitud de la secuencia 
    Lim -	Limite de la secuencia
    """

    n = 0
    queue = []
    while n < N:
        if b < lim:
            queue.append(a)
        else:
            break
        a, b = b, a + b
        n += 1
    return queue[-1]