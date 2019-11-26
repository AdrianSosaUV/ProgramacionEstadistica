###blind-test.R file ###

source("blind.R")	# se cargan los metodos de busqueda ciega

# leer los D bits de un entero X

binint = function(x,D)
{
	x = rev(intToBits(x)[1:D])	# obtener los D bits
	as.numeric(unlist(strsplit(as.character(x),""))[(1:D)*2])	# eliminar los 0´s del arreglo 
}

# convertir un vector binario en entero
intbin = function(x) sum(2^(which(rev(x==1))-1))

# suma del binario X sin procesar ( funcion a evaluar)
sumbin = function(x) sum(as.numeric(x))

# maximo seno del objeto binario sin procesar 
maxsin = function(x, Dim) sin(pi*(intbin(x))/(2^Dim))

D = 8	# numero de dimensiones
x = 0 :(2^D-1)	# espacio de busqueda (enteros)
# establecer espacio d ebusqueda completo en las soluciones x D
objetivo = t(sapply(x, binint, D=D))
# establecer los valores de dominio ( D variables binarias)
dominio = vector("list",D)
for (i in 1:D) dominio[[i]] = c(0,1) #bits

# suma de bits, fsearch:
S1 = fsearch(objetivo, sumbin, "max")	# busqueda completa
cat("mejor fsearch s:", S1$sol, "f:", S1$eval, "\n")

# suma de bits, dfsearch:
S2 = dfsearch(dominio=dominio, Fx=sumbin, type="max")
cat("mejor dfsearch s:", S2$sol, "f:", S2$eval, "\n")

# maximo seno, fsearch:
S3 = fsearch(objetivo, maxsin, "max", Dim=8)	# busqueda completa
cat("mejor fsearch s:", S3$sol, "f:", S3$eval, "\n")

# maximo seno, dfsearch:
S4 = dfsearch(dominio=dominio, Fx=maxsin, type="max", Dim=8)
cat("mejor dfsearch s:", S4$sol, "f:", S4$eval, "\n")