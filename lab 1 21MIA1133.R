std<-c("shankar","santosh","Bami","Dwarak","Viswa")
marks<-c(10,8,9,8,10)
for (x in 1:(length(std))) {
  assign(std[x],marks[x])
}
Bami

details<-c(std,marks)

length(details)

std[which.min(marks)]

std[which.max(marks)]

sum(marks)

mean(marks)

sd(marks)

sort(marks)

rep_std <-rep(std, each =3)
rep_std

rep_marks <-rep(marks, each =3 )
rep_marks

seq <- 10:1
seq_marks <- c(marks,seq)
seq_marks

boolen <- marks>8
boolen