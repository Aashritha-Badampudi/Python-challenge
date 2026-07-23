#To find no. of digits in my string
a="honey@123"
count=0
for i in a:
    if i.isdigit()==True:
        count+=1
print("No. of digits:",count)
    