### graph.R file ###
library("ggplot2")
graph <- function(limI, limS, steps, Fx, min, max)
{
	x <-seq(limI, limS, steps)
	y <- c()
	for( i in seq_along(x))
	{
	  y[i] <- Fx(x[i])
	}
	df <- data.frame(x,y) 
	ggplot(data= df, mapping=aes(x= x, y =y))+
  		geom_line(color=4)+
  		annotate(geom="text",  x=min$sol-1, y=min$eval, label="mínimo")+
  		annotate(geom="point", x=min$sol, y=min$eval, size =5, shape=14, fill="transparent")+  
  		annotate(geom="text",  x=max$sol-1, y=max$eval, label="máximo")+
  		annotate(geom="point", x=max$sol, y=max$eval, size =5, shape=14, fill="transparent")
}

