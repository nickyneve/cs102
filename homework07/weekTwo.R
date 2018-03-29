df <- read.csv('mlbootcamp5_train.csv')
library(ggplot2)
head(df)
qplot(data=df, df$age, df$gender, df$height, df$weight, df$ap_hi, df$ap_lo, df$cholesterol, df$gluc, df$smoke, df$alco, df$active, df$cardio)