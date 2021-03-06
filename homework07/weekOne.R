df <- read.csv('mlbootcamp5_train.csv')
head(df)
mean(df$height[df$gender == 1])
mean(df$height[df$gender == 2])
sex <- as.array(df$gender == 1)
female <- which(sex == TRUE)
male <- which(sex == FALSE)
alco_fem <- length(as.array(which(as.array(df$alco == 1) & sex == TRUE)))
alco_m <- length(as.array(which(as.array(df$alco == 1) & sex == FALSE)))
print(length(female))
print(alco_fem)
print(alco_m)
smoke_fem <- length(as.array(which(as.array(df$smoke == 1) & sex == TRUE)))
smoke_m <- length(as.array(which(as.array(df$smoke == 1) & sex == FALSE)))
s_w <- smoke_fem / length(female) * 100
s_m <- smoke_m / length(male) * 100
print(round(s_m/s_w))
df$age_years <- round(df$age / 365)
head(df)
mean(df$age_years[df$smoke == 1])
mean(df$age_years[df$smoke == 0])
mean(df$age_years[df$smoke == 0])
mean(df$age_years[df$smoke == 1])
print(median(df$age_years[df$smoke == 0])*12 - median(df$age_years[df$smoke == 1])*12)
v1 <- df$cardio[(df$gender == 2) & (df$age_years >=60) & (df$age_years <=64) & (df$smoke == 1) & (df$ap_hi < 120) & (df$cholesterol ==1)] 
v2 <- df$cardio[(df$gender == 2) & (df$age_years >=60) & (df$age_years <=64) & (df$smoke == 1) & (df$ap_hi >= 160) &(df$ap_hi < 180) & (df$cholesterol ==1)]
print(round(mean(v2)/mean(v1)))
df$height_m <- (df$height/100)**2
df$BMI <- df$weight/df$height_m
print(median(round(df$BMI)))
print(mean(round(df$BMI[female])))
print(mean(round(df$BMI[male])))
print(mean(round(df$BMI[which(df$cardio == 0)])))
print(mean(round(df$BMI[which(df$cardio == 1)])))
print(mean(round(df$BMI[which(as.array(df$alco == 0) & as.array(df$cardio == 0) & sex == FALSE)])))
print(mean(round(df$BMI[which(as.array(df$alco == 0) & as.array(df$cardio == 0) & sex == TRUE)])))
new_df <- length(df$BMI[(df$ap_hi >=  df$ap_lo) & (df$height >= quantile(df$height, 0.025)) & (df$height <= quantile(df$height, 0.975)) & (df$weight >= quantile(df$weight, 0.025)) & (df$weight <= quantile(df$weight, 0.975))])
first_df <- length(df$BMI)
s = round( new_df/ first_df *100, 0)
print(100-s)
