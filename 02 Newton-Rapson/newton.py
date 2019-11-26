def newton(f, df, x_0, maxiter=50, xtol=1.0e-6, ftol=1.0e-6):
    """Método de Newton
    Halla la raíz de la función f en el entorno de x_0 mediante el método de
    Newton.
    Argumentos
    ----------
    f - Función
    df - Función, debe ser la función derivada de f
    x_0 - Punto de partida del método
    maxiter (opcional) - Número máximo de iteraciones
    xtol (opcional) - Cota para el error relativo para la raíz
    ftol (opcional) - Cota para el valor de la función
    Devuelve
    --------
    x - Raíz de la ecuación en el entorno de x_0
    """
    x = float(x_0)  # Se convierte a número de coma flotante
    for i in range(maxiter):
        dx = -f(x) / df(x)  # ¡Aquí se puede producir una división por cero!
                            # También x puede haber quedado fuera del dominio
        x = x + dx
        if abs(dx / x) < xtol and abs(f(x)) < ftol:
            return x
    raise RuntimeError("No hubo convergencia después de {} iteraciones".format(maxiter))










def newt(Fx,Fx1, p0, iters=50 , tol = 1.0e-6):
    for i in range(iters):
        p0= float(p0)
        p = p0 - (Fx(p0)/Fx1(p0))

        if abs(p - p0)< tol:
            return float(p)
            i= iters
        else:
            i += 1
            p0=p








def f(x):
    """Funcion a evaluar x^3 +4x^2 -10"""
    return pow(x,3)+ 4*pow(x,2)-10

def df(x):
    '''Derivada de la funcion, 3x^2 + 8x '''
    return 3*pow(x,2) + 8*x
