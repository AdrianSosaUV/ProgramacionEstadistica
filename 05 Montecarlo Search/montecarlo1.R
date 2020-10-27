### montecarlo.R file  ###

source("../03 Blind Searc/fsearch.R", encoding = "utf-8")

mcsearch <- function(N, lower, upper, Fx, type="min", ...)
{
  D <- length(lower)              # vars
  s <- matrix(nrow=N, ncol=D)     # espacio de búsqueda
  for (i in 1:N) s[i,] = runif(D, lower, upper)  # números aleatorios
  fsearch(sol=s, Fx=Fx, type=type, ...)
}