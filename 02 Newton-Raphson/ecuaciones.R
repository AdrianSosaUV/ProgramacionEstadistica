### ecuaciones.R file ###

# [-10,10]
fx1 <- function(x){return(x^2 + 3*x  - 2)}
dfx1 <- function(x){return(2*x + 3)}
# [-10,10]
fx2 <- function(x){return(x^5 + 10)}
dfx2 <- function(x){return(5*x^4)}
# [-10,10]
fx3 <- function(x){return(x^3 - x^2 + 3)}
dfx3 <- function(x){return(3*x^2 - 2*x)}
# [-10,10]
fx4 <- function(x){return(cos(x) + sin(x))}
dfx4 <- function(x){return(cos(x) - sin(x))}
# [-10,10]
fx5 <- function(x){return((x-7)^3 + (2*x-5)^2)}
dfx5 <- function(x){return(3*(x-7)^2 + 2*(2*x-5))}
# [-10,10]
fx6 <- function(x){return(x^3 - (x^2 / 2) - 3*x + 2)}
dfx6 <- function(x){return(3*x^2 - x - 3)}