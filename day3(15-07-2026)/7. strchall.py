#To find no. of special charecters in the given string:
a="password#123@"
count=0
for i in a:
    if i.isalnum()==False:
        count+=1
print("No. of special charecters are:",count)