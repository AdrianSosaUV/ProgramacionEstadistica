# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Maquina import *
import threading


numObj = 4
random = np.random
maquina = Maquina(numObj)
objetos = [Objeto(True, random.randint(600), random.randint(400)) for i in range(numObj)]
#print(objetos[0].x)
bateria = Objeto(True, random.randint(600), random.randint(400))
maquina.Inicializa(objetos, bateria)
maquina.Run()
#hilo = threading.Thread(target= maquina.Run())
#hilo.start()
