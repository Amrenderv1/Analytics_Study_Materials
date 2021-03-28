#Adding or loading files
data=EmployeeData
head(data)
library(sqldf)
sqldf('select * from data')

#Removing duplicated values if any
Data_without_duplicate=unique(data)
Data_without_duplicategr(Name,Dept,Salary)


#Using sqldf to get the desired output as mentioned

sqldf('select 
case
when salary BETWEEN 0 and 2000 then "Group 1"
when salary BETWEEN 2001 and 3000 then "Group 2"
when salary BETWEEN 3001 and 4000 then "Group 3"
when salary BETWEEN 4001 and 5000 then "Group 4"
when salary BETWEEN 5001 and 6000 then "Group 5"
end as salary_range,Dept,count(*) as Num_of_Employees
from Data_without_duplicate group by salary_range')

