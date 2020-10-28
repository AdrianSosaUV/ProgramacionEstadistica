### hillclimbing.R file ###

source("../03 Blind Search/fsearch.R", encoding = "utf-8")

#     Ascenso a la cordillera:
#     x   -   Solución inicial
#     Fx  -   Función
#     lower   -   Vector con el valor mas bajo de cada dimensión
#     upper   -   Vector con el valor mas alto de cada dimensión
#     N   -   Número de puntos aleatorios
#     type  -   "min" or "max"
#     ...   -   Parametros extras para FUN

hclimbing <- function(x, Fx, lower, upper, type="min", N= 1000, ...)
{
  D <- length(lower)
  s <- matrix(nrow=N, ncol=D)
  for (i in 1:N) s[i,] = runif(D,lower, upper)
  best <- fsearch(sol=s, Fx=Fx, type=type, ...)	
  best_1 <- Fx(x, ...)
  
  if(type=="min")
  {
    if(best_1 < best$eval) return(list(sol=x, eval=best_1)) else hclimbing(best$sol, Fx, lower, upper, type, N, ...)
  }else{
    if(best_1 > best$eval) return(list(sol=x, eval=best_1)) else hclimbing(best$sol, Fx, lower, upper, type, N, ...)
  }
}