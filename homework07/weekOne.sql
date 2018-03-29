select avg(height) from train where gender = '1';
select avg(height) from train where gender = '2';
select count(id) from train where gender = '1';
select count(id) from train where gender = '2';
select count(alco) from train where gender = '1' and alco = '1';
select count(alco) from train where gender = '2' and alco = '1';
select ((select count(smoke) from train where gender = '2' and smoke = '1')/(select count(gender) from train where gender = '2')/(count(smoke)/(select count(gender) from train where gender = '1')) from train where gender = '1' and smoke = '1';
select (((select count(smoke) from train where gender = '2' and smoke = '1')/(select count(gender) from train where gender = '2'))/((select count(smoke) from train where smoke = '1' and gender = '1')/(select count(gender) from train where gender = '1'))) from train limit 1;
select ((select avg(age / 365) from train where smoke = '0')*12 - (select avg(age / 365) from train where smoke = '1')*12) from train limit 1;
select(select avg(cardio) from train where gender = '2' and age >= 60*365 and age <= 64*365 and smoke = '1' and ap_hi >= 160 and ap_hi < 180 and cholesterol = '1') / (select avg(cardio) from train where gender = '2' and age >= 21900 and age <= 64*365 and smoke = '1' and ap_hi < 120 and cholesterol = '1') from train limit 1;
select (select avg(weight) from train where gender = '2' )/(select  avg(pow(height/100,2)) from train where gender = '2' ) from train  limit 1 ;
select (select avg(weight) from train where cardio = '0' and gender = '2' and alco = '0' )/(select  avg(pow(height/100,2)) from train where cardio = '0' and gender = '2' and alco = '0' ) from train  limit 1 ;
select id from train where height >= percent_rank(0.025, height) limit 1;