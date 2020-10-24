### grid.R file ###

source("C:/Users/adrsosa/OneDrive - Universidad Veracruzana/Programación Estadistica/03 Blind Search/fsearch.R", encoding = "utf-8")

#		Metodo estandar de búsqueda en maya (búsqueda ciega amplitud)
#		step	-	vector con el tamaño del paso para cada dimensión D
#		lower	-	vector con el valor mas bajo de cada dimensión
#		upper	-	vector con el valor mas alto de cada dimensión
#		FUN		-	Función a evaluar
#		type	-	"min"o "max"
#		...		-	parametros extras para FUN

gsearch <- function(step,lower,upper,FUN,type="min",...)
{
  # dimensión
  D<-length(step)
  # valores de dominio
  domain<-vector("list",D)
  # vector auxiliar
  L <- vector(length=D)
  # llenamos domain con una secuencia d enumeros desde lower hasta upper en pasos de step
  # se actualiza el vector auxiliar con la longitud de cada arreglo de domain
  for(i in 1:D)
  { 
    domain[[i]]=seq(lower[i],upper[i],by=step[i])
    L[i]=length(domain[[i]])
  }
  # obtenemos el producto de L
  LS <- prod(L)
  # definimos el espacio de busqueda
  s <- matrix(ncol=D, nrow=LS)
  for (i in 1:D)
  {
    if (i==1) E <-1 else E <- E+L[i+1]			# se define cada cuanto se repite la serie 
    s[,i] <- rep(domain[[i]], length.out=LS, each=E)	# llena el espacio de busqueda con valores sucesivos definidos por E y domain
  }
  fsearch(sol=s, Fx=FUN,type=type,...)		#buscamos la mejor solución
}

#		Metodo estandar de búsqueda en maya (búsqueda ciega profundidad)
#		step	-	vector con el tamaño del paso para cada dimensión D
#		lower	-	vector con el valor mas bajo de cada dimensión
#		upper	-	vector con el valor mas alto de cada dimensión
#		FUN		-	Función a evaluar
#		type	-	"min"o "max"
#		...		-	parametros extras para FUN

fgsearch <- function(step,lower,upper,FUN,type="min",...)
{
	D = length(step)						# dimensiones
	dominio=vector("list",D)					# valores de dominio
	for(i in 1:D) dominio[[i]]=seq(lower[i],upper[i],by=step[i])		# llena el dominio de busqueda con valors secuenciales dentre upper y lower en steps

	dfsearch(dominio=dominio, Fx=FUN, type=type, ...) # solution
}