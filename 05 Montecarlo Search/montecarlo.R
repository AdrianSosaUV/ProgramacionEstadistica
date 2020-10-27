### montecarlo.R file ###

source("../03 Blind Search/fsearch.R", encoding = "utf-8")

#		Metodo uniforme de búsqueda montecarlo
#		N		-	Número de muestras
#		lower	-	Vector con el valor mas bajo de cada dimensión
#		upper	-	Vector con el valor mas alto de cada dimensión
#		Fx		-	Función a evaluar
#		type	-	"min"o "max"
#		...		-	parametros extras para FUN

mcsearch <- function(N, lower, upper, Fx, type="min", ...)
{
  D <- length(lower)
  s <- matrix(nrow=N, ncol=D)						# se define el espacio de búsqueda
  for (i in 1:N) s[i,] = runif(D,lower, upper)		# se utilizan números aleatorios 
  fsearch(sol=s, Fx=Fx, type=type, ...)				# mejor solución
}