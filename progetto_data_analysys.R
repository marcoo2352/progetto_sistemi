rm(list = ls())
worker <- read.csv("C:\\Users\\Marco\\Documents\\Uni\\sistemi 2\\progetto2\\Impact_of_Remote_Work_on_Mental_Health.csv")

#######################  R(1) #################################################################
worker$bin_mental_health <- ifelse(worker$Mental_Health_Condition == "None", 0, 1)
table_mh <- with(worker, table(worker$Work_Location, worker$bin_mental_health))
prop.table(table_mh,1)
chisq.test(table_mh)

# secondo questo test non ci sono presupposti per rifiutare l'ipotesi nulla 

####################### 
str(worker)

plot(worker$Number_of_Virtual_Meetings)
