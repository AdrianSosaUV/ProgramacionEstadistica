### biseccion.R file ###

# Método de bisección
# Halla una raíz de la función Fx en el intervalo [a, b] mediante el método
# de bisección.
#
# Argumentos
# ----------
# Fx    - Función, debe ser tal que f(a)*f(b) < 0
# limI  - Extremo inferior del intervalo
# limS  - Extremo superior del intervalo
# tol (opcional) - Cota para el error absoluto de la x
#
# Devuelve
# --------
# x - Raíz de Fx en [a, b]

biseccion <- function(Fx,limI, limS, tol=1.0e-6)
{
  repeat
  {
    # punto medio
    x <- (limI + limS) / 2 
    L <- (limS - limI) / 2    
    if(Fx(x) == 0)
    {
      return(x)
      break
    }else if (Fx(limI)*Fx(x) < 0)
    {
      # [a,x]
      limS <- x               
    }else
    {
      # [x,b]
      limI <- x               
    }
    if(L < tol)
    {
      return(x)
      break
    }
  }
}