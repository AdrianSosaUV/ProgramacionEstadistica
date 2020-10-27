### ecuaciones.R file ###

sphere <- function(x) {sum(x^2)}
rastrigin <- function(x) {10*length(x)+sum(x^2-10*cos(2*pi*x))}


fx1 <- function(x){return((x^2 + 3)*(x^2 - 4*x))}
fx2 <- function(x){return((6*x + 5)*(x^3 - 2))}
fx3 <- function(x){return(x*(1 - x^2))}
fx4 <- function(x){return(x*(x^2 + 8))}
fx5 <- function(x){return(x^3 * cos(x))}
fx6 <- function(x){return(x*sin(x))}
fx7 <- function(x){return(x/(x^2+1))}
fx8 <- function(x){return((x^2 + 4)/(5*x - 3))}
fx9 <- function(x){return(sin(x)/(x^3 + 1))}
fx10 <- function(x){return(sin(x)/x^2)}


fxh1 <- function(x){return(x*(1 - (4/(x + 3))))}
fxh2 <- function(x){return(x^4*(1 - (2/(x + 1))))}
fxh3 <- function(x){return((3*x - 1)/sin(x))}
fxh4 <- function(x){return((x^2 - 2)^2)}
fxh5 <- function(x){return((1/4)*x^4 + 2*x^2)}
fxh6 <- function(x){return((2 - (1/x))/(x - 3))}
fxh7 <- function(x){return(x^2 *((2/x)-(1/(x+1))))}
fxh8 <- function(x){return(cos(x)/x^3)}
fxh9 <- function(x){return((1/x) - 12* sin(x))}
fxh10 <- function(x){return(2*x*sin(x) + x^2*cos(x))}