x <- c(1:20)
y <- c(x^2)
library(ggplot2)
qplot(x, y, geom=c("point","line"),main = "Graph of X against Y axis",
      xlab = "X-Values", ylab = "Y-Values", color= I("blue"))

