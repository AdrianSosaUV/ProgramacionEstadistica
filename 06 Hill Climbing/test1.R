A <- c(1,1,1,1,1,2,2,2,2,2)
B <- c(1:10)

Data <- data.frame(A,B)

Data

Out = change(Data, Var = 'B',
         type = 'proportion',
         NewVar = 'PercentChange',
         slideBy = -2)

Out