### newton.R file ###

#    Método de Newton
#    Halla la raíz de la función Fp en el entorno de p_0 mediante el método de
#    Newton.
#
#    Argumentos
#    ----------
#    Fx - Función
#    df - Función, debe ser la función derivada de Fp
#    p_0 - Punto de partida del método
#    maxiter (opcional) - Número mápimo de iteraciones
#    tol (opcional) - Cota para el error relativo para la raíz
#
#    Devuelve
#    --------
#    p - Raíz de la ecuación en el entorno de p_0

newton <- function(Fx, df, p_0, maxiter=50, tol=1.0e-6)
{
	i <- 1
	while(i <= maxiter)
	{
		p <- p_0 -(Fx(p_0) / df(p_0)) 	# ¡Aquí se puede producir una división por cero!
										# También puede haber quedado fuera del dominio
		if(abs(p - p_0) < tol)
		{
			return(p)
			break
		}
		p_0 <- p
		i <- i + 1
	}
}
