 #calling the libraries
library(ggplot2)
library("dplyr")
#reading in the data
ilr <-read.csv("C:\\GLOBE PROJECT\\newmay.csv",stringsAsFactors = FALSE,header = TRUE)
ilara2 <-read.csv("C:\\GLOBE PROJECT\\newoct.csv",stringsAsFactors = FALSE)
#getting high level ovierview of the may data
str(ilr)
summary(ilr)
#getting high level ovierview of the oct data
str(ilara2)
summary(ilara2)
#making a pairplot
pairs(ilr)
pairs(ilara2)
#calculating correlation coeficient
cor.test(ilr$TDS.mg.l.,ilr$Sal.mg.l.)
#using spearman correlation coefficient
cor(ilr,method ="spearman") #for may data
cor(ilara2,method = "spearman") #for october data
