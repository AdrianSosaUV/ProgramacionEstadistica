### blind.R file ###

#	Método de busqueda ciega
#	Halla la solucion de la función Fx en el espacio de busqueda.
#
#	Argumentos
#	----------
#	Fx 				- Función
#	sol			- Espacio de busqueda, Matrix(MxN)
#	type (opcional) - Tipo de optimización
#					- min -> mínimo 
#					- max -> máximo 
#	...				- Parametros extras para Fx
#
#	Devuelve
#	--------
#	x - Solucion de la funcion Fx en el espacio de busqueda

fsearch <- function(sol,Fx, type="min",...)
{
	x  	<- apply(sol,1,Fx,...)
	ib 	<- switch(type, min=which.min(x), max=which.max(x))	
	return(list(index=ib,sol=sol[ib], eval=x[ib]))
}

#	Método de busqueda ciega completa 
#	Halla la solucion de la función Fx en el espacio de busqueda.
#
#	Argumentos
#	----------
#	Fx 				- Función
#	dominio 		- Espacio de busqueda, Matrix(MxN)
#	l 				- Nivel del arbol
#	b 				- Rama del arbol
#	type (opcional) - Tipo de optimización
#					- min -> mínimo 
#					- max -> máximo 
#	D 				- Dimensión (numero de variables)
#	x 				- vector de posibles soluciones
#	msol 			- mejor solucion actual 
#	...				- Parametros extras para Fx
#
#	Devuelve
#	--------
#	msol - Solucion de la funcion Fx en el espacio de busqueda

dfsearch <- function(domino, Fx, l=1, b=1,type="min", D=length(dominio), x=rep(NA,D), 
	msol=switch(type, min=list(sol=NULL,eval=Inf), max=list(sol=NULL,eval=-Inf)), ...)
{
	if((l-1) == D)
	{
		f <- Fx(x,...)
		fb <- msol$eval 
		ib <- switch(type, min=which.min(c(fb,f)), max=which.max(c(fb,f)))
		if(ib ==1) return(msol) else return(list(index= ib, sol=x,eval=f,bsol=x[ib],beval=f[ib]))
	}else
	{
		for(j in 1:length(dominio[[l]]))
		{
			x[l] <- dominio[[l]][j]
			msol <- dfsearch(dominio, Fx, l+1, j, type, D=D, x=x, msol=msol, ...)
		}
		return(msol)				
	}
}