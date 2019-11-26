# metodo de busqueda ciega
# 	objetivo - matriz con las soluciones x D
# 	Fx - funcion a evaluar
# 	type - "min" o "max"
# 	... - parametros extras para Fx

fsearch = function(objetivo, Fx, type="min", ...)
{
	x = apply(objetivo,1,Fx,...) # evalua Fx sobre todas las filas
	ib = switch(type, min=which.min(x), max=which.max(x))
	return (list(index=ib, sol=objetivo[ib,], eval=x[ib]))
}

# metodo de busqueda completa en profundidad
# 	l - nivel del arbol
# 	b - rama del arbol
# 	dominio - lista de vectores de tamaño D con los valores de dominio
# 	Fx - funcion a evaluar
# 	type - "min" o "max"
# 	D - dimension (numero de variables)
# 	x - vector de soluciones actual
# 	msol - mejor solucion actual
# 	... - parametros extras para Fx

dfsearch = function(l=1, b=1, dominio, Fx, type="min", D=length(dominio),
		x=rep(NA, D), msol=switch(type, min=list(sol=NULL, eval=Inf),
									max=list(sol=NULL, eval=-Inf)), ... )
{
	if ((l-1)==D) # evalua la rama superior
	{
		f = Fx(x,...)
		fb = msol$eval
		ib = switch(type, min=which.min(c(fb, f)),max=which.max(c(fb, f)))
		if (ib==1) return (msol) else return(list(sol=x, eval=f))
	}
	else # pasa por las sub ramas
	{
		for (j in 1:length(dominio[[l]]))
		{
			x[1] = dominio[[l]][j]
			msol = dfsearch(l+1, j, dominio, Fx, type, D=D, x=x, msol=msol, ... )
		}
		return(msol)
	}
}

mcsearch = function(N,lower,upper,FUN,type="min",...) 
{ 
	D=length(lower) 
	s=matrix(nrow=N,ncol=D) # set the search space 
	for(i in 1:N) s[i,]=runif(D,lower,upper) 
	fsearch(s,FUN,type,...) # best solution
}

N= 1000

sphere=function(x) sum(x^2)
rastrigin=function(x) 10*length(x)+sum(x^2-10*cos(2*pi*x))
D=c(2,30)

label="sphere" 
for(i in 1:length(D)) 
{ 
	S=mcsearch(N,rep(-5.2,D[i]),rep(5.2,D[i]),sphere,"min") 
	cat(label,"D:",D[i],"s:",S$sol[1:2],"f:",S$eval,"\n") 
}
label="rastrigin" 
for(i in 1:length(D)) 
{ 
	S=mcsearch(N,rep(-5.2,D[i]),rep(5.2,D[i]),rastrigin,"min") 
	cat(label,"D:",D[i],"s:",S$sol[1:2],"f:",S$eval,"\n") 
}