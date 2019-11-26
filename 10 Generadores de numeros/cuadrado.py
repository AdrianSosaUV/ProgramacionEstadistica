# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import math 

def cuadrado(num, iter = 20):
	"""
	Argumentos:
	num  -	número inicial
	iter -	número de iteraciones
	
	devuelve:
	aleatorio
	"""

    memory = []
    i= 0
    while i < iter:
        new = pow(num,2)
        news = str(new)
        longitud = len(news)
        if longitud >= 5:
            bound = math.floor((longitud - 4)/2)
            verifica = bound % 2
            if not(verifica == 0):
                bound += 1
            bound = int(bound)
            news = news[bound:bound + 4]
            if news == "0000" or news == "0":
                return memory[-1]
                break
            if not(news in memory):
                memory.append(news)
                num = int(news)
            else:
                break
        else:
            num = pow(num, 2)
        i += 1    
    return num