data1=read.csv("/Users/tianpujia/Desktop/Tesla-s&p.csv")
lm1 = lm(formula=Tesla_return~sp_return, data = data1)
summary(lm1)

FitWithConfidencePlots <- function(
    formula,
    dataset){
  fit_coef = lm(formula, dataset)
  return(fit_coef$coefficients[[1]])
}

FitWithConfidencePlots(Tesla_return~sp_return,data1)

MeanAbsoluteError <- function(linearModel){
  average=mean(abs(linearModel$residuals))
  return(average)
}

MeanAbsoluteError(lm1)

library(ggplot2)
plot1=ggplot(data1, aes(x = sp_return, y = Tesla_return)) + 
  geom_point() +
  stat_smooth(method = "lm", col = "red") 
plot1
