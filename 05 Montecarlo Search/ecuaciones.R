### ecuaciones.R file ###

sphere <- function(x) {sum(x^2)}
rastrigin <- function(x) {10*length(x)+sum(x^2-10*cos(2*pi*x))}


