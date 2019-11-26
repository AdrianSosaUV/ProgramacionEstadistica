# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
import math
from GridSearch import *

var = 5
upper = [1000]*var
lower = [1]*var
step = [50]*var 

def f(x):
	return -pow(x,5)+ pow(x,4) + x

valor= GridSearch(step, lower, upper, f, "min")
print("x: ",valor)
print("y: ",f(valor))

