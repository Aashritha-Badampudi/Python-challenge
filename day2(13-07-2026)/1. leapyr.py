#we will get leap year when the yr is (divisible by 4 and not divisible by 100) or divisible by 400
y=1993
if (y%4==0 and y%100!=0) or y%400==0:
    print("It is a leap year")
else:
    print("It is not a leap year")